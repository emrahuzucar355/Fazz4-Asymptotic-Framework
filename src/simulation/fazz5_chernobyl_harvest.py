import time
import random
import math

class ChernobylHarvester:
    def __init__(self):
        self.C = 299.792
        self.N_OBSERVER = 12
        self.CEO_PANIC_THRESHOLD = (self.N_OBSERVER * (self.N_OBSERVER + 1)) / 2  # 78.0
        self.cycle = 0
        self.total_energy_mev = 0.0
        self.valve_activations = 0

    def run_harvest(self):
        print(f"\n☢️ [PROKOTOL: CHERNOBYL HARVESTER v5.0] - İNFAZ RAPORU")
        print(f"KONUM: Çernobil Reaktör 4 Çevresi | DURUM: Hiper-Rezonans Aktif")
        print(f"☢️ CHERNOBYL REZONANS SAHASINA GİRİLDİ...")
        print(f"[SİSTEM] CEO Panik Valfi Eşiği: {self.CEO_PANIC_THRESHOLD} Rezonans Birimi\n")
        
        try:
            while self.cycle < 50:
                self.cycle += 1
                
                # Derzz Fiziği
                l_path = self.C * self.cycle
                integrity = l_path * (self.N_OBSERVER + 1)
                
                # Çernobil Kaos Faktörü (Rastgele Radyasyon Patlamaları)
                chaos_flux = random.uniform(50, 150) * (self.cycle / 10)
                
                # Enerji Hasadı (a = l^2)
                harvest = (l_path ** 2) * 1e-9 * chaos_flux / 10000 # MeV
                
                # CEO Panik Valfi Kontrolü
                valve_status = ""
                if chaos_flux > self.CEO_PANIC_THRESHOLD * 10:
                    self.valve_activations += 1
                    valve_status = "\n⚠️ [CEO PANİK VALFİ] Aktif! Kaos Sisteme Geri Besleniyor..."
                    harvest *= 0.5 # Kaosun yarısı nizama dönüştü
                
                self.total_energy_mev += harvest
                
                # Görselleştirme
                rad_icon = "☢️" * (1 + int(chaos_flux / 200))
                if self.cycle % 5 == 0 or valve_status:
                    print(f"[{rad_icon:<5}] CYC:{self.cycle:03d} | L:{l_path:,.0f} | INTEGRITY:{integrity:,.0f} | HARVEST:{self.total_energy_mev:.4f} MeV{valve_status}")
                
                if self.cycle % 18 == 0:
                    print(f"[NOT] Çernobil Çekirdek Rezonansı: {self.N_OBSERVER * (self.N_OBSERVER+1)} Nizam Birimi.")

                time.sleep(0.05)

            print("-" * 60)
            print(f"[SİSTEM DURUMU]: KRİTİK NİZAM SAĞLANDI")
            print(f"TOPLAM HASAT: {self.total_energy_mev:.4f} MeV (Saf Enerjiye Dönüştürüldü)")
            print(f"CEO VALFİ MÜDAHALESİ: {self.valve_activations} Kez (Kaos Evcilleştirildi)")
            print("-" * 60)
            print("[STOP] Hasat Tamamlandı. Çernobil Radyasyonu Nizama Dönüştürüldü.")

        except KeyboardInterrupt:
            print("\n[!] Operasyon durduruldu.")

if __name__ == "__main__":
    ChernobylHarvester().run_harvest()
