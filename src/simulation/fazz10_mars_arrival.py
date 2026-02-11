import time
import sys
import random

class DerzzMarsArrival:
    """
    FAZZ-10: MARS ARRIVAL (FLIP & BURN) PROTOCOL
    
    Bu sınıf, uzay aracının Mars'a yaklaşırken yaptığı ters manevrayı (Retrograde Burn)
    ve yörüngeye giriş (Orbital Insertion) sürecini simüle eder.
    
    Attributes:
        velocity (float): Mevcut hız (km/h).
        target_velocity (float): Hedef yörünge hızı (km/h).
        distance_to_mars (float): Mars'a kalan mesafe (km).
        integrity (float): Gemi zırh bütünlüğü (%).
        fuel_pressure (float): Yakıt basıncı (Bar).
    """
    
    def __init__(self):
        self.velocity = 1_200_000.0       # km/h (Maksimum Seyir Hızı)
        self.target_velocity = 14_000.0   # km/h (Yörüngeye Giriş Hızı)
        self.distance_to_mars = 112_500_000 # km (Yarı yol/Frenleme Başlangıcı)
        self.integrity = 100.0            # Zırh %
        self.fuel_pressure = 78.0         # Bar
        
        print("\033[1;36m>>> FAZZ-10: MARS YAKLAŞMA VE FRENLEME PROTOKOLÜ AKTİF <<<\033[0m")
        print("\033[1;33m[NAVİGASYON] Yarı Yol (Midpoint) Geçildi. Dönüş Hazırlığı...\033[0m")
        time.sleep(1)

    def flip_maneuver(self):
        """
        Gemiyi 180 derece döndürerek motorları gidiş yönünün tersine (Retrograde) çevirir.
        """
        print("\n\033[1;35m[UYARI] GEMİ 180 DERECE DÖNDÜRÜLÜYOR (RETROGRADE)...\033[0m")
        angles = [0, 45, 90, 135, 180]
        
        for angle in angles:
            # Görsel Dönüş Efekti
            sys.stdout.write(f"\r[JİROSKOP] Dönüş Açısı: {angle}° " + "↺" * (angle // 45))
            sys.stdout.flush()
            time.sleep(0.3) 
            
        print(f"\n\n\033[1;32m>>> DÖNÜŞ TAMAMLANDI. MOTORLAR FRENLEME POZİSYONUNDA. <<<\033[0m")
        print("[SİSTEM] G-KUVVETİ YÖN DEĞİŞTİRDİ. YERÇEKİMİ 'TAVAN'DAN 'TABAN'A GEÇİYOR.")
        time.sleep(1)

    def suicide_burn(self):
        """
        Ana motorları ateşleyerek hızı düşürür (Deceleration Burn).
        Suicide Burn: Son ana kadar bekleyip maksimum güçle frenleme.
        """
        print(f"\n\033[1;31m[KOMUTAN] FRENLEME BAŞLATILIYOR (DECELERATION BURN)!\033[0m")
        time.sleep(1)
        
        burn_cycle = 0
        while self.velocity > self.target_velocity:
            burn_cycle += 1
            
            # Frenleme Formülü (Derzz Fiziği: Ters İvme)
            # Yakıt basıncı ve rastgele faktörlerle frenleme gücü
            deceleration = (self.fuel_pressure * 200) + random.uniform(0, 500)
            
            # Hız düşüşü ve mesafe kısalması
            self.velocity -= deceleration
            self.distance_to_mars -= (self.velocity / 3600) * 0.1 # Zaman ölçeklemesi
            
            # Zırh Stresi (Frenleme sırasında yapısal yük)
            if burn_cycle % 10 == 0:
                stress = random.uniform(0.01, 0.05)
                self.integrity -= stress

            # Durum Güncellemesi (Her 15 döngüde veya son aşamada)
            if burn_cycle % 15 == 0 or self.velocity <= self.target_velocity + deceleration:
                # Hıza göre renk kodları
                if self.velocity > 500_000: color = "\033[1;31m"   # Kırmızı (Çok Hızlı)
                elif self.velocity > 100_000: color = "\033[1;33m" # Sarı (Orta)
                else: color = "\033[1;32m"                         # Yeşil (Güvenli)
                
                print(f"{color}[FRENLEME T+{burn_cycle:02d}s] "
                      f"HIZ: {self.velocity:9,.0f} km/h | "
                      f"MESAFE: {max(0, self.distance_to_mars/1e6):6.2f}M km\033[0m")
                
                time.sleep(0.05) 
                
        print(f"\n\033[1;36m>>> HEDEF HIZA ULAŞILDI. MARS YERÇEKİMİ YAKALADI. <<<\033[0m")
        time.sleep(1)

    def orbital_insertion(self):
        """Mars yörüngesine giriş ve irtifa sabitleme."""
        print("\n[NAVİGASYON] Mars Yörüngesine Giriliyor (Orbital Insertion)...")
        print(f"[ZIRH DURUMU] Ag92-Gd7 Bütünlüğü: %{self.integrity:.2f}")
        time.sleep(1)
        
        orbit_alt = 20000 # km
        target_orbit = 400 # km (Low Mars Orbit)
        
        while orbit_alt > target_orbit:
            orbit_alt -= 2000
            if orbit_alt < target_orbit: orbit_alt = target_orbit
            
            sys.stdout.write(f"\r[YÖRÜNGE ALÇALMA] İrtifa: {orbit_alt:5d} km ...")
            sys.stdout.flush()
            time.sleep(0.1)
            
        print(f"\n\n\033[1;35m>>> GÖREV BAŞARILI: DERZZ-ONE MARS YÖRÜNGESİNDE! <<<\033[0m")
        print(f"\033[1;32m[GÖRÜNTÜ] Kızıl Gezegen Pencerede. Olympus Mons Selamlıyor.\033[0m")

if __name__ == "__main__":
    arrival = DerzzMarsArrival()
    
    # 1. Adım: Ters Dönüş
    arrival.flip_maneuver()
    
    # 2. Adım: Frenleme
    arrival.suicide_burn()
    
    # 3. Adım: Yörüngeye Giriş
    arrival.orbital_insertion()
