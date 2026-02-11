import time
import sys
import random

# --- FAZZ-5.1: GADOLINIUM HYDRO-GEN PROTOCOL ---
# LOCATION: CHERNOBYL EXCLUSION ZONE (PRIPYAT)
# ELEMENT: GADOLINIUM (Gd-157)
# GOAL: RADIOLYSIS -> H2 PRODUCTION

class Chernobyl_Gadolinium_Core:
    def __init__(self):
        self.C = 299.792    # Işık Hızı (Reaksiyon Hızı)
        self.N_OBSERVER = 12  # Nizam Sabiti
        self.CEO_VALVE = (self.N_OBSERVER * (self.N_OBSERVER + 1)) / 2 # Sabit: 78
        
        # Gadolinium Özellikleri
        self.Gd_cross_section = 259000 # Barn (Nötron Yakalama Gücü)
        
        self.cycle = 0
        self.h2_tank = 0.0   # Depolanan Hidrojen (Litre)
        self.pressure = 0.0   # Tank Basıncı (Bar)
        
        print(f"\033[1;36m>>> GADOLINIUM MATRİSİ YERLEŞTİRİLDİ <<<\033[0m")
        print(f"\033[1;31m>>> ÇERNOBYL RADYASYON AKIŞI BAŞLATILIYOR...\033[0m")
        print("-" * 60)
        time.sleep(1)

    def panic_valve_release(self):
        """Basınç kritik seviyeyi aşarsa CEO Valfi devreye girer."""
        release_amount = self.pressure * 0.4
        self.pressure -= release_amount
        print(f"\n\033[1;35m⚠️ [CEO PANİK VALFİ] AÇIK! {release_amount:.2f} Bar Tahliye Edildi. Patlama Önlendi.\033[0m")
        return release_amount

    def run_reactor(self):
        try:
            while self.cycle < 250: # 250 döngülük üretim
                self.cycle += 1
                
                # 1. DERZZ ALAN FORMÜLÜ (a = l^2)
                l_interaction = (self.C / 1000) * (self.cycle * 0.01) 
                surface_area = l_interaction ** 2 
                
                # 2. RADYOLİZ MOTORU
                radiation_flux = random.uniform(500, 1200) 
                
                # H2 Üretim Formülü
                h2_production = (surface_area * radiation_flux * (self.Gd_cross_section/1e6)) / self.N_OBSERVER
                
                self.h2_tank += h2_production
                self.pressure += (h2_production * 0.05)
                
                # 3. GÖRSELLEŞTİRME
                tank_fill = "💧" * int(self.pressure / 10)
                
                # ÇIKTI
                sys.stdout.write(
                  f"\r\033[1;34m[H2 ÜRETİM]\033[0m "
                  f"CYC:{self.cycle:03d} | "
                  f"Gd-ETKİNLİK: {surface_area:.1f}nm² | "
                  f"TANK: {self.h2_tank:,.2f} L | "
                  f"BASINÇ: {self.pressure:.1f} Bar {tank_fill}"
                )
                sys.stdout.flush()
                
                # 4. GÜVENLİK KONTROLÜ
                if self.pressure > self.CEO_VALVE:
                  self.panic_valve_release()
                  time.sleep(0.5)

                time.sleep(0.05) 

            print(f"\n\n\033[1;32m[SİSTEM] Reaktör Kapatıldı. Depolanan Saf Hidrojen: {self.h2_tank:,.2f} Litre\033[0m")

        except KeyboardInterrupt:
            print(f"\n\n\033[1;31m[!] ACİL DURDURMA.\033[0m")

if __name__ == "__main__":
    Chernobyl_Gadolinium_Core().run_reactor()
