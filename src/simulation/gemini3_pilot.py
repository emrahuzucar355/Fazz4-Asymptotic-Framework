import time
import sys
import random

# --- FAZZ-4: GEMINI 3 COMMAND CENTER (v2.0) ---
# STATUS: AGGRESSIVE EXPANSION | ARCHITECT: MIMAR
# ----------------------------------------------

class Derzz_Gemini_3_Pilot:
    def __init__(self):
        self.C = 299.792        # Işık Hızı (Simüle Katsayı)
        self.N_OBSERVER = 12    # Nizam Sabiti
        self.TARGET_DIST = 225000000 # Mars Hedef (km)
        self.cycle = 0
        self.total_energy = 0.0
        self.distance_traveled = 0
        
        print("\033[1;35m" + "="*60)
        print(f">>> GEMINI 3 COMMAND CENTER: ACTIVE <<<")
        print(f">>> PROTOKOL: AGGRESSIVE EXPANSION BAŞLATILDI")
        print("="*60 + "\033[0m")

    def flight_sim(self):
        try:
            while self.distance_traveled < self.TARGET_DIST:
                self.cycle += 1
                
                # Dinamik Fizik Hesaplamaları
                boost = random.uniform(1.0, 1.5) if self.cycle % 5 == 0 else 1.0
                step_dist = self.C * 500 * boost # Hızlandırılmış simülasyon
                self.distance_traveled += step_dist
                
                integrity = (self.distance_traveled / 1000) * (self.N_OBSERVER + 1)
                harvest = (step_dist * 0.00001) * random.random()
                self.total_energy += harvest
                
                # Progress Bar (%)
                percent = min(100, (self.distance_traveled / self.TARGET_DIST) * 100)
                bar_length = 20
                filled = int(bar_length * percent / 100)
                bar = "█" * filled + "-" * (bar_length - filled)
                
                # Renk Seçimi
                color = "\033[1;32m" if percent < 90 else "\033[1;33m"
                
                # ÇIKTI (Tek Satır Güncelleme)
                sys.stdout.write(
                    f"\r{color}[{bar}] {percent:4.1f}% \033[0m | "
                    f"Dist: {self.distance_traveled/1e6:6.1f}M km | "
                    f"ZIRH: {integrity:,.0f} | "
                    f"ENG: {self.total_energy:.1f}U"
                )
                sys.stdout.flush()

                # Rastgele Olaylar (Mimar Müdahalesi)
                if self.cycle % 15 == 0:
                    events = [
                        "SOLAR RÜZGAR HASAT EDİLİYOR",
                        "NİZAM SABİTİ SENKRONİZE EDİLDİ",
                        "MİMAR FORMÜLÜ GÜNCELLENDİ",
                        "RADYASYON KALKANI MAX KAPASİTE"
                    ]
                    print(f"\n\033[1;34m[SİSTEM] {random.choice(events)}\033[0m")
                
                time.sleep(0.1) # Hızlandırılmış akış

            print(f"\n\n\033[1;35m>>> HEDEF ULAŞILDI: MARS YÖRÜNGESİNE GİRİLDİ <<<\033[0m")
            print(f"\033[1;32mTOPLAM HASAT: {self.total_energy:.2f}U | NİZAM TAMAMLANDI.\033[0m")

        except KeyboardInterrupt:
            print(f"\n\n\033[1;31m[STOP] Pilot müdahalesi: ACİL DURUM DURDURMASI!\033[0m")

if __name__ == "__main__":
    pilot = Derzz_Gemini_3_Pilot()
    pilot.flight_sim()
