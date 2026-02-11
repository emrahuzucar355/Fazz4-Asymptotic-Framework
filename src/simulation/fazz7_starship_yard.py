import time
import sys
import random

# --- FAZZ-7: HULL ASSEMBLY & TRAJECTORY LOCK ---
# TARGET: MARS (Red Planet)
# MATERIAL: Ag92-Gd7-DerzzType (The Monolith)
# ARCHITECT: MIMAR (COMMANDER)

class Derzz_Starship_Yard:
    def __init__(self):
        self.N_OBSERVER = 12
        self.alloy_code = "Ag92-Gd7"
        self.ship_integrity = 0
        self.mars_distance = 225_000_000 # km
        
        print("\033[1;36m>>> FAZZ-7: YÖRÜNGE TERSANESİ AKTİF <<<\033[0m")
        print("\033[1;33m[KOMUTAN] Mimar Yetkisi Doğrulandı. Montaj Başlıyor...\033[0m")

    def assemble_hull(self):
        print("\n[MONTAJ] Gümüş Yekpare (Monolith) İnşa Ediliyor...")
        sections = ["BURUN KONİSİ", "YAŞAM MODÜLÜ", "YAKIT TANKLARI", "ANA İTKİ SİSTEMİ"]
        
        for section in sections:
            # Görsel İnşa Efekti
            sys.stdout.write(f" > {section:<20} ........... ")
            for i in range(5):
                sys.stdout.write("█")
                sys.stdout.flush()
                time.sleep(0.1) # Hızlandırılmış simülasyon
            
            # Mukavemet Hesabı (Mimar Formülü)
            strength = (self.N_OBSERVER + 1) * random.uniform(980, 1020)
            self.ship_integrity += strength
            print(f" \033[1;32mOK (Mukavemet: {strength:.0f} GPa)\033[0m")
        
        print(f"\n\033[1;35m>>> GEMİ TAMAMLANDI: 'DERZZ-ONE' <<<\033[0m")
        print(f"TOPLAM BÜTÜNLÜK: {self.ship_integrity:,.0f} GPa")
        print(f"DIŞ ZIRH: {self.alloy_code} (Radyasyon Emici Aktif)")

    def calculate_trajectory(self):
        print("\n[NAVİGASYON] Mars Hohmann Transfer Rotası Hesaplanıyor...")
        
        # Astrodinamik Hesaplama
        delta_v = 3.6 # km/s (Dünya'dan kaçış)
        flight_time_days = 6 # Mimar'ın Hedefi (Hiper-İtki ile)
        
        # Rota Çizimi
        print(f" > HEDEF: Mars (Kızıl Gezegen)")
        print(f" > MESAFE: {self.mars_distance / 1e6} Milyon km")
        print(f" > GEREKLİ DELTA-V: {delta_v} km/s")
        print(f" > ÖNGÖRÜLEN SÜRE: {flight_time_days} GÜN (Hiper-İtki Aktif)")
        
        print("\n[SİSTEM] Rota Kilitleniyor...")
        for i in range(0, 101, 25):
            sys.stdout.write(f"\rHesaplanıyor: %{i}")
            sys.stdout.flush()
            time.sleep(0.2)
            
        print(f"\n\033[1;32m>>> ROTA KİLİTLENDİ (LOCKED) <<<\033[0m")
        print("\033[1;31m[UYARI] Kalkış İçin Komutan Emri Bekleniyor.\033[0m")

if __name__ == "__main__":
    yard = Derzz_Starship_Yard()
    yard.assemble_hull()
    yard.calculate_trajectory()
