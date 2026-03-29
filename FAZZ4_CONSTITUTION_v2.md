# FAZZ-4 PROTOCOL SYSTEM — BİRLEŞİK ANAYASA
## Kavramsal Çerçeve + Teknik Mimari

**DOI**: 10.5281/zenodo.19112378  
**Versiyon**: 2.0.0  
**Tarih**: Mart 2026  
**İmza**: Mimar Emrah Uzuçar — Uzuçar Law Office / Blue Line Architecture

---

> *"Eksik kavrayış = eksik fizik = eksik sistem."*  
> *"Muhteşem eksiklik — döngü kapanmaz, sistem yaşar."*

---

## ÖNSÖZ — Felsefi Zorunluluk

Bu anayasa iki katmandan oluşur.

**Birinci katman** felsefi zorunluluktur. Bir sistemi neden kurduğumuzu, hangi çerçeveden baktığımızı, kavrayışın mühendisliği nasıl öncelediğini tanımlar. Bu katman olmadan teknik maddeler doğru olabilir, ama sonuç yanlış olur. Isı, savrulma, kaos.

**İkinci katman** teknik mimaridir. Birinci katmanın gerektirdiği kararların uygulandığı yerdir. Teknisyenler burada çalışır.

Bu ikisi ayrı değildir. Zincirin halkalarıdır.

---

## MADDE 0 — TEK SABİT VE KAVRAMSAL ÇERÇEVE

### 0.1 Tek Sabit Nedir?

Evrenin yerel sınırlarını ve gözlemcinin kavrayışını belirleyen tek zorunlu çerçevedir. Bu sabit üç temel unsurdan oluşur ve bunlar eşkenar üçgenin köşeleridir:

```
           KAVRAMA YANSIMASI
           (Gözlem ve Bilginin Sınırı)
                    △
                   / \
                  /   \
                 /     \
                /       \
         IŞIK HIZI ——— MUTLAK SIFIR
    (Bilginin Yerel Sınırı)  (Enerjinin Sınırı)
```

**Işık Hızı (c):** Yerel evrende bilginin ve etkileşimin hareket sınırıdır. Bir seyahat limiti değil, gerçekliğin render hızıdır. `L = c·t`

**Mutlak Sıfır (0K):** Enerjinin ulaşılamaz tabanıdır. Fiziksel sınırlar burada kesin olarak işler. Asimptotik limit.

**Kavrama Yansıması:** Bir olgu yalnızca kavramsal olarak algılandığında gözlemlenebilir. Gözlemci olmadan üçgen tamamlanmaz — sınırın içi boş kalır.

> Üç köşeden biri eksik olduğunda üçgen çöker. Eksik kavrayış = eksik fizik = eksik sistem.

### 0.2 Geometrik Formül Zinciri

FAZZ-4'ün tüm teknik kararları bu zincirden türer:

| Formül | Anlamı | Kullanımı |
|--------|--------|-----------|
| `L = c·t` | Nedensel uzunluk — tepki süresinin ışık hızındaki karşılığı | Sistem tasarımında alan hesabı |
| `A = L²` | Holografik yüzey — bilgi kapasitesi hacimle değil yüzeyle ölçülür | Ağ kapsama alanı |
| `Σn = n(n+1)/2` | Ayrık nedensel birikim — ağdaki benzersiz bağlantı sayısı | Dağıtım topolojisi |

Bu formüller soyut değildir. Her mimari kararın arkasında bu geometri durur.

### 0.3 Zincir: Felsefi → Kavramsal → Teknik → Fiziksel

```
1. FELSEFİ ZORUNLULUK
   Neden? Hangi fenomeni görüyoruz? 
   Mavi orca nerede?
         ↓
2. KAVRAMSAL SABİT
   Tek Sabit üçgeni — hangi çerçeveden bakıyoruz?
   n(n+1)/2 ile olasılık alanı daralır.
         ↓
3. TEKNİK ARAYÜZ
   Teknisyenler tasarımı uygular.
   Bu anayasanın teknik maddeleri burada başlar.
         ↓
4. FİZİKSEL MODEL
   Somut fenomenler ve deneyler ortaya çıkar.
   Iz burada görünür.
```

Bu zincir fiziği kavramsal sabite mecbur bırakır. Zincirin herhangi bir halkası atlanırsa sistem kendi içinde entropi üretir.

### 0.4 Altlama ve Derzz

**Altlama:** Fiziksel yasalara pazarlıksız teslimiyet. Termödinomiğin sınırlarını, kaynak kısıtlarını, geri döndürülemezliği tartışmasız kabul etmek. Başlangıç noktası her zaman burasıdır.

**Derzz:** Altlama'nın bıraktığı aralıkta adaptif yönetim. `n(n+1)/2` bağlantı üzerinden kaosun yeniden dağıtılması, entropinin sisteme yeniden kazandırılması.

```
ALTLAMA: Sınırı kabul et → enerji harcama
DERZZ:   Aralıkta kal   → enerji kazan
```

### 0.5 Kusurlu Muhteşemlik

Mükemmel sistem nefes almaz. Tüm döngüleri kapatan sistem kendi içinden entropi üretir.

Bu anayasa kasıtlı olarak eksik bırakıldığı yerlere sahiptir. Bu zayıflık değil, tasarım ilkesidir. Kapanmayan döngü yaşayan sistemdir.

> *"Ne olursa olsun eksik kalır — ve bu tam olarak doğru."*

---

## MADDE 1 — AMAÇ VE VİZYON

### 1.1 Birincil Amaç

Tek Sabit çerçevesini — felsefi zorunluluktan fiziksel modele — yazılım sistemleri üzerinde operasyonel hale getirmek. Mac M2 Apple Silicon bu çerçevenin ilk fiziksel tezahür platformudur.

### 1.2 Vizyon

- Kavrama Yansıması'nı teknik kararlara taşıyan bir platform
- Bilimsel araştırmalar için güvenilir ve tekrarlanabilir altyapı
- Açık kaynak — iz bırakmak için değil, iziyle paylaşmak için
- Her modülün kendi Altlama muhasebesini tutması

### 1.3 Değer Önermeleri

| Değer | Teknik Karşılığı | Felsefi Kökü |
|-------|-----------------|--------------|
| **Şeffaflık** | Her karar dokümante | Altlama — kaybı gizleme |
| **Tekrarlanabilirlik** | Reproduce edilebilir süreçler | Berzah — aralık tutarlı kalır |
| **Eksiklik** | Mükemmel coverage hedeflenmez | Kusurlu Muhteşemlik |
| **Topluluk** | Katkıya açık sistem | Kavrayan Bilim — gözlemci içinde |
| **Performans** | Apple Silicon tam kullanım | Derzz — mevcut kaynaktan maksimum |

---

## MADDE 2 — SİSTEM MİMARİSİ

### 2.1 Katmanlı Mimari

```
┌─────────────────────────────────────────────┐
│  Kavrama Katmanı (Felsefi Zorunluluk)        │ ← Madde 0
├─────────────────────────────────────────────┤
│  Presentation Layer (CLI/API)                │ ← Kullanıcı Etkileşimi
├─────────────────────────────────────────────┤
│  Application Layer — Derzz Protokolü         │ ← İş Mantığı + Adaptif Yönetim
├─────────────────────────────────────────────┤
│  Domain Layer (Çekirdek Protokol)            │ ← L=ct, A=l², n(n+1)/2
├─────────────────────────────────────────────┤
│  Infrastructure Layer — Altlama Muhasebesi   │ ← Veri, Sistem, Fiziksel Sınırlar
└─────────────────────────────────────────────┘
```

Her katman bir alt katmandan beslenir. Domain katmanı hiçbir dış bağımlılığa sahip olamaz — bu Altlama'nın teknik karşılığıdır.

### 2.2 CEO Panik Valfi

Sistemin kaos altında stabilite koruması:

```python
def ceo_panik_valfi(flux: float, n: int) -> tuple:
    """
    n(n+1)/2 eşiği aşılırsa kaosun %50'si emilir.
    Müdahaleci değil — kavrayan tepki.
    
    Altlama: flux gerçektir, pazarlık yok.
    Derzz: emilen enerji sisteme nizam olarak döner.
    """
    sigma_n = n * (n + 1) / 2
    esik = sigma_n * 10
    valf_acik = flux > esik
    emilen = flux * 0.50 if valf_acik else 0.0
    return valf_acik, emilen, esik
```

### 2.3 Apple Silicon Optimizasyonu

- **ZORUNLU**: Tüm kritik modüller ARM64 native
- **ZORUNLU**: Unified Memory — sıfır kopyalama
- **TAVSİYE**: Metal API GPU yoğun işlemler
- **TAVSİYE**: Neural Engine ML çıkarımları

---

## MADDE 3 — MODÜLERLİK

### 3.1 Her Modül Kendi Berzah'ında

Her modül üç soruyu kendi içinde yanıtlamalıdır:

```
1. ALTLAMA: Bu modülün kaçınılmaz sınırı nedir?
2. DERZZ:   Aralıkta ne üretilir?
3. İZ:      Bu modül ne bırakır?
```

### 3.2 Plugin Arayüzü

```python
class FazzPlugin:
    """Her plugin kendi Altlama muhasebesini tutar."""
    
    def altlama(self) -> dict:
        """Fiziksel/teknik sınırları beyan et."""
        ...
    
    def derzz(self, context: Context) -> Result:
        """Aralıkta üret."""
        ...
    
    def iz(self) -> str:
        """Bu plugin ne bıraktı?"""
        ...
```

### 3.3 Geriye Dönük Uyumluluk

- Minor version: API uyumluluğu korunur
- Major version: Felsefi çerçeve değişmez, teknik uygulama değişebilir
- Berzah değişmez — iki asimptot sabit, aralık genişleyebilir

---

## MADDE 4 — GÜVENLİK

### 4.1 Defense in Depth — Kavrayan Güvenlik

Müdahaleci güvenlik: tehdidi durdur, zırhla, kapat.  
Kavrayan güvenlik: sistemin doğal frekanslarını koru, anomaliyi sinyal olarak oku.

```
1. Input Validation      — Altlama: giriş sınırını tanı
2. Authentication        — Kavrama: kim gözlemliyor?
3. Authorization         — Derzz: ne kadar erişim aralığı var?
4. Encryption            — AES-256-GCM / RSA-4096 / Ed25519
5. Audit Logging         — İz: her kritik işlem kayıt altında
```

### 4.2 Şifreleme Standartları

- **Symmetric**: AES-256-GCM
- **Asymmetric**: RSA-4096 veya Ed25519
- **Hashing**: SHA-256 minimum
- **Key Derivation**: Argon2 (tercih) veya PBKDF2

---

## MADDE 5 — KRİPTOGRAFİK BÜTÜNLÜK

- Tüm data paketleri SHA-256 checksum
- Kritik veriler dijital imzalanır
- TLS 1.3 minimum
- mTLS kurum içi iletişimde

---

## MADDE 6 — KOD KALİTESİ

### 6.1 Python Standartları

- PEP 8 uyumluluğu zorunlu
- Type hints her fonksiyonda
- Docstrings Google style
- Maximum line: 88 karakter
- McCabe complexity ≤ 10

### 6.2 Fazz-4 Özel Kural

Her fizik hesabı içeren fonksiyon şunu beyan etmeli:

```python
def hesap_fonksiyonu(param: float) -> float:
    """
    [ALTLAMA]: Bu hesabın fiziksel sınırı nedir?
    Ölçülen mi, hipotez mi? Fark edilmeli.
    
    [DERZZ]: Geriye ne kalıyor?
    
    Args:
        param: Açıklama
    Returns:
        Açıklama
    """
```

---

## MADDE 7 — TEST

### 7.1 Test Piramidi

```
        /\
       /  \    E2E (5%)
      /────\
     /      \  Integration (20%)
    /────────\
   /          \ Unit (75%)
  ──────────────
```

### 7.2 Altlama Testi

Her modül için zorunlu:

```python
def test_altlama_siniri():
    """
    Sistemin fiziksel/teknik sınırını test et.
    Bu sınır aşılmamalı — aşılırsa Altlama ihlali.
    """
    pass

def test_derzz_ciktisi():
    """
    Aralıkta üretilen çıktıyı test et.
    Kayıp gösterilmeli, gizlenmemeli.
    """
    pass
```

---

## MADDE 8 — DOKÜMANTASYON

### 8.1 Her ADR'de Felsefi Zorunluluk

```markdown
# ADR-NNN: Başlık

## Felsefi Zorunluluk
Bu kararın arkasındaki Kavrama Yansıması nedir?

## Altlama
Bu kararın kaçınılmaz teknik sınırı nedir?

## Derzz
Bu kararın aralıkta ürettiği değer nedir?

## Status
[Proposed | Accepted | Deprecated]

## Context / Decision / Consequences
...
```

---

## MADDE 9 — PERFORMANS HEDEFLERİ

| İşlem | P50 | P95 | P99 |
|-------|-----|-----|-----|
| API Response | <50ms | <100ms | <200ms |
| Protocol Processing | <100ms | <250ms | <500ms |
| n(n+1)/2 hesabı | <1ms | <5ms | <10ms |
| CEO Panik Valfi | <5ms | <10ms | <20ms |

**Kaynak Sınırları (Altlama):**
- Memory idle: < 500MB
- Memory peak: < 2GB  
- CPU average: < 30%
- Disk I/O: < 100MB/s

---

## MADDE 10 — ÖLÇEKLENEBİLİRLİK

- Stateless service design
- n(n+1)/2 topolojisi ölçekleme kararlarında referans
- Her yeni node: Derzz ağı genişler, sigma_n büyür
- Berzah korunur: sistem asla "tam" olmaz

---

## MADDE 11-14 — GÖZLEMLENEBILIRLIK

### Isı Anomali Tespiti (FAZZ-4 Özgün)

```python
# Standart metrik
request_duration_seconds

# FAZZ-4 metriği — Nizam Skoru
fazz4_nizam_score          # 0=kaos, 1=nizam
fazz4_isi_anomali          # nizamsız hareketin termal maliyeti
fazz4_ceo_valf_durumu      # açık/kapalı
fazz4_sigma_n              # n(n+1)/2 ağ büyüklüğü
```

**Alert Kuralları:**

| Metrik | Eşik | Tepki |
|--------|------|-------|
| Nizam < 0.4 | Warning | Derzz devreye girer |
| Nizam < 0.2 | Critical | CEO Valfi açılır |
| Isı anomali > eşik | Warning | Faz hizalama başlar |
| Error rate > 10% | Critical | Altlama muhasebesi |

---

## MADDE 15 — KATKI

### 15.1 Git Workflow

```
1. Fork
2. Feature branch: git checkout -b feature/kavrama-yansi
3. Commit: git commit -m 'feat(core): add kavrama layer'
4. PR açmadan önce: Altlama beyanı eklendi mi?
```

### 15.2 Commit Tipleri

```
feat:     Yeni kavrama katmanı veya teknik özellik
fix:      Hata düzeltme
altlama:  Sınır beyanı güncelleme
derzz:    Adaptif yönetim geliştirmesi
iz:       Dokümantasyon, iz bırakma
refactor: Yapısal iyileştirme
test:     Test ekleme
```

---

## MADDE 16 — TOPLULUK

- Saygılı ve yapıcı iletişim
- Kavrayan yaklaşım: eleştiri tehdit değil, sinyal
- Müdahaleci değil: "bu yanlış" değil, "hangi çerçeveden bakıyorsun?"
- Yeni gözlemcilere açık kapı

---

## MADDE 17 — LİSANS VE ATIF

**Lisans**: Creative Commons Attribution 4.0 International (CC BY 4.0)

```bibtex
@software{fazz4_protocol,
  author    = {Uzuçar, Emrah},
  title     = {FAZZ-4 Asymptotic Framework},
  year      = {2026},
  doi       = {10.5281/zenodo.19112378},
  url       = {https://github.com/emrahuzucar355/Fazz4-Asymptotic-Framework},
  note      = {Blue Line Architecture / Kavrayan Bilim Ekolü}
}
```

**Zenodo Zaman Damgası Zinciri:**

| Tarih | DOI | Katman |
|-------|-----|--------|
| 7 Ocak 2026 | 10.5281/zenodo.18169648 | İlk çerçeve |
| 24 Şubat 2026 | 10.5281/zenodo.18757772 | Paradigma ayrımı |
| 2 Mart 2026 | 10.5281/zenodo.18831923 | Radyoliz uygulaması |
| 2 Mart 2026 | 10.5281/zenodo.18183914 | Çernobil protokolü |
| 19 Mart 2026 | 10.5281/zenodo.19112378 | Revize çerçeve |
| 20 Mart 2026 | 10.5281/zenodo.19138329 | Kavrama Yansıması |

---

## MADDE 18-20 — VERİ VE BAKIM

*(Orijinal anayasanın Madde 18-20 teknik hükümleri aynen geçerlidir. Ek olarak:)*

Her yedekleme döngüsü kendi Altlama muhasebesini tutar:
- Ne kadar veri kaybedilebilir? (RPO)
- Ne kadar süre kesilebilir? (RTO)
- Berzah ne kadar geniş tutulabilir?

---

## MADDE 21 — EĞİTİM VE BİLGİ

### 21.1 Yeni Katılımcı için Önce Şunlar

```
1. Madde 0'ı oku — teknik maddelere geçme
2. n(n+1)/2'yi hesapla — neden bu topoloji?
3. Bir modülün Altlama muhasebesini bul
4. Sonra koda gir
```

---

## MADDE 22-24 — ANAYASA DEĞİŞİKLİKLERİ

**Değişmeyecek olan:**
- Tek Sabit üçgeni (Madde 0.1)
- Felsefi zorunluluk zinciri (Madde 0.3)
- Kusurlu Muhteşemlik ilkesi (Madde 0.5)

**Değişebilecek olan:**
- Teknik uygulama detayları
- Platform seçimleri
- Performans hedefleri

---

## MADDE 25 — İLETİŞİM

- **GitHub**: github.com/emrahuzucar355/Fazz4-Asymptotic-Framework
- **Zenodo**: doi.org/10.5281/zenodo.19112378
- **Email**: admin@blueline-arch.company
- **Ekol**: Blue Line Architecture — Kavrayan Bilim

---

## SON HÜKÜMLER

Bu anayasa 28 Ocak 2025'te başladı, Mart 2026'da ikinci versiyonuna ulaştı.

Kasıtlı olarak eksik yerleri vardır. Bu zayıflık değil, Kusurlu Muhteşemlik'in uygulamasıdır.

Döngü kapanmaz. Sistem yaşar.

---

## SÖZLÜK

| Terim | Tanım |
|-------|-------|
| **Tek Sabit** | c + 0K + Kavrama Yansıması üçgeni |
| **Kavrama Yansıması** | Gözlemcinin fenomeni çerçeveleme koşulu |
| **Altlama** | Fiziksel sınırlara pazarlıksız teslimiyet |
| **Derzz** | Aralıkta adaptif yönetim |
| **Berzah** | Üretken aralık — iki asimptot arası |
| **Kusurlu Muhteşemlik** | Kasıtlı eksiklik = yaşayan sistem |
| **CEO Panik Valfi** | n(n+1)/2 eşikli kaos emici |
| **Nizam** | Faz uyumlu düzen — ısısız akış |
| **İz** | Sistemin bıraktığı kalıcı iz |

---

**Belge Sorumlusu**: Mimar Emrah Uzuçar  
**Versiyon**: 2.0.0  
**DOI**: 10.5281/zenodo.19112378  
**Ekol**: Blue Line Architecture

---

*"Mükemmel mimari karmaşıklıkla değil, ölçeklenebilen zarif bir sadelikle ilgilidir."*  
*"Ve o sadelik her zaman biraz eksik kalır — tam olması gerektiği gibi."*
