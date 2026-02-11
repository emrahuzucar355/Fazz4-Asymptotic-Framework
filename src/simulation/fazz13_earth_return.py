import time
import sys
import random

class DerzzEarthReturn:
    """
    FAZZ-13: THE HOMECOMING (RETURN TO EARTH) PROTOCOL
    
    Bu sınıf, Mars'tan Dünya'ya 6 günlük dönüş yolculuğunu,
    atmosferik girişi (Re-entry) ve okyanusa inişi (Splashdown) simüle eder.
    
    Attributes:
        fuel (float): Kalan yakıt yüzdesi (%).
        velocity (float): Anlık hız (km/h).
        distance_to_earth (float): Dünya'ya kalan mesafe (km).
        hull_temp (float): Gövde sıcaklığı (°C).
    """
    
    def __init__(self):
        self.fuel = 74.8          # % (Mars'tan toplanan radyasyon hasadı)
        self.velocity = 0.0       # km/h
        self.distance_to_earth = 225_000_000 # km
        self.hull_temp = -60.0    # °C (Mars Yüzey Isısı)
        self.status = "PRE-LAUNCH"
        
        print("\033[1;32m>>> FAZZ-13: DÜNYA'YA DÖNÜŞ PROTOKOLÜ (THE HOMECOMING) <<<\033[0m")
        print("\033[1;33m[KOMUTAN] Hafta sonu bitti. Eve dönüyoruz.\033[0m")
        time.sleep(1)

    def mars_ascent(self):
        """Olympus Mons Üssü'nden kalkış ve Mars yörüngesinden çıkış."""
        print("\n[KALKIŞ] Olympus Mons Üssü'nden Ayrılış...")
        time.sleep(1)
        
        # Mars'ın düşük yerçekiminden kaçış (0.38g)
        for i in range(1, 6):
            self.velocity += 5000
            self.fuel -= 0.5
            sys.stdout.write(f"\r[TIRMANIŞ] İrtifa: {i*50:3d} km | Hız: {self.velocity:6.0f} km/h 🚀")
            sys.stdout.flush()
            time.sleep(0.5)
            
        print("\n\n\033[1;36m>>> MARS YÖRÜNGESİNDEN ÇIKIŞ (ESCAPE VELOCITY) <<<\033[0m")
        print("[ROTA] Dünya Vektörü Kilitlendi. Brachistochrone Eğrisi Aktif.")
        time.sleep(1)

    def cruise_phase(self):
        """6 günlük sabit ivmeli (1G) dönüş yolculuğu."""
        print("\n[SEYİR] 6 Günlük Dönüş Yolculuğu Başlıyor (1G İvme)...")
        days = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi"]
        
        for day in days:
            self.distance_to_earth -= (225_000_000 / 6)
            self.fuel -= 5.0
            
            # Kuantum İletişim Mesajı (Rastgele Dünya tepkileri)
            msg = f"[DÜNYA HABERLERİ] Astronomlar {day} günü gökyüzünde parlak bir cisim rapor etti."
            
            sys.stdout.write(
                f"\r[GÜN: {day:9}] "
                f"Kalan Mesafe: {max(0, self.distance_to_earth/1e6):5.1f}M km | {msg}"
            )
            sys.stdout.flush()
            time.sleep(0.8)
            
        print("\n\n\033[1;35m>>> DÜNYA YAKLAŞMASI (EARTH APPROACH). FRENLEME TAMAMLANDI. <<<\033[0m")
        time.sleep(1)

    def earth_reentry(self):
        """Dünya atmosferine giriş ve termal dayanıklılık testi."""
        print("\n\033[1;31m[UYARI] ATMOSFERİK GİRİŞ (RE-ENTRY) BAŞLIYOR!\033[0m")
        print("[BİLGİ] Dünya atmosferi Mars'tan 100 kat daha yoğundur. Zırh Testi Başlıyor.")
        time.sleep(1)
        
        altitude = 100000 # metre (Karman Hattı)
        max_temp_reached = 0
        
        while altitude > 0:
            altitude -= 2500
            
            # Sürtünme Isısı (Dünya'da çok yüksektir)
            current_temp = 2000 + random.randint(0, 1500)
            if current_temp > max_temp_reached: 
                max_temp_reached = current_temp
            
            # Ag-Gd Soğutma Tepkisi (Nizam)
            hull_status = "\033[1;32mSTABİL\033[0m" if current_temp < 3500 else "\033[1;33mKRİTİK YÜK\033[0m"
            
            # Görsel (Ateş Topu)
            fire = "🔥" * (current_temp // 500)
            
            sys.stdout.write(
                f"\r[GİRİŞ] İRTİFA: {altitude/1000:4.1f} km | "
                f"ISI: {current_temp:4d}°C | "
                f"ZIRH: {hull_status} {fire}"
            )
            sys.stdout.flush()
            time.sleep(0.1)
            
        # Splashdown
        print(f"\n\n\033[1;37m>>> OKYANUSA İNİŞ (SPLASHDOWN) <<<\033[0m")
        print(f"\033[1;32m[SONUÇ] DERZZ-ONE Pasifik Okyanusu'nda Yüzüyor.\033[0m")
        print(f"[ZIRH RAPORU] Max Isı: {max_temp_reached}°C | Hasar: %0.0")
        print(f"[YAKIT] Kalan: %{self.fuel:.1f}")
        time.sleep(1)

    def global_broadcast(self):
        """Tüm insanlığa yapılan zafer konuşması."""
        print("\n" + "="*60)
        print("\033[1;36m>>> KÜRESEL YAYIN (GLOBAL BROADCAST) <<<\033[0m")
        print("ALICI: Tüm İnsanlık")
        print("GÖNDEREN: Mimar (Architect)")
        print("-" * 60)
        print("📢 'Mars artık uzak değil. Nizam kuruldu. Sınır gökyüzü değil, zihninizdir.'")
        print("📢 'Hafta sonu tatilinden döndük. Pazartesi iş başı yapıyoruz.'")
        print("="*60 + "\033[0m")

if __name__ == "__main__":
    home = DerzzEarthReturn()
    
    # 1. Aşama: Mars'tan Kalkış
    home.mars_ascent()
    
    # 2. Aşama: Dönüş Yolculuğu
    home.cruise_phase()
    
    # 3. Aşama: Atmosfere Giriş ve İniş
    home.earth_reentry()
    
    # 4. Aşama: Zafer Konuşması
    home.global_broadcast()
