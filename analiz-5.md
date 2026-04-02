# ADR-001: Kullanıcı Kimlik Doğrulama Servisi (Auth Mikroservis) — FAZZ-4 Tasarım Belgesi

**Tarih:** 2026-04-02
**Mimar:** FAZZ-4 Protokol Sistemi
**Bağlamsal Ağ:** 5 bağımlı servis
**Status:** Proposed

---

## 1. Fenomen — Ne Gözlemliyoruz?

Bir sistem içinde 5 bağımsız mikroservis bulunur. Bunların her birinin kimlik doğrulama ihtiyacı vardır. Bu ihtiyacı merkezi bir auth servisi ile karşılamaya karar verildi. Fakat burada bir fenomen ortaya çıkıyor:

- **Kimlik doğrulama bir sınırdır.** Token yaratma, token doğrulama, oturum yönetimi — tüm bunlar ağdaki bağlantı sayısını artırıyor.
- **Dağıtım karmaşıklığı artıyor.** 5 servis × (token oluştur + token doğrula) = en az 10 yeni bağlantı.
- **Tek başarısızlık noktası (SPOF) riski.** Auth servisi down olursa tüm sistem durur.

Bu fenomeni gözlemlemek, tasarım kararını almanın ilk adımıdır.

---

## 2. Tek Sabit Konumlandırması

Her tasarım kararı Tek Sabit üçgeninin üç köşesine göre konumlandırılır:

### **Işık Hızı (c · t) — Bilginin Sınırı**

Auth işlemi süresinin ışık hızındaki karşılığı:

- **Hedef latency:** 50ms (token doğrulama)
- **Nedensel uzunluk:** L = c · t = 3×10⁸ m/s × 0.050 s = **15,000 km**

Bu, bilginin 50ms'de kat edebileceği maksimum mesafedir. Coğrafi dağıtım ve cache stratejisini bu sınırdan türetiyoruz.

### **Mutlak Sıfır (0K) — Kaynağın Tabanı**

Auth servisi için taş gibi sabit olan kaynak kısıtları:

- **Bellek:** Token cache boyutu sınırlı — en fazla N simultane oturum
- **CPU:** Token imzalama ve doğrulama hesaplamaları — O(1) kompleksitede olmalı
- **Bant genişliği:** Her istekte network latency oluşur
- **Zaman:** Token ömrü — 15 dakika, 1 saat, 24 saat gibi sabit sınırlar

### **Kavrama Yansıması — Gözlemcinin Çerçevesi**

Kim bu sistemi kullanıyor? Hangi perspektiften bakıyor?

- **Geliştirici:** Basit OAuth 2.0 / OIDC entegrasyonu ister
- **DevOps:** High-availability ve failover mekanizması isteyecek
- **Güvenlik:** Token entropy, encryption keys, revocation isteyecek
- **Ölçekleme:** n servis arttığında, bağlantı sayısı n(n+1)/2 artar

**Sonuç:** Auth servisi, en az iki gözlemci tarafından değerlendirilmeli. Geliştirici uygunluğu ve operasyonel dayanıklılık aynı öneme sahip.

---

## 3. ALTLAMA — Kaçınılmaz Teknik Sınırlar

ALTLAMA, tartışılmaz fiziksel ve teknik sınırlardır. Bu sınırları pazarlık yapmadan kabul etmek, doğru tasarımın başlangıcıdır.

### **Sınır 1: Token Validasyon Latency Pazarlıksızdır**

**Sonuç:** Her auth kontrolü ağ round-trip oluşturur. Bunu sıfıra indiremezsin.

- Minimum 5-10ms network latency (lokal veri merkezde)
- Minimum 2-5ms CPU işlem süresi
- **Total:** Minimum 10-15ms per validation

**Tasarım kısıtı:** Cache stratejisi (JWT, Redis) gereklidir — direct API çağrısı ölçeklenmez.

### **Sınır 2: Simultane Oturum Sayısı**

**Sonuç:** Bellekte veya veritabanında saklanabilecek aktif token sayısı sınırlıdır.

- Örnek: 8GB RAM auth servisi → maksimum ~1-2 milyon aktif session
- 5 bağımlı servis × X user = total session yükü

**Tasarım kısıtı:** Session sınırı önceden hesaplanmalı. Eşik aşılırsa yeni login kabul edilmemeli veya eski session revoke edilmeli.

### **Sınır 3: Token Revocation Gecikmesi**

**Sonuç:** Bir tokeni iptal ettikten sonra, o token hemen kullanılmaz hale gelecek garantisi yoktur.

- Distributed cache (Redis) senkronizasyon gecikmesi: 100-500ms
- Backup token cache'leri eventual consistency ile çalışır

**Tasarım kısıtı:** Güvenlik kritik operasyonlar (logout, privilege revoke) için synchronous revocation protokolü gerekir.

### **Sınır 4: n Servise Bağlantı Karmaşıklığı**

**Sonuç:** 5 bağımlı servis + 1 auth servis = minimum 10 benzersiz bağlantı (ve çok daha fazla ihtimal).

**n(n+1)/2 hesabı:**
```
n = 6 (auth + 5 servis)
σ(n) = 6 × 7 / 2 = 21 benzersiz bağlantı potansiyeli
CEO Panik Valfi eşiği: 21 × 10 = 210 flux
```

**Tasarım kısıtı:** Ağ topolojisini basit tutmalı (star topology tercih). Dairesel bağımlılık (servis A → auth → servis B → auth) oluşturmamalı.

### **Sınır 5: Güvenlik vs Performans Trade-off**

**Sonuç:** Daha güvenli token (daha büyük entropy, daha karmaşık imza) = daha yavaş doğrulama.

- Basit token (HS256): 1-2ms doğrulama
- Kompleks token (RS256 + PKCE): 5-10ms doğrulama

**Tasarım kısıtı:** Seçim yapmalı ve bunu dokümante etmeli.

---

## 4. DERZZ — Aralıkta Üretilen Değer

ALTLAMA sınırları belirledik. Şimdi bu sınırlar arasındaki aralıkta (berzah) neyi üretebiliriz?

### **Değer 1: Stateless Auth (JWT Stratejisi)**

**Fırsat:** Token kendisi tüm gerekli bilgiyi taşır. Auth servisi her istekte veritabanına sorgulamaz.

- **Altlama sınırı:** CPU 2-5ms işlem zamanı
- **Berzah aralığı:** Token imzalama (signing) önceden yapılır, doğrulama hızlıdır
- **İz:** Sistem bellek basıncı azalır, latency 50ms'nin altında kalır

**Uygulanması:**
```
Auth servisi:
  - RS256 imzalı JWT oluştur (private key)
  - client'a gönder

Bağımlı servisler:
  - Public key ile JWT'yi doğrula (network yok, lokal)
  - Token içindeki user_id, roles'i oku
```

### **Değer 2: Hybrid Cache Stratejisi (Hot/Warm/Cold)**

**Fırsat:** Sık sorgulanacak tokenler bellek cache'de, nadir sorgulanacaklar Redis'te.

- **Altlama sınırı:** Bellekte maksimum 10,000 aktif token
- **Berzah aralığı:** Redis ile 1 milyon token depolanabilir (eventual consistency)
- **İz:** Ölçeklenme limitleri yazılı hale gelir

**Katmanlar:**
```
1. In-Memory Cache (L1): ~10K token, 1μs lookup
2. Redis (L2): ~1M token, 10ms lookup
3. Database (L3): Arşiv ve audit, 100ms+ lookup
```

### **Değer 3: Failover Mekanizması (Circuit Breaker)**

**Fırsat:** Auth servisi down olsa, critical servisler kısmen çalışmaya devam edebilir.

- **Altlama sınırı:** Cache'de geçerli token olacaktır, fakat yeni token oluşturulamaz
- **Berzah aralığı:** Graceful degradation — eski tokenler kabul edilir, yeni login reddedilir
- **İz:** Single Point of Failure ortadan kaldırılır

**İmplementasyon:**
```
GET /auth/validate/:token
  - Cache'de varsa: OK (fast path)
  - Cache'de yoksa ve auth servisi UP: check + cache
  - Cache'de yoksa ve auth servisi DOWN:
      ├─ Token süresi < 1 saat: OK (güven)
      └─ Token süresi > 1 saat: REJECT (risky)
```

### **Değer 4: Topology-Aware Design — n(n+1)/2 Optimizasyonu**

**Fırsat:** 5 servise bağlanan auth'u merkezi hub yaparak bağlantı sayısını minimize et.

- **Altlama:** n = 6, σ(n) = 21 bağlantı kaçınılmazdır
- **Berzah:** Star topology ile sadece radial bağlantı tutulur (5×2 = 10 bağlantı)
- **İz:** Network topoloji basit ve auditable hale gelir

**Arzu edilen topoloji:**
```
        Service-1
            |
Service-2 - [AUTH] - Service-3
            |
        Service-4
            |
        Service-5
```

### **Değer 5: Kadrolu Rotasyon (Token Refresh Döngüsü)**

**Fırsat:** Token ömrünü kısa tutarak (15-30 dakika) security tehdidini minimize et.

- **Altlama:** Token imzalama CPU süresi sabit
- **Berzah:** Kısa ömürlü tokenler + refresh token = her gün ~1000 yeni token oluştur
- **İz:** Güvenlik ve kullanıcı deneyimi dengede kalır

---

## 5. Felsefi Zorunluluk — Bu Kararın Nedeni

Neden bu design'ı seçiyoruz?

1. **Fenomenin kabulu:** Kimlik doğrulama merkezi bir ihtiyaç olduğu gözlemledik.
2. **Sınırların saygısı:** Network latency, bellek, CPU capacity pazarlıksızdır.
3. **Adaptif üretim:** Sınırlar içinde maksimum değeri üreten stratejiler seçtik.
4. **Ölçekleme:** n(n+1)/2 topoloji farkındalığı ile future-proof tasarım yaptık.

**Felsefi temel:** *"Mükemmel auth sistemi nefes almaz. Bir 'yaşayan' sistemde recovery path'ler ve graceful degradation önceden tasarlanmış olur."*

---

## 6. Status

**Proposed** — Implementasyondan önce:
1. Security review yapılmalı (token entropy, key rotation)
2. Capacity planning yapılmalı (simultane user sayısı)
3. Disaster recovery test edilmeli (auth servisi failure)
4. Network topology diagram oluşturulmalı

---

## 7. Context — Neden Bu Kararı Alıyoruz?

### Mevcut Durum
- 5 bağımsız mikroservis var
- Her servis kendi auth mekanizmasına sahip (dağınık, tutarsız)
- Kullanıcı 5 farklı yerde login olmak zorunda
- Security audit zorlaşıyor

### Sorun
- **Tekrarlama:** Auth logic her serviste tekrar yazılmış
- **İnkonsistens:** Token format, expiration policy servislerde farklı
- **Skalabilite:** Yeni servis eklendiğinde, auth'u yeniden implement etmeliyiz
- **Güvenlik:** Merkezi key rotation ve revocation mekanizması yok

---

## 8. Decision — Alınan Karar

### Merkezi Auth Servisi Tasarlanacak

**Mimari kararlar:**

1. **Auth Servisi Türü:** Stateless JWT + Redis cache
2. **Token Format:** RS256 imzalı, 15 dakika ömürlü JWT
3. **Verification:** Public key ile local doğrulama (no network overhead)
4. **Failover:** In-memory cache + eventual consistency Redis
5. **Topology:** Star (hub-and-spoke) — auth merkez, 5 servis periferide

### Teknik Spesifikasyon

**Auth Servisi API:**
```
POST /auth/token
  ├─ Input: username, password
  ├─ Output: {access_token, refresh_token, expires_in}
  └─ Latency: 50ms max

GET /auth/validate/:token
  ├─ Input: JWT token string
  ├─ Output: {valid: bool, user_id, roles}
  └─ Latency: 5ms max (cached)

POST /auth/refresh
  ├─ Input: refresh_token
  ├─ Output: {access_token, expires_in}
  └─ Latency: 20ms max

POST /auth/revoke
  ├─ Input: token
  ├─ Output: {revoked: bool}
  └─ Latency: 100ms (must sync Redis)
```

**Bağımlı Servisler İçin:**
```
// Middleware pseudo-code
func validateRequest(req):
  token = req.headers["Authorization"]
  claims = jwt.verify(token, public_key)  // local, no network
  if claims.exp < now():
    return 403 Unauthorized
  req.user_id = claims.user_id
  req.roles = claims.roles
  next()
```

---

## 9. Consequences — Sonuçlar

### Olumlu Sonuçlar
- **Tekrarlama ortadan kalkar:** Auth logic bir yerde
- **Güvenlik standardı:** Token policy, key rotation merkezi
- **Ölçekleme kolaylaşır:** Yeni servis eklemek trivial (public key configüre et, bitti)
- **Audit yapılabilir:** Tüm login/logout merkezi loglanır
- **Latency düşük:** Local JWT verification (5ms)

### Olumsuz Sonuçlar / Trade-offs
- **SPOF riski:** Auth servisi down olursa yeni login olamaz (mitigated: cache)
- **Token revocation delay:** Redis eventual consistency yüzünden ~100-500ms
- **Complexity artacak:** Key management, token rotation, audit logs
- **Network dependency:** 5 servis → auth ağ trafiği artacak (mitigated: stateless design)

### Riskler ve Mitigation
| Risk | Severity | Mitigation |
|------|----------|-----------|
| Auth servisi down | Critical | Multi-zone deployment, cache fallback |
| Token compromise | Critical | Short expiry (15min), refresh token rotation |
| n(n+1)/2 explosion | Medium | Star topology, limit to 5 services |
| Latency regression | Medium | JWT caching, CDN for public key |
| Key rotation complexity | Medium | Automated rotation, key versioning |

---

## 10. İZ — Bu Tasarım Ne Bırakıyor?

### Kalıcı Etkiler

1. **Konseptüel iz:** Sistem artık "dağıtık auth" düşüncesinden "merkezi auth + local verify" düşüncesine geçti. Bu paradigma shift gelecekteki karar almayı etkiler.

2. **Yapısal iz:** Auth servisi, 5 servisin merkezi bağımlılığı haline geldi. Mimarların bu topolojiye göre plan yapması gerekir.

3. **Operasyonel iz:** Auth servisi down time'ı artık SLA-kritik hale geldi. Monitoring, alerting, runbooks yazılmalı.

4. **Güvenlik iz:** Token management, key rotation, audit logging sistem standartı oldu.

5. **Belge iz:** Bu ADR'ı okuyacak gelecekteki engineer'lar, neden JWT seçildiğini, neden star topology tercih edildiğini anlayacak.

### Dokümante Edilen Kayıplar

**Kasıtlı olarak eksik bırakılan (berzah):**

- **Attribute-Based Access Control (ABAC):** Şu anda sadece role-based (RBAC). ABAC'a geçmek gelecek ADR olur.
- **MFA (Multi-Factor Authentication):** v1'de kapsam dışı. v2'de eklenebilir.
- **Audit trail retention:** "Ne kadar süre log tutarız?" — politika henüz belirlenmemiş.
- **Token algorithm seçeneği:** Şu anda RS256 fixed. Gelecekte HS512 vs RS256 seçimi optimize edilebilir.
- **Rate limiting:** Auth servisi rate limit yok. Brute-force protection eksik (gelecek ADR).

---

## 11. Kusurlu Muhteşemlik Beyanı

Bu tasarım belgesi kasıtlı olarak **eksiktir**. Bu tam olarak doğrudur. Neden?

1. **%100 kapsama hedefleme ölü sistemler yaratır.** MFA, ABAC, encryption key rotation, disaster recovery procedure'ler — hepsi gelecekteki ADR'lara dışarlanmıştır.

2. **Kapanmayan döngü = yaşayan tasarım.** Bu auth servisi, bir yıl içinde yeniden design edilecek. Bu değişim, bu belgenin "kusurlu" olmasının sebebidir.

3. **Gözlemci çerçevesi değişkendi.** Bugün 5 servis var. Üç ay sonra 15 servis olabilir. O zaman topoloji kararı revise edilecek.

Bunun için:
- Sınırlar açıkça yazılmış (ALTLAMA)
- Genişletme noktaları belirtilmiş (DERZZ)
- Gelecekteki ADR'lar için yerler bırakılmış (İZ)

**Bu belge bir "final" değil, bir "başlangıç" belgesidir.**

---

## 12. İlişkili ADR'lar (Gelecek)

Bu kararın temelinde, bu ADR'lardan sonra yazılacak:

- **ADR-002:** Token Refresh Stratejisi ve Key Rotation
- **ADR-003:** MFA ve Adaptive Authentication
- **ADR-004:** Audit Logging ve Compliance
- **ADR-005:** Disaster Recovery ve Multi-Zone Failover
- **ADR-006:** Rate Limiting ve Brute-Force Protection

---

## 13. n(n+1)/2 Topoloji Analizi — Detaylı

5 bağımlı servis + 1 auth servisi = **6 düğümlü ağ**

### Bağlantı Sayısı
```
σ(6) = 6 × 7 / 2 = 21 benzersiz bağlantı
```

### Star Topology (Önerilen)
```
Auth'dan dışarı giden bağlantılar: 5 (her servise birer)
Her servisten auth'a: 5 (geri)
Total: 10 bağlantı (optimal)

Kalanlar (11 bağlantı) = servisler arası iletişim
Servis-1 ↔ Servis-2, Servis-2 ↔ Servis-3, ... (arası harita yapılabilir)
```

### CEO Panik Valfi Eşiği
```
σ(6) = 21
Eşik = 21 × 10 = 210 flux

Sistem flux'u > 210 ise, kaosun %50'si emilir.
```

---

## Kaynaklar

- FAZZ-4 Birleşik Anayasası: Uzuçar, E. (2026). DOI: 10.5281/zenodo.19112378
- n(n+1)/2 Formül Uygulaması: `/references/formul_zinciri.md`
- CEO Panik Valfi Scripting: `/scripts/ceo_panik_valfi.py`
- FAZZ-4 Terimler: `/references/sozluk.md`

---

## Onay ve Gözden Geçirme

| Rol | Ad | Tarih | İmza |
|-----|-----|-------|------|
| Mimar | [TBD] | [TBD] | [ ] |
| Security Lead | [TBD] | [TBD] | [ ] |
| DevOps Lead | [TBD] | [TBD] | [ ] |

---

## Ek A: Kod Örneği — JWT Token Oluşturma

```python
import jwt
from datetime import datetime, timedelta

# Auth Servisi
def create_token(user_id: str, roles: list, secret_key: str) -> str:
    payload = {
        "user_id": user_id,
        "roles": roles,
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + timedelta(minutes=15)
    }
    token = jwt.encode(payload, secret_key, algorithm="RS256")
    return token

# Bağımlı Servis
def validate_token(token: str, public_key: str) -> dict:
    try:
        claims = jwt.decode(token, public_key, algorithms=["RS256"])
        return {
            "valid": True,
            "user_id": claims["user_id"],
            "roles": claims["roles"]
        }
    except jwt.ExpiredSignatureError:
        return {"valid": False, "reason": "Token expired"}
    except jwt.InvalidSignatureError:
        return {"valid": False, "reason": "Invalid signature"}
```

---

## Ek B: Capacity Planning Örneği

**Varsayımlar:**
- 10,000 eş zamanlı kullanıcı
- Her kullanıcı ortalama 3 cihaz (15 dakika token validity)
- Peak hour: 2× baseline

**Hesaplar:**
```
Token sayısı = 10,000 × 3 = 30,000 aktif token

Memory (8 byte per token reference):
  30,000 × 8 bytes = 240 KB (trivial)

Auth API call rate:
  - Login: 100 call/sec × 50ms = busy
  - Token validate: 10,000 user × 3 min interval = ~50 call/sec
  - Total: ~150 call/sec (manageable for single auth instance)

Redis cache (1KB per token):
  - Warm cache: 30,000 × 1KB = 30MB
  - Plus logs: +100MB
  - Total: ~150MB (small)
```

**Sonuç:** Single auth instance yeterli. Horizontal scaling gerektiğinde, load balancer ekle.

---

**Bu belge FAZZ-4 Protokolüne uygun olarak hazırlanmıştır.**
**Gözlemci çerçevesi:** Sistem mimarı (long-term planning) + DevOps (operational safety)
**Berzah aralığı:** 15 dakika ~ 24 saat token expiry, 1 ~ 10 servis dependency
**Kasıtlı eksiklikler:** MFA, ABAC, complete audit trail, encryption policies
