import streamlit as st
import time
import random
import pandas as pd
import numpy as np
import math

# ============================================
# SAYFA YAPILANDIRMASI
# ============================================
st.set_page_config(page_title="FAZZ-4 Entegre Platform", layout="wide")
st.title("🌀 FAZZ-4 Entegre Simülasyon Platformu")
st.write("**Kavrayan Bilim:** `n(n+1)/2` ile entropiden enerjiye dönüşüm")

# ============================================
# YARDIMCI FONKSİYONLAR
# ============================================
def kavrama_yansimasi(n):
    return n * (n + 1) // 2

def format_number(num):
    return f"{num:,.0f}".replace(",", ".")

# ============================================
# MODÜL 1: MARS GÖREV KONTROLÜ (DERZZ VS STARSHIP)
# ============================================
def mars_gorev_kontrolu():
    st.header("🔴 Mars Görev Kontrolü – Derzz vs Starship")
    st.write("**FAZZ-4 Derzz** (sınırsız enerji) vs **Starship** (kimyasal yakıt) | Hedef: 225 milyon km")

    TARGET_DIST = 225_000_000  # km
    DERZZ_SPEED = 3000          # km/s (teorik)
    STARSHIP_SPEED = 7.5        # km/s
    STARSHIP_FUEL_CAPACITY = 1200  # ton
    FUEL_CONSUMPTION_RATE = 1200 / TARGET_DIST

    # Session state
    if "mars_derzz_dist" not in st.session_state:
        st.session_state.mars_derzz_dist = 0
        st.session_state.mars_starship_dist = 0
        st.session_state.mars_cycle = 0
        st.session_state.mars_energy = 0.0
        st.session_state.mars_fuel = STARSHIP_FUEL_CAPACITY
        st.session_state.mars_running = False
        st.session_state.mars_completed = False
        st.session_state.mars_starship_stopped = False

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🚀 GÖREVİ BAŞLAT", key="mars_start"):
            st.session_state.mars_running = True
            st.session_state.mars_completed = False
            st.session_state.mars_starship_stopped = False
            st.session_state.mars_derzz_dist = 0
            st.session_state.mars_starship_dist = 0
            st.session_state.mars_cycle = 0
            st.session_state.mars_energy = 0.0
            st.session_state.mars_fuel = STARSHIP_FUEL_CAPACITY
    with col2:
        if st.button("⏸️ DURDUR", key="mars_stop"):
            st.session_state.mars_running = False
    with col3:
        if st.button("🔄 SIFIRLA", key="mars_reset"):
            st.session_state.mars_derzz_dist = 0
            st.session_state.mars_starship_dist = 0
            st.session_state.mars_cycle = 0
            st.session_state.mars_energy = 0.0
            st.session_state.mars_fuel = STARSHIP_FUEL_CAPACITY
            st.session_state.mars_running = False
            st.session_state.mars_completed = False
            st.session_state.mars_starship_stopped = False

    col_prog1, col_prog2 = st.columns(2)
    with col_prog1:
        st.subheader("🚀 Derzz (FAZZ-4)")
        progress_derzz = st.progress(0, text="Derzz ilerleme")
    with col_prog2:
        st.subheader("🛰️ Starship")
        progress_starship = st.progress(0, text="Starship ilerleme")

    col_met1, col_met2, col_met3 = st.columns(3)
    with col_met1:
        dist_derzz = st.empty()
        dist_starship = st.empty()
    with col_met2:
        energy_derzz = st.empty()
        fuel_starship = st.empty()
    with col_met3:
        cycle_disp = st.empty()
        status = st.empty()

    if st.session_state.mars_running and not st.session_state.mars_completed:
        with st.spinner("Yolculuk devam ediyor..."):
            time_step = 3600  # 1 saat
            while st.session_state.mars_running and not st.session_state.mars_completed:
                st.session_state.mars_cycle += 1

                step_derzz = DERZZ_SPEED * time_step
                st.session_state.mars_derzz_dist += step_derzz
                if st.session_state.mars_derzz_dist > TARGET_DIST:
                    st.session_state.mars_derzz_dist = TARGET_DIST

                harvest = 15000 * 0.005 * time_step / 3600 * (1 + st.session_state.mars_cycle / 1000)
                st.session_state.mars_energy += harvest

                if st.session_state.mars_fuel > 0 and not st.session_state.mars_starship_stopped:
                    step_starship = STARSHIP_SPEED * time_step
                    st.session_state.mars_starship_dist += step_starship
                    if st.session_state.mars_starship_dist > TARGET_DIST:
                        st.session_state.mars_starship_dist = TARGET_DIST
                    fuel_used = step_starship * FUEL_CONSUMPTION_RATE
                    st.session_state.mars_fuel -= fuel_used
                    if st.session_state.mars_fuel < 0:
                        st.session_state.mars_fuel = 0
                else:
                    st.session_state.mars_starship_stopped = True

                percent_derzz = (st.session_state.mars_derzz_dist / TARGET_DIST) * 100
                percent_starship = (st.session_state.mars_starship_dist / TARGET_DIST) * 100

                progress_derzz.progress(int(percent_derzz), text=f"Derzz: %{percent_derzz:.2f}")
                progress_starship.progress(int(percent_starship), text=f"Starship: %{percent_starship:.2f}")

                dist_derzz.metric("Derzz Mesafe", f"{st.session_state.mars_derzz_dist/1e6:.2f} M km")
                dist_starship.metric("Starship Mesafe", f"{st.session_state.mars_starship_dist/1e6:.2f} M km")
                energy_derzz.metric("Derzz Enerji (kg H₂)", f"{st.session_state.mars_energy:.1f}")
                fuel_starship.metric("Starship Yakıt (ton)", f"{st.session_state.mars_fuel:.1f}")
                cycle_disp.metric("Saat (döngü)", st.session_state.mars_cycle)

                if st.session_state.mars_starship_stopped:
                    status.warning("🛑 Starship yakıtı bitti, yolculuk tamamlanamadı!")
                else:
                    status.info("▶️ Starship yolunda")

                if st.session_state.mars_derzz_dist >= TARGET_DIST:
                    st.session_state.mars_completed = True
                    st.balloons()
                    st.success("✅ DERZZ MARS'A ULAŞTI!")
                if st.session_state.mars_starship_dist >= TARGET_DIST:
                    st.session_state.mars_completed = True
                    st.balloons()
                    st.success("✅ STARSHIP MARS'A ULAŞTI!")

                time.sleep(0.1)

    if st.session_state.mars_completed:
        st.balloons()

# ============================================
# MODÜL 2: ÇEKİRDEK REAKTÖR
# ============================================
def cekirdek_reaktor():
    st.header("☢️ Çekirdek Reaktör")
    st.write("Radyasyon → Hidrojen dönüşümü (Gadolinyum katalizörlü)")

    col1, col2, col3 = st.columns(3)
    with col1:
        radyasyon = st.number_input("Radyasyon seviyesi (mSv/h)", 1000, 50000, 15000, step=1000)
    with col2:
        saat = st.slider("Simülasyon süresi (saat)", 1, 24, 10)
    with col3:
        gd_verim = st.slider("Gadolinyum verimi (%)", 50, 100, 92) / 100

    if st.button("▶️ REAKTÖRÜ ÇALIŞTIR", key="reaktor_start"):
        with st.spinner("Reaktör çalışıyor..."):
            sogurulan = radyasyon * gd_verim
            h2_kg = sogurulan * 0.005 * saat
            enerji_mj = h2_kg * 141.8

            data = []
            for t in range(1, saat+1):
                h2_t = sogurulan * 0.005 * t
                enerji_t = h2_t * 141.8
                data.append({"Saat": t, "H₂ (kg)": h2_t, "Enerji (MJ)": enerji_t})

            df = pd.DataFrame(data)
            st.line_chart(df.set_index("Saat"))
            st.success(f"**Sonuç:** {h2_kg:.2f} kg H₂ üretildi, {enerji_mj:.2f} MJ enerji elde edildi.")
            st.dataframe(df)

# ============================================
# MODÜL 3: KAHİN MODU
# ============================================
def kahin_modu():
    st.header("🔮 Kahin Modu")
    st.write("15000 evren olasılığında en iyi rotayı seçer")

    col1, col2 = st.columns(2)
    with col1:
        n_evren = st.number_input("Evren sayısı", 1000, 100000, 15000, step=1000)
    with col2:
        chaos = st.slider("Kaos faktörü (σ)", 0.01, 0.2, 0.05)

    if st.button("🌀 KAHİN MODUNU BAŞLAT", key="kahin_start"):
        with st.spinner(f"{n_evren} evren taranıyor..."):
            base_eff = 0.989
            alignments = 0
            leaks = 0
            results = []
            for i in range(min(n_evren, 10000)):
                chaos_val = np.random.normal(0, chaos)
                eff = base_eff + chaos_val
                if eff >= 0.99:
                    alignments += 1
                    status = "Hizalandı"
                elif eff < 0.90:
                    leaks += 1
                    status = "Kaçak"
                else:
                    status = "Stabil"
                if i % 1000 == 0:
                    results.append(f"Adım {i}: {status} | Verim: {eff:.4f}")

            alignment_prob = (alignments / min(n_evren, 10000)) * 100
            leak_prob = (leaks / min(n_evren, 10000)) * 100

            st.metric("Hizalanma Olasılığı", f"%{alignment_prob:.2f}")
            st.metric("Entropi Kaçağı", f"%{leak_prob:.2f}")
            st.write("**Örnek loglar:**")
            for r in results[:5]:
                st.text(r)

# ============================================
# MODÜL 4: DERZZ YARIŞI (KLASİK VS DERZZ)
# ============================================
def derzz_yarisi():
    st.header("🏁 Derzz Yarışı")
    st.write("Klasik motor (kırmızı) vs Derzz motoru (mavi)")

    TARGET = 10000
    FUEL_PRICE = 950

    if "yaris_c_dist" not in st.session_state:
        st.session_state.yaris_c_dist = 0
        st.session_state.yaris_d_dist = 0
        st.session_state.yaris_c_fuel = 0
        st.session_state.yaris_d_fuel = 0
        st.session_state.yaris_c_time = 0
        st.session_state.yaris_d_time = 0
        st.session_state.yaris_running = False
        st.session_state.yaris_completed = False

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🚦 YARIŞI BAŞLAT", key="yaris_start"):
            st.session_state.yaris_c_dist = 0
            st.session_state.yaris_d_dist = 0
            st.session_state.yaris_c_fuel = 0
            st.session_state.yaris_d_fuel = 0
            st.session_state.yaris_c_time = 0
            st.session_state.yaris_d_time = 0
            st.session_state.yaris_running = True
            st.session_state.yaris_completed = False
    with col2:
        if st.button("⏸️ DURDUR", key="yaris_stop"):
            st.session_state.yaris_running = False
    with col3:
        if st.button("🔄 SIFIRLA", key="yaris_reset"):
            st.session_state.yaris_c_dist = 0
            st.session_state.yaris_d_dist = 0
            st.session_state.yaris_c_fuel = 0
            st.session_state.yaris_d_fuel = 0
            st.session_state.yaris_c_time = 0
            st.session_state.yaris_d_time = 0
            st.session_state.yaris_running = False
            st.session_state.yaris_completed = False

    progress_c = st.progress(0, text="Klasik")
    progress_d = st.progress(0, text="Derzz")
    met1, met2, met3 = st.columns(3)
    with met1:
        c_dist = st.empty()
        d_dist = st.empty()
    with met2:
        c_cost = st.empty()
        d_cost = st.empty()
    with met3:
        c_time = st.empty()
        d_time = st.empty()

    if st.session_state.yaris_running and not st.session_state.yaris_completed:
        with st.spinner("Yarış devam ediyor..."):
            while st.session_state.yaris_running and (st.session_state.yaris_c_dist < TARGET or st.session_state.yaris_d_dist < TARGET):
                if st.session_state.yaris_c_dist < TARGET:
                    speed_c = 25 + random.randint(-10, 5)
                    st.session_state.yaris_c_dist += speed_c
                    st.session_state.yaris_c_fuel += (speed_c / 100) * 1.8
                    st.session_state.yaris_c_time += 1
                    if st.session_state.yaris_c_dist > TARGET:
                        st.session_state.yaris_c_dist = TARGET

                if st.session_state.yaris_d_dist < TARGET:
                    speed_d = 45
                    st.session_state.yaris_d_dist += speed_d
                    st.session_state.yaris_d_fuel += (speed_d / 100) * 0.85
                    st.session_state.yaris_d_time += 1
                    if st.session_state.yaris_d_dist > TARGET:
                        st.session_state.yaris_d_dist = TARGET

                pc = (st.session_state.yaris_c_dist / TARGET) * 100
                pd = (st.session_state.yaris_d_dist / TARGET) * 100
                progress_c.progress(int(pc), text=f"Klasik: %{pc:.2f}")
                progress_d.progress(int(pd), text=f"Derzz: %{pd:.2f}")

                c_dist.metric("Klasik Mesafe", f"{st.session_state.yaris_c_dist:.0f} km")
                d_dist.metric("Derzz Mesafe", f"{st.session_state.yaris_d_dist:.0f} km")
                c_cost.metric("Klasik Maliyet", f"${st.session_state.yaris_c_fuel * FUEL_PRICE:,.0f}")
                d_cost.metric("Derzz Maliyet", f"${st.session_state.yaris_d_fuel * FUEL_PRICE:,.0f}")
                c_time.metric("Klasik Zaman", f"{st.session_state.yaris_c_time} adım")
                d_time.metric("Derzz Zaman", f"{st.session_state.yaris_d_time} adım")

                time.sleep(0.05)

            st.session_state.yaris_completed = True
            st.success("Yarış tamamlandı!")
            tasarruf = (st.session_state.yaris_c_fuel - st.session_state.yaris_d_fuel) * FUEL_PRICE
            st.info(f"Derzz tasarrufu: ${tasarruf:,.2f}")

# ============================================
# MODÜL 5: ÇERNOBİL PROTOKOLÜ
# ============================================
def cernobil_protokolu():
    st.header("☢️ Çernobil Protokolü")
    st.write("Gadolinyum katalizörlü radyoliz ile hidrojen üretimi (Fil Ayağı)")

    if "cern_sonuc" not in st.session_state:
        st.session_state.cern_sonuc = None

    CAPTURE_EFFICIENCY_GD = 0.92
    col1, col2 = st.columns(2)
    with col1:
        saat = st.slider("Simülasyon saati", 1, 24, 10)
    with col2:
        st.metric("Radyasyon kaynağı", "15000 mSv/h (Fil Ayağı)")

    if st.button("☢️ HASADI BAŞLAT", key="cern_start"):
        with st.spinner("Radyasyon hasadı yapılıyor..."):
            corium_radiation = 15000
            absorbed_flux = corium_radiation * CAPTURE_EFFICIENCY_GD
            hydrogen_output_kg = absorbed_flux * 0.05 * saat
            energy_value_mj = hydrogen_output_kg * 141.8

            st.session_state.cern_sonuc = {
                "saat": saat,
                "h2": hydrogen_output_kg,
                "enerji": energy_value_mj
            }

            hours = list(range(1, saat+1))
            h2_per_hour = [absorbed_flux * 0.05 * t for t in hours]
            df = pd.DataFrame({"Saat": hours, "H₂ (kg)": h2_per_hour})
            st.line_chart(df.set_index("Saat"))

    if st.session_state.cern_sonuc:
        s = st.session_state.cern_sonuc
        st.success(f"{s['saat']} saatte üretilen H₂: {s['h2']:.2f} kg")
        st.success(f"Enerji değeri: {s['enerji']:.2f} MJ")

# ============================================
# MODÜL 6: ENTROPİ DÖNÜŞÜMÜ
# ============================================
def entropi_donusumu():
    st.header("♻️ Entropi Dönüşümü")
    st.write("Her entropi bir sonraki işlemin tetikçisi | `n(n+1)/2` ile sonsuz döngü")

    if "entropi_state" not in st.session_state:
        st.session_state.entropi_state = {
            "adim": 0,
            "enerji": 500,
            "entropi": 0,
            "calisiyor": False,
            "tamamlandi": False
        }

    col1, col2, col3 = st.columns(3)
    with col1:
        bas_enerji = st.number_input("Başlangıç Enerjisi", 100, 1000, 500, key="ent_enerji")
    with col2:
        ent_katsayi = st.slider("Entropi → Enerji katsayısı", 0.0001, 0.01, 0.001, step=0.0001)
    with col3:
        max_adim = st.number_input("Maksimum adım", 100, 1000, 200, step=50)

    b1, b2, b3 = st.columns(3)
    with b1:
        if st.button("▶️ BAŞLAT", key="ent_start"):
            st.session_state.entropi_state = {
                "adim": 0,
                "enerji": bas_enerji,
                "entropi": 0,
                "calisiyor": True,
                "tamamlandi": False
            }
    with b2:
        if st.button("⏸️ DURDUR", key="ent_stop"):
            st.session_state.entropi_state["calisiyor"] = False
    with b3:
        if st.button("🔄 SIFIRLA", key="ent_reset"):
            st.session_state.entropi_state = {
                "adim": 0,
                "enerji": bas_enerji,
                "entropi": 0,
                "calisiyor": False,
                "tamamlandi": False
            }

    progress_bar = st.progress(0, text="Entropi dönüşümü")
    col_a, col_b, col_c = st.columns(3)
    enerji_met = col_a.empty()
    entropi_met = col_b.empty()
    verim_met = col_c.empty()
    chart_place = st.empty()

    if st.session_state.entropi_state["calisiyor"] and not st.session_state.entropi_state["tamamlandi"]:
        data = []
        while (st.session_state.entropi_state["calisiyor"] and 
               st.session_state.entropi_state["adim"] < max_adim and
               st.session_state.entropi_state["enerji"] > 0.01):
            st.session_state.entropi_state["adim"] += 1
            adim = st.session_state.entropi_state["adim"]

            entropi_birikim = adim * (adim + 1) / 2
            st.session_state.entropi_state["entropi"] = entropi_birikim

            verim = 1 / (1 + entropi_birikim * 0.001)
            kazanilan = entropi_birikim * ent_katsayi
            harcanan = st.session_state.entropi_state["enerji"] * 0.02
            st.session_state.entropi_state["enerji"] = st.session_state.entropi_state["enerji"] - harcanan + kazanilan

            data.append({
                "Adım": adim,
                "Enerji": st.session_state.entropi_state["enerji"],
                "Entropi": entropi_birikim / 1000
            })

            progress_bar.progress(int(adim / max_adim * 100), text=f"Adım: {adim}/{max_adim}")
            enerji_met.metric("Kalan Enerji", f"{st.session_state.entropi_state['enerji']:.2f}")
            entropi_met.metric("Entropi Birikimi", f"{entropi_birikim:.0f}")
            verim_met.metric("Anlık Verim", f"{verim:.4f}")

            df = pd.DataFrame(data).set_index("Adım")
            chart_place.line_chart(df[["Enerji", "Entropi"]])

            time.sleep(0.05)

        st.session_state.entropi_state["tamamlandi"] = True
        st.success("Döngü tamamlandı (veya enerji sıfırlandı).")

# ============================================
# MODÜL 7: FAZZ-9 TMI (GERÇEKÇİ)
# ============================================
def tmi_manevrasi():
    st.header("🚀 FAZZ-9: Trans-Mars Injection (TMI)")
    st.write("**Gerçekçi uzay şartları simülasyonu** – Derzz-ONE ile Mars transferi")

    v_escape = 11.2
    v_leo = 7.8
    ve = 4.5
    mars_distance = 225e6
    G = 6.67430e-20

    with st.sidebar:
        st.subheader("TMI Parametreleri")
        hedef_hiz_kat = st.selectbox(
            "Hedef hız (kaçış hızı katı)",
            [1.2, 1.5, 2.0, 2.5, 3.0],
            index=1,
            help="Kaçış hızının katı. Daha yüksek hız = daha kısa süre ama daha çok yakıt."
        )
        yakıt_orani = st.slider(
            "Yakıt/Kütle oranı (başlangıç)",
            0.5, 0.95, 0.85,
            help="Roketin ilk kütlesinin yakıt yüzdesi. Gerçekçi aralık %85-90."
        )
        sim_hizi = st.slider("Simülasyon hızı", 1, 100, 50, help="Ne kadar hızlı ilerlesin?")

    hedef_hiz = v_escape * hedef_hiz_kat
    delta_v = hedef_hiz - v_leo
    m0_m1 = math.exp(delta_v / ve)
    gerekli_yakıt_orani = 1 - 1 / m0_m1
    if gerekli_yakıt_orani > 0.99:
        gerekli_yakıt_orani = 0.99

    sure_saat = mars_distance / (hedef_hiz * 3600)
    sure_gun = sure_saat / 24

    col1, col2, col3 = st.columns(3)
    col1.metric("Gerekli Δv", f"{delta_v:.2f} km/s")
    col2.metric("Gerekli Yakıt Oranı", f"%{gerekli_yakıt_orani*100:.1f}")
    col3.metric("Tahmini Varış", f"{sure_gun:.1f} gün")

    if gerekli_yakıt_orani > yakıt_orani:
        st.warning("⚠️ Mevcut yakıt bu hıza ulaşmak için yetersiz! Daha düşük hız seçin veya yakıt oranını artırın.")

    if st.button("🚀 TMI MANEVRASINI BAŞLAT", key="tmi_start"):
        if gerekli_yakıt_orani > yakıt_orani:
            st.error("Yakıt yetersiz! Manevra iptal edildi.")
            return

        hiz = v_leo
        yakıt = yakıt_orani
        mesafe = 0
        zaman = 0
        radyasyon = 0.05
        sicaklik = 20

        progress_bar = st.progress(0, text="Manevra başlıyor...")
        status = st.empty()
        col_a, col_b, col_c, col_d = st.columns(4)
        hiz_met = col_a.empty()
        yakit_met = col_b.empty()
        rad_met = col_c.empty()
        temp_met = col_d.empty()
        chart_placeholder = st.empty()

        chart_data = []
        toplam_adim = int(sure_saat) + 1
        for adim in range(toplam_adim):
            ilerleme = adim / toplam_adim
            progress_bar.progress(ilerleme, text=f"Uçuş süresi: {adim} / {toplam_adim:.0f} saat")

            if adim == 0:
                hiz = hedef_hiz
                yakıt -= (delta_v / ve) * 0.1
                if yakıt < 0:
                    yakıt = 0
            else:
                mesafe += hiz * 3600
                if mesafe > mars_distance:
                    mesafe = mars_distance

                radyasyon = 0.05 + 0.15 * (mesafe / mars_distance) - 0.1 * (abs(mesafe - mars_distance/2) / (mars_distance/2))
                if radyasyon < 0.01:
                    radyasyon = 0.01
                sicaklik = 20 - 250 * (mesafe / mars_distance)
                if sicaklik < -50:
                    sicaklik = -50

            hiz_met.metric("Hız (km/s)", f"{hiz:.2f}")
            yakit_met.metric("Yakıt Kütle Oranı", f"%{yakıt*100:.1f}")
            rad_met.metric("Radyasyon (mSv/h)", f"{radyasyon:.3f}")
            temp_met.metric("Sıcaklık (°C)", f"{sicaklik:.1f}")

            chart_data.append({"Zaman (saat)": adim, "Hız (km/s)": hiz, "Radyasyon (mSv/h)": radyasyon*10})
            df = pd.DataFrame(chart_data)
            if len(df) > 1:
                chart_placeholder.line_chart(df.set_index("Zaman (saat)"))

            time.sleep(0.1 * (100 / sim_hizi))

            if mesafe >= mars_distance:
                break

        progress_bar.empty()
        st.balloons()
        st.success(f"✅ Mars'a ulaşıldı! Toplam süre: {adim} saat ({adim/24:.2f} gün)")
        st.info(f"**Son durum:** Hız: {hiz:.2f} km/s, Kalan yakıt: %{yakıt*100:.1f}")

# ============================================
# ANA MENÜ
# ============================================
modul = st.sidebar.radio(
    "Modül Seç",
    [
        "Mars Görev Kontrolü (Derzz vs Starship)",
        "Çekirdek Reaktör",
        "Kahin Modu",
        "Derzz Yarışı",
        "Çernobil Protokolü",
        "Entropi Dönüşümü",
        "FAZZ-9: TMI Manevrası (Gerçekçi)"
    ]
)

if modul == "Mars Görev Kontrolü (Derzz vs Starship)":
    mars_gorev_kontrolu()
elif modul == "Çekirdek Reaktör":
    cekirdek_reaktor()
elif modul == "Kahin Modu":
    kahin_modu()
elif modul == "Derzz Yarışı":
    derzz_yarisi()
elif modul == "Çernobil Protokolü":
    cernobil_protokolu()
elif modul == "Entropi Dönüşümü":
    entropi_donusumu()
elif modul == "FAZZ-9: TMI Manevrası (Gerçekçi)":
    tmi_manevrasi()

st.sidebar.markdown("---")
st.sidebar.write("© 2026 Emrah Uzuçar (Fakir Tony Stark)")
