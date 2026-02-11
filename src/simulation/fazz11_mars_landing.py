import time
import sys
import random

class DerzzMarsLanding:
    """
    FAZZ-11: THE LANDING (PRECISION DESCENT) PROTOCOL
    
    Bu sınıf, Mars yörüngesinden yüzeye (Olympus Mons Base) yapılan
    itkili iniş (Powered Descent) manevrasını simüle eder.
    Paraşüt kullanılmaz, sadece Ag-Gd motorları ile frenleme yapılır.
    
    Attributes:
        altitude (float): Yüzeyden yükseklik (metre).
        velocity (float): İniş hızı (km/h).
        fuel (float): Kalan yakıt yüzdesi (%).
        hull_temp (float): Gövde sıcaklığı (°C).
    """
    
    def __init__(self):
        self.altitude = 400000.0  # metre (400 km - Yörünge İrtifası)
        self.velocity = 14000.0   # km/h (Yörünge Hızı)
        self.fuel = 12.0          # % (Kalan Rezerv)
        self.hull_temp = -120.0   # °C (Uzay Soğuğu)
        self.status = "ORBITAL"
        
        print("\033[1;31m>>> FAZZ-11: MARS YÜZEY İNİŞ PROTOKOLÜ (SILENT DESCENT) <<<\033[0m")
        print("\033[1;33m[KOMUTAN] 'Sakin İniş' Modu Aktif. Paraşütler Devre Dışı. Sadece İtki.\033[0m")
        time.sleep(1)

    def deorbit_burn(self):
        """Yörüngeden çıkış ateşlemesi (De-Orbit Burn)."""
        print("\n[NAVİGASYON] Yörüngeden Çıkış Ateşlemesi (De-Orbit Burn)...")
        time.sleep(1)
        print(" > Rota: Olympus Mons Etekleri")
        print(" > Eğim: 12 Derece (Sığ Giriş)")
        
        # Hızı düşürüp irtifa kaybetme simülasyonu
        for _ in range(3):
            self.velocity -= 2000
            sys.stdout.write(f"\r[MOTORLAR] Frenleme... Hız: {self.velocity:,.0f} km/h 📉")
            sys.stdout.flush()
            time.sleep(0.8)
            
        print("\n\n\033[1;32m>>> ATMOSFERİK GİRİŞ ARAYÜZÜNE ULAŞILDI <<<\033[0m")
        time.sleep(1)

    def atmospheric_entry(self):
        """Mars atmosferine giriş ve sürtünme ısısı yönetimi."""
        print("\n\033[1;35m[GİRİŞ] Mars Atmosferi ile Temas (Entry Interface)...\033[0m")
        time.sleep(1)
        
        # 10 km kalana kadar atmosferik frenleme
        while self.altitude > 10000: 
            # İrtifa azalırken hız ve sıcaklık artışı/düşüşü
            drop_rate = self.velocity / 100
            self.altitude -= drop_rate
            
            # Sürtünme ısısı artışı
            self.hull_temp += random.uniform(50, 150) 
            
            # Ag-Gd Zırhının Termal Yönetimi (Mimar Dokunuşu)
            # Zırh ısınır ama Gadolinyum sayesinde ısıyı enerjiye çevirir
            # Max sıcaklık limiti (Nizam)
            if self.hull_temp > 1500: 
                self.hull_temp = 1200 
            
            # Hız atmosferik sürtünmeyle azalır
            self.velocity *= 0.95
            
            # Görselleştirme (Plazma Rengi)
            plasma_color = "\033[1;31m" if self.hull_temp > 1000 else "\033[1;33m"
            bar = "▒" * int(self.altitude / 20000)
            
            sys.stdout.write(
                f"\r{plasma_color}[PLAZMA] "
                f"ALT: {self.altitude/1000:6.1f} km | "
                f"HIZ: {self.velocity:6.0f} km/h | "
                f"ISI: {self.hull_temp:4.0f}°C (Ag-Gd Stabil) {bar}\033[0m"
            )
            sys.stdout.flush()
            time.sleep(0.1)
            
        print("\n\n\033[1;36m>>> SON YAKLAŞMA (FINAL APPROACH). MOTORLAR DEVREDE. <<<\033[0m")
        time.sleep(1)

    def touchdown(self):
        """Son 10 km - Powered Descent (İtkili İniş) ve Temas."""
        print("[SİSTEM] İniş Radarı: ZEMİN GÖRÜLDÜ. (Olympus Mons Base)")
        time.sleep(1)
        
        # Son yaklaşma döngüsü
        while self.altitude > 0:
            # Yakıt harcayarak hızı sıfırlama
            self.fuel -= 0.1
            if self.fuel < 0: self.fuel = 0
            
            # İrtifa kaybı
            current_drop = self.velocity / 10
            self.altitude -= current_drop
            
            # Hassas Frenleme Mantığı
            if self.altitude < 1000: 
                # 1000m altı: Yumuşak dokunuş için hız = irtifa / 2
                target_v = self.altitude / 2
                if self.velocity > target_v:
                    self.velocity = target_v
            elif self.velocity > 300: 
                # 1000m üstü: Hızı kademeli düşür
                self.velocity -= 50
            
            # Temas kontrolü
            if self.altitude < 5: 
                self.altitude = 0 
                self.velocity = 0
            
            # Toz Kalkma Efekti (Son 500m)
            dust = "🌫️" if self.altitude < 500 else ""
            
            sys.stdout.write(
                f"\r\033[1;32m[İNİŞ] "
                f"İRTİFA: {self.altitude:5.1f} m | "
                f"DİKEY HIZ: {self.velocity:4.1f} km/h | "
                f"YAKIT: %{self.fuel:.1f} {dust}\033[0m"
            )
            sys.stdout.flush()
            time.sleep(0.15)
            
            if self.altitude == 0:
                break

        # Başarı Mesajı
        print(f"\n\n\033[1;37m>>> TEMAS (TOUCHDOWN). MOTORLAR KAPALI. <<<\033[0m")
        print(f"\033[1;31m>>> MARS YÜZEYİNE HOŞ GELDİNİZ, KOMUTAN. <<<\033[0m")
        print(f"DIŞ ORTAM: -63°C | BASINÇ: 600 Pa | RADYASYON: Ag-Gd Tarafından Emiliyor.")

if __name__ == "__main__":
    lander = DerzzMarsLanding()
    
    # 1. Aşama: Yörüngeden Çıkış
    lander.deorbit_burn()
    
    # 2. Aşama: Atmosferik Giriş
    lander.atmospheric_entry()
    
    # 3. Aşama: İniş ve Temas
    lander.touchdown()
