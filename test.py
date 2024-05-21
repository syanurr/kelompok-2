import streamlit as st
from PIL import Image
import math

def MyBG_colour(wch_colour): 
    my_colour = f"<style> .stApp {{background-color: {wch_colour};}} </style>"
    st.markdown(my_colour, unsafe_allow_html=True)

MyBG_colour("#FDD7D7") 

st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #A4BDF9;
    }
</style>
""", unsafe_allow_html=True)
with st.sidebar:
    "## "

def halaman_utama():
    st.header(":blue[APLIKASI KALKULATOR STANDARDISASI TITRIMETRI]", divider="rainbow")
    st.title("_LPK_ is :rainbow[cool] :sunglasses:")
    st.image("foto5.jpeg")
    
    st.write("Halo gaiss!!! selamat datang di kalkulator standardisasi titrimetri 👩🏻‍🔬⚗️🧪")
    st.write("Aplikasi ini dapat digunakan untuk menentukan nilai % RSD dengan menginput rata-rata normalitas dan nilai standar deviasi yang dilengkapi dengan perhitungan normalitas, rata-rata normalitas dan standar deviasi🤩🧪⚛️")

    st.write(":fire::fire::fire: KELOMPOK 2 :fire::fire::fire:")
    st.write(':blue[Dea Seinthia Safani (2360096)]')
    st.write(':violet[Marsya Nurmala Fitriani (2360169)]')
    st.write(':green[Muhammad Ghema Putra (2360185)]')
    st.write(':orange[Valerin Dianaocta Ifada (2360283)]')
    st.write(':red[Vienita Dian Maulidie (2360285)]')

def informasi():
    st.write('**PENGERTIAN**')
    st.write("Normalitas adalah ukuran yang menunjukkan besaran konsentrasi pada berat ekuivalen setara dalam gram per larutan. Normalitas juga dapat didefinisikan sebagai jumlah mol ekuivalen dari suatu zat perliter larutan. biasanya kita menghitung normalitas menggunakan rumus pengenceran larutan, maka rumus normalitas yang digunakan adalah: N1.V1=N2.V2.")
    st.write("Standar deviasi adalah ukuran statistik yang menunjukkan seberapa tersebar atau bervariasi suatu kumpulan data dari nilai rata-ratanya. Semakin besar nilai standar deviasi, maka semakin besar pula penyebaran atau variasi data. Sebaliknya, semakin kecil nilai standar deviasi, maka semakin kecil pula penyebaran atau variasi data.")
    st.write(" %RSD adalah nilai absolut dari koefisien variasi. Hal ini sering dinyatakan sebagai persentase. Sebuah istilah serupa yang kadang-kadang digunakan adalah varians relatif yang merupakan kuadrat dari koefisien variasi. Standar deviasi relatif banyak digunakan dalam kimia analitik untuk menyatakan presisi.")
    st.write("**INFORMASI BOBOT EKIVALEN**")
    st.write("Bobot Ekivalen H₂C₂O₄.2H₂O(Asam Oksalat) = 63 mg/mgrek")
    st.write("Bobot Ekivalen Na₂B₄O₇.10H₂O(Boraks) = 191 mg/mgrek")
    st.write("Bobot Ekivalen K₂Cr₂O₇(Kalium Dikromat) = 49 mg/mgrek")
    st.write("Bobot Ekivalen CaCO₃(Kalsium Karbonat) = 100 mg/mgrek")

def normalitas():
    st.write("KALKULATOR PERHITUNGAN NORMALITAS")
    massa=st.number_input("Masukkan massa (mg)", min_value=0.0000)
    st.write("Massa sebesar",massa,step=0.0001)
    Bobot_Ekivalen=st.number_input("Masukkan nilai Bobot Ekivalen (mg/mgrek)", min_value=0.0000)
    st.write("Bobot ekivalen sebesar",Bobot_Ekivalen,step=0.0001)
    volume=st.number_input("Masukkan Volume larutan (mL)", min_value=0.0000)
    st.write("Volume sebesar",volume,step=0.0001)
    faktor_pengali=st.number_input("Masukkan nilai FP", min_value=0.0000)
    st.write("Faktor Pengali sebesar",faktor_pengali,step=0.0001)
    if st.button("hitung normalitas"):
        normalitas=massa / (Bobot_Ekivalen*volume*faktor_pengali)
        st.write(f"normalitas sebesar = {normalitas} mgrek/mL")
        st.balloons()

def rataratanormalitas():
    st.write("KALKULATOR PERHITUNGAN RATA-RATA NORMALITAS")
    st.write("📌📌Penginputan desimal pada data normalitas menggunakan tanda baca titik📌📌")
    data_input = []
    num_columns = st.number_input("Jumlah Kolom Input Data", min_value=1, max_value=10, value=1)

    for i in range(num_columns):
        input_data = st.text_input(f"Masukkan Normalitas {i+1}")
        if input_data:
            data_input.append([float(x.strip()) for x in input_data.split(',') if x.strip()])

    merged_data = [item for sublist in data_input for item in sublist]
    def page_ratarata(data):
        try:
            rata_rata = sum(data) / len(data)
            return rata_rata
        except:
            return "Masukkan semua hasil konsentrasi" 
    if merged_data:
        hasil_ratarata = page_ratarata(merged_data)
    if st.button("hitung rata-rata normalitas"):
        st.write(f"rata-rata normalitas sebesar = {hasil_ratarata} N")
        st.balloons()

def standardeviasi():
    st.write('KALKULATOR PERHITUNGAN STANDAR DEVIASI (SD)')
    st.write('📌📌Penginputan desimal pada data normalitas menggunakan tanda baca titik📌📌')
    data_input = []
    num_columns = st.number_input("Jumlah Kolom Input Data", min_value=1, max_value=10, value=1)

    for i in range(num_columns):
        input_data = st.text_input(f"Masukkan Normalitas {i+1}")
        if input_data:
            data_input.append([float(x.strip()) for x in input_data.split(',') if x.strip()])

    merged_data = [item for sublist in data_input for item in sublist]
    def page_standar_deviasi_calc(data):
        try:
            rata_rata = sum(data) / len(data)
            selisih_kuadrat = sum((x - rata_rata) ** 2 for x in data)
            standar_deviasi = math.sqrt((selisih_kuadrat) / (len(data) - 1))
            return standar_deviasi
        except:
            return "Masukkan semua hasil konsentrasi" 
    if merged_data:
        hasil_standar_deviasi = page_standar_deviasi_calc(merged_data)
    if st.button("Hitung Standar Deviasi"):
        st.write(f"Standar Deviasi sebesar = {hasil_standar_deviasi} N")
        st.balloons()



def RSD():
    st.write("KALKULATOR PERHITUNGAN % RSD")
    sd= st.number_input("Masukkan nilai standar deviasi",step=0.0001)
    st.write("standar deviasi adalah",sd,step=0.0001)
    rt=st.number_input("masukkan nilai rata-rata normalitas",step=0.0001)
    st.write("rata-rata normalitas adalah",rt,step=0.0001)
    if st.button("hitung % RSD"):
        RSD=(sd/rt)*100
        st.write(f"Nilai %RSD adalah = {RSD} %")
        st.balloons()
    

menu_options=["HALAMAN UTAMA","PENGERTIAN","KALKULATOR NORMALITAS","KALKULATOR RATA-RATA NORMALITAS","KALKULATOR STANDAR DEVIASI (SD)","KALKULATOR % RSD"]
selected_menu=st.sidebar.radio("**Options**",menu_options)

if selected_menu=="HALAMAN UTAMA":
   page_bg_img="""
   <style>
   </style>
   """
   st.markdown(page_bg_img,unsafe_allow_html=True)
   halaman_utama()
elif selected_menu=="PENGERTIAN":
    informasi()
elif selected_menu=="KALKULATOR NORMALITAS":
    normalitas()
elif selected_menu=="KALKULATOR RATA-RATA NORMALITAS":
    rataratanormalitas()
elif selected_menu=="KALKULATOR STANDAR DEVIASI (SD)":
    standardeviasi()
elif selected_menu=="KALKULATOR % RSD":
    RSD()



