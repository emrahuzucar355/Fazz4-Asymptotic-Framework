p.p1 {margin: 0.0px 0.0px 0.0px 0.0px; font: 13.0px 'Helvetica Neue'; min-height: 15.0px} p.p2 {margin: 0.0px 0.0px 0.0px 0.0px; font: 13.0px 'Helvetica Neue'} p.p3 {margin: 0.0px 0.0px 2.0px 0.0px; font: 16.0px 'Helvetica Neue'}

import time
import sys
import random

--- FAZZ-8: GRAND LAUNCH SEQUENCE ---

MISSION: EARTH -> MARS (6 DAYS)

SHIP: DERZZ-ONE (Ag92-Gd7)

COMMANDER: MIMAR

class Derzz_Launch_Control:
  def init(self):
    self.t_minus = 10
    self.velocity = 0.0 # km/h
    self.altitude = 0.0 # km
    self.g_force = 1.0
    self.status = "GO FOR LAUNCH"
     
  def system_check(self):
    checks = [
      ("NİZAM SABİTİ", "SENKRONİZE"),
      ("HİDROJEN BASINCI", "78 BAR (OPTİMAL)"),
      ("GÜMÜŞ ZIRH", "SOĞUTMA AKTİF"),
      ("NAVİGASYON", "MARS KİLİTLİ"),
      ("MİMAR YETKİSİ", "DOĞRULANDI")
    ]
    print("\033[1;36m>>> FIRLATMA ÖNCESİ SON KONTROLLER (PRE-FLIGHT) <<<\033[0m")
    for system, state in checks:
      time.sleep(0.4)
      print(f" > {system:.<25} \033[1;32m{state}\033[0m")
    print("-" * 50)
    time.sleep(1)

def countdown(self):
    print("\n\033[1;33m[KULE] DERZZ-ONE, Fırlatma Pozisyonu Alındı. Geri Sayım Başlıyor...\033[0m")
    time.sleep(1)
     
    for i in range(self.t_minus, 0, -1):
      color = "\033[1;31m" if i <= 3 else "\033[1;37m"
      msg = ""
      if i == 6: msg = "(Ana Motorlara Hidrojen Akışı)"
      if i == 3: msg = "(Tutucu Kollar Ayrıldı)"
       
      sys.stdout.write(f"\r{color}>>> T-MINUS {i:02d} {msg} {' . ' * (i%3)}\033[0m")
      sys.stdout.flush()
      time.sleep(1)
      # Terminal temizleme efekti için boşluk
      sys.stdout.write("\r" + " "*60 + "\r")
       
    print("\n\033[1;32m>>> ATEŞLEME (IGNITION) <<<\033[0m")
    print("\033[1;35m>>> KALKIŞ (LIFTOFF)! DERZZ-ONE YÜKSELİYOR! <<<\033[0m")

def ascent_phase(self):
    # Atmosferden çıkış ve Hızlanma Simülasyonu
    try:
      start_time = time.time()
      while self.altitude < 400: # 400 km (LEO)
        elapsed = time.time() - start_time
         
        # Derzz İvmelenmesi (Exponential)
        self.velocity += (self.velocity * 0.05) + 150 # Agresif Hızlanma
        self.altitude += (self.velocity / 3600)
        self.g_force = 1 + (self.velocity / 5000)
         
        # Görsel Efektler
        bar = "▒" * int(self.altitude / 20)
        flame = "🔥" * (int(self.g_force))
         
        # Durum Mesajları
        stage = "ATMOSFERİK UÇUŞ"
        if self.altitude > 100: stage = "KARMAN HATTI GEÇİLDİ (UZAY)"
        if self.velocity > 28000: stage = "YÖRÜNGE HIZI (ORBITAL)"
         
        sys.stdout.write(
          f"\r\033[1;36m[{stage}]\033[0m "
          f"ALT: {self.altitude:6.1f} km | "
          f"HIZ: {self.velocity:8.0f} km/h | "
          f"G-KUVVETİ: {self.g_force:.1f}G {flame}"
        )
        sys.stdout.flush()
         
        # Max-Q Titreşimi (Aerodinamik Basınç)
        if 12 < elapsed < 15:
          time.sleep(0.2) # Zorlanma efekti
        else:
          time.sleep(0.08) # Hızlı akış

print(f"\n\n\033[1;32m>>> DÜNYA YÖRÜNGESİNE YERLEŞİLDİ (PARKING ORBIT) <<<\033[0m")
      print(f"\033[1;33m[KOMUTAN] Sırada: TRANS-MARS INJECTION (TMI) MANEVRASI.\033[0m")
      print(f"HEDEF VARIŞ SÜRESİ: 5 GÜN 23 SAAT 58 DAKİKA")

except KeyboardInterrupt:
      print("\n[ABORT] Fırlatma İptal Edildi.")

if name == "main":
  lc = Derzz_Launch_Control()
  lc.system_check()
  lc.countdown()
  lc.ascent_phase()
