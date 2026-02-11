import time
import sys
import random

class DerzzMarsBase:
    """
    FAZZ-12: MARS COLONIZATION & QUANTUM LINK
    
    Bu sınıf, Mars yüzeyindeki 4 günlük ilk operasyonu simüle eder.
    - Kuantum Dolanıklığı ile anlık (0 ms) iletişim.
    - Ag-Gd zırhı ile pasif radyasyon emilimi ve yakıt üretimi.
    - Drone filosu ile yerleşke keşfi.
    
    Attributes:
        fuel_level (float): Yakıt yüzdesi (%).
        days_passed (int): Geçen gün sayısı.
        scout_drones (list): Aktif drone filosu.
        earth_link (str): Bağlantı durumu.
    """
    
    def __init__(self):
        self.fuel_level = 9.5  # % (İniş sonrası kalan rezerv)
        self.days_passed = 0
        self.scout_drones = ["Alpha", "Beta", "Gamma"]
        self.best_location = None
        self.earth_link = "CONNECTED (QUANTUM)"
        
        print("\033[1;31m>>> FAZZ-12: MARS YÜZEY OPERASYONU BAŞLATILDI <<<\033[0m")
        print("\033[1;36m[İLETİŞİM] Kuantum Dolanıklığı (Ag-Qubits) Aktif. Gecikme: 0.00 ms\033[0m")
        time.sleep(1)

    def quantum_chat(self, message):
        """
        Dünya ile anlık iletişim simülasyonu.
        Kuantum dolanıklığı sayesinde ışık hızı limiti (20 dk) aşılır.
        """
        print(f"\n\033[1;33m[MARS -> DÜNYA] {message}\033[0m")
        time.sleep(0.5)  # İşlem süresi (Mesafe gecikmesi yok)
        
        responses = [
            "Anlaşıldı Komutan. Görüntü net.",
            "Telemetri verileri kusursuz akıyor.",
            "Nizam Sabiti Dünya'da da stabil.",
            "Gümüş rezervleri güvenli, arkanızdayız.",
            "Lava tüplerine odaklanın, en iyi koruma orada."
        ]
        reply = random.choice(responses)
        print(f"\033[1;32m[DÜNYA -> MARS] {reply}\033[0m")

    def run_4_day_cycle(self):
        """
        4 Dünya Günü (96 Saat) süren yüzey operasyonu.
        Yakıt üretimi ve keşif döngülerini içerir.
        """
        total_hours = 96
        current_hour = 0
        
        print("\n[OPERASYON] 96 Saatlik Yüzey Döngüsü Başlıyor...")
        time.sleep(1)
        
        while current_hour < total_hours:
            current_hour += 4  # Simülasyon hızı: Her adım 4 saat
            
            # 1. RADYASYON HASADI (REFUELING)
            # Ag-Gd zırhı, Mars'ın ölümcül radyasyonunu yakıta çevirir.
            flux = random.uniform(1.2, 2.5)
            self.fuel_level += flux
            if self.fuel_level > 100: 
                self.fuel_level = 100
            
            # 2. DRONE KEŞİF (SCOUTING)
            found_site = None
            # Belirli saat aralıklarında keşif ihtimalleri
            if 20 < current_hour < 30: found_site = "Krater (Düşük Koruma)"
            if 40 < current_hour < 50: found_site = "Kanyon (Orta Koruma)"
            if 70 < current_hour < 80: found_site = "Lava Tüpü (Mükemmel Koruma)"
            
            if found_site:
                # Daha iyi bir yer bulursa günceller
                if found_site == "Lava Tüpü (Mükemmel Koruma)":
                    self.best_location = found_site
                elif self.best_location != "Lava Tüpü (Mükemmel Koruma)":
                    self.best_location = found_site
                    
                scout_msg = f"KEŞİF: {found_site} tespit edildi."
            else:
                scout_msg = "KEŞİF: Drone'lar tarıyor..."
            
            # Görselleştirme
            bar = "█" * int(self.fuel_level / 5)
            sys.stdout.write(
                f"\r[SAAT {current_hour:02d}/{total_hours}] "
                f"YAKIT: %{self.fuel_level:5.1f} {bar} | "
                f"{scout_msg}"
            )
            sys.stdout.flush()
            
            # Her 24 saatte bir (Günde 1) Dünya Raporu
            if current_hour % 24 == 0:
                self.days_passed += 1
                print(f"\n\n--- GÜN {self.days_passed} RAPORU ---")
                self.quantum_chat(f"Gün {self.days_passed} tamamlandı. Yakıt seviyesi %{self.fuel_level:.1f}. Keşif sürüyor.")
                print("-" * 50)
            
            time.sleep(0.3)
            
        # Görev Sonu Raporu
        print("\n\n\033[1;35m>>> 4 GÜNLÜK GÖREV TAMAMLANDI <<<\033[0m")
        print(f"[SONUÇ] Dönüş Yakıtı: %{self.fuel_level:.1f} (Tam Kapasite)")
        print(f"[KONUM] En Uygun Üs Bölgesi: \033[1;32m{self.best_location}\033[0m")
        print("[HAZIRLIK] Eve Dönüş veya Kalıcı Üs Kurulumu İçin Hazır.")
        
        

if __name__ == "__main__":
    base = DerzzMarsBase()
    base.run_4_day_cycle()
