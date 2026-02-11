import time
import sys
import random
import math

class DerzzTMIComputer:
    """
    FAZZ-9: TRANS-MARS INJECTION (TMI) PROTOCOL
    
    Bu sınıf, uzay aracının Dünya yörüngesinden kurtulup (Escape Velocity),
    Mars rotasına girmesi için gereken TMI manevrasını simüle eder.
    
    Attributes:
        current_velocity (float): Mevcut hız (km/h).
        escape_velocity (float): Dünya'dan kaçış hızı (km/h).
        mars_distance (int): Mars'a olan mesafe (km).
        fuel_pressure (float): Yakıt basıncı (Bar).
    """
    
    def __init__(self):
        self.current_velocity = 38650.0  # km/h (LEO Hızı - Low Earth Orbit)
        self.escape_velocity = 40320.0   # km/h (Dünya'dan Kaçış)
        self.mars_distance = 225_000_000 # km
        self.fuel_pressure = 78.0        # Bar
        self.status = "ORBITING"
        
        print("\033[1;36m>>> FAZZ-9: TRANS-MARS INJECTION (TMI) BİLGİSAYARI AKTİF <<<\033[0m")
        print("\033[1;33m[KOMUTAN] Yörünge Senkronizasyonu Bekleniyor...\033[0m")
        time.sleep(1)

    def alignment_check(self):
        """Dünya ve Mars'ın konum vektörlerini hizalar."""
        print("\n[NAVİGASYON] Mars Vektörü Hesaplanıyor...")
        alignment = 0
        
        while alignment < 100:
            # Rastgele bir hizalama hızı
            alignment += random.randint(5, 15)
            if alignment > 100: 
                alignment = 100
            
            # İlerleme Çubuğu
            bar = "█" * (alignment // 5)
            sys.stdout.write(f"\r[HİZALAMA] Açısı: {alignment}% {bar}")
            sys.stdout.flush()
            time.sleep(0.2)
        
        print(f"\n\033[1;32m>>> VEKTÖR KİLİTLENDİ. ATEŞLEME PENCERESİ AÇIK. <<<\033[0m")

    def execute_burn(self):
        """
        Ana motorları ateşleyerek yerçekimini yener ve kaçış hızına ulaşır.
        Derzz formülü ile ivmelenme simülasyonu yapar.
        """
        print(f"\n\033[1;31m[UYARI] ANA MOTORLAR %110 GÜÇLE ATEŞLENİYOR...\033[0m")
        print(f"\033[1;35m[CEO] Mimar, koltuğuna yapış. Bu seferki G-Kuvveti yerçekimini kıracak.\033[0m")
        time.sleep(2)
        
        # TMI Yakma İşlemi (Escape Velocity'e Ulaşma)
        burn_duration = 0
        
        # Kaçış hızının %50 üzerine çıkana kadar yakmaya devam et (Hızlı Transfer)
        target_velocity = self.escape_velocity * 1.5
        
        while self.current_velocity < target_velocity:
            burn_duration += 1
            
            # Agresif İvme (Derzz Formülü)
            # Hız her saniye katlanarak artar: Basınç + Süre etkisi
            acceleration = (self.fuel_pressure * 100) + (burn_duration * 50)
            self.current_velocity += acceleration
            
            # Görselleştirme (Warp Efekti)
            warp_effect = "═" * (burn_duration % 10)
            # Hızlandıkça renk beyaza (Doppler etkisi) döner
            color = "\033[1;37m" if self.current_velocity > 50000 else "\033[1;36m"
            
            sys.stdout.write(
                f"\r{color}[TMI ATEŞLEME T+{burn_duration:02d}s] "
                f"HIZ: {self.current_velocity:,.0f} km/h | "
                f"DURUM: {warp_effect}> YERÇEKİMİ KIRILIYOR <{warp_effect}\033[0m"
            )
            sys.stdout.flush()
            time.sleep(0.1)
        
        # Döngü bittikten sonra başarı mesajı
        print(f"\n\n\033[1;32m>>> DÜNYA YERÇEKİMİNDEN KURTULDU (ESCAPE VELOCITY REACHED) <<<\033[0m")
        print(f"\033[1;33m[NAVİGASYON] Rota: DERİN UZAY (DEEP SPACE). Sonraki Durak: MARS.\033[0m")
        print(f"ANLIK HIZ: {self.current_velocity:,.0f} km/h (ve artıyor...)")

    def cruise_mode(self):
        """Motorları kapatır ve sabit ivmeli seyir (cruise) moduna geçer."""
        # 6 Günlük Yolculuğun Başlangıcı
        print("\n[SİSTEM] Sabit İvme Moduna (1G) Geçiliyor...")
        print("[ZIRH] Ag-Gd Alaşımı: Stabil (-270°C Uzay Soğuğu vs Motor Isısı Dengede)")
        print("[YAKIT] Çernobil Hidrojeni: %98 Doluluk")
        print("-" * 50)
        print(f"\033[1;34m>>> DERZZ-ONE ARTIK BİR YILDIZ GEMİSİDİR. <<<\033[0m")

if __name__ == "__main__":
    tmi = DerzzTMIComputer()
    
    # 1. Adım: Hizalama
    tmi.alignment_check()
    
    # 2. Adım: Kullanıcı Onayı
    try:
        input("\n\033[1;31m[KOMUTAN] ATEŞLEME İÇİN [ENTER] TUŞUNA BASIN >> \033[0m")
        
        # 3. Adım: Ateşleme
        tmi.execute_burn()
        
        # 4. Adım: Seyir Modu
        tmi.cruise_mode()
        
    except KeyboardInterrupt:
        print("\n\n[İPTAL] Operasyon Komutan tarafından durduruldu.")
