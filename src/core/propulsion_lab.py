import time
import sys
import random
import math

class DerzzPropulsionLab:
    """
    FAZZ-6: METALLURGY & IGNITION PROTOCOL
    
    Bu sınıf, Mimar'ın Ag-Gd (Gümüş-Gadolinyum) alaşım oranlarını hesaplar
    ve Çernobil kökenli H2 yakıtının itki testini simüle eder.
    
    Attributes:
        fuel_tank (float): Yakıt tankındaki H2 miktarı (Litre).
        n_observer (int): Nizam Sabiti (Observer Constant).
        ag_atomic_mass (float): Gümüş'ün atomik kütlesi.
        gd_atomic_mass (float): Gadolinyum'un atomik kütlesi.
    """
    
    def __init__(self):
        # Başlangıç Değerleri
        self.fuel_tank = 7812.45  # Çernobil'den gelen saf H2 (Litre)
        self.n_observer = 12      # Nizam Sabiti
        
        # Fizik Sabitleri
        self.ag_atomic_mass = 107.86
        self.gd_atomic_mass = 157.25
        
        print("\033[1;36m>>> FAZZ-6: METALURJİ VE İTKİ LABORATUVARI AKTİF <<<\033[0m")
        print("-" * 60)
        time.sleep(1)

    def calculate_alloy(self) -> float:
        """
        Nizam Formülü ile Ag-Gd Alaşım Oranını ve Mukavemetini hesaplar.
        
        Formül:
          Ag Oranı = n / (n+1)
          Gd Oranı = 1 / (n+1)
          
        Returns:
            float: Alaşımın teorik mukavemet skoru (GPa).
        """
        print("\033[1;33m[METALURJİ] Gümüş-Gadolinyum (Ag-Gd) Alaşımı Hesaplanıyor...\033[0m")
        time.sleep(1)
        
        # Oran Hesaplamaları
        ratio_gd = 1 / (self.n_observer + 1)
        ratio_ag = self.n_observer / (self.n_observer + 1)
        
        # Yüzdelik Dönüşüm
        pct_ag = ratio_ag * 100
        pct_gd = ratio_gd * 100
        
        # Alaşım Mukavemeti (Simüle)
        # Formül: (Ag_mass * ratio_ag) + (Gd_mass * ratio_gd * n_observer)
        alloy_integrity = (self.ag_atomic_mass * ratio_ag) + (self.gd_atomic_mass * ratio_gd * self.n_observer)
        
        # Raporlama
        print(f" > NİZAM ORANI (n={self.n_observer}): 1'e {self.n_observer}")
        print(f" > GÜMÜŞ (Ag) ORANI:    %{pct_ag:.2f} (İletken Zırh)")
        print(f" > GADOLİNYUM (Gd) ORANI: %{pct_gd:.2f} (Nötron Avcısı)")
        print(f" > ALAŞIM KODU:       Ag{int(pct_ag)}-Gd{int(pct_gd)}-DerzzType")
        print(f" > MUKAVEMET SKORU:   {alloy_integrity:.2f} GPa (Teorik)")
        print("-" * 60)
        
        return alloy_integrity

    def ignition_test(self, alloy_strength: float):
        """
        Hesaplanan alaşım mukavemetine göre H2 yakıtının itki testini gerçekleştirir.
        
        Args:
            alloy_strength (float): calculate_alloy() fonksiyonundan dönen mukavemet değeri.
        """
        print(f"\n\033[1;31m[İTKİ TESTİ] {self.fuel_tank:.2f} Litre H2 Ateşleniyor...\033[0m")
        print(f"\033[1;34m[SİSTEM] Ag-Gd Alaşımlı Nozullar Hazır.\033[0m")
        time.sleep(2)
        
        burn_rate = 250.0  # Litre/Saniye Yanma Hızı (Baz)
        thrust_total = 0.0
        t = 0
        
        try:
            while self.fuel_tank > 0:
                t += 1
                
                # Yakıt Tüketimi (Dalgalı Yanma Simülasyonu)
                burn = min(self.fuel_tank, burn_rate * random.uniform(0.9, 1.1))
                self.fuel_tank -= burn
                
                # İtki Hesabı (F = m * ve) - Basitleştirilmiş
                # Alaşımın gücü itki verimini (Specific Impulse) artırır
                thrust = (burn * 4.5) * (alloy_strength / 100.0) 
                thrust_total += thrust
                
                # Görselleştirme (Ateş Efekti)
                flame_intensity = int(thrust / 1000) 
                flame = "🔥" * (flame_intensity if flame_intensity > 0 else 1)
                
                # Yakıt azaldıkça renk değişimi (Kırmızı -> Sarı)
                exhaust_color = "\033[1;31m" if self.fuel_tank < 1000 else "\033[1;33m"
                
                # Terminal Çıktısı (Satır içi güncelleme)
                sys.stdout.write(
                    f"\r{exhaust_color}[YANMA T+{t:02d}s] "
                    f"YAKIT: {self.fuel_tank:7.2f} L | "
                    f"GÜÇ: {thrust:6.0f} kN {flame}\033[0m"
                )
                sys.stdout.flush()
                time.sleep(0.15)
            
            # Test Sonu Raporu
            print(f"\n\n\033[1;32m>>> TEST TAMAMLANDI. YAKIT TÜKENDİ. <<<\033[0m")
            print(f"TOPLAM İTKİ GÜCÜ: {thrust_total:,.0f} kN")
            print(f"SONUÇ: Ag-Gd Alaşımı Termal Şoka Dayandı.")
            
        except KeyboardInterrupt:
            print("\n\n\033[1;31m[İPTAL] Test Manuel Olarak Durduruldu.\033[0m")

if __name__ == "__main__":
    # Laboratuvarı Başlat
    lab = DerzzPropulsionLab()
    
    # 1. Aşama: Alaşım Hesabı
    integrity_score = lab.calculate_alloy()
    
    # Mimar Onayı Bekleme Simülasyonu
    time.sleep(1)
    
    # 2. Aşama: Ateşleme Testi
    lab.ignition_test(integrity_score)
