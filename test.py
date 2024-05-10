import streamlit as st
from PIL import Image
import base64

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
    st.write("Aplikasi ini dapat digunakan untuk menentukan nilai % RSD dengan menginput rata rata normalitas dan nilai standar deviasi yang dilengkapi dengan perhitungan normalitas, rata-rata normalitas dan standar deviasi🤩🧪⚛️")

    st.write(":fire::fire::fire: KELOMPOK 2 :fire::fire::fire:")
    st.write(':blue[Dea Seinthia Safani (2360096)]')
    st.write(':violet[Marsya Nurmala Fitriani (2360169)]')
    st.write(':green[Muhammad Ghema Putra (2360185)]')
    st.write(':orange[Valerin Dianaocta Ifada (2360283)]')
    st.write(':red[Vienita Dian Maulidie (2360285)]')

def informasi():
    st.write('**INFORMASI**')
    st.write("Normalitas adalah ukuran yang menunjukkan besaran konsentrasi pada berat ekuivalen setara dalam gram per larutan. Normalitas juga dapat didefinisikan sebagai jumlah mol ekuivalen dari suatu zat perliter larutan. biasanya kita menghitung normalitas menggunakan rumus pengenceran larutan, maka rumus normalitas yang digunakan adalah: N1.V1=N2.V2.")
    st.write("Standar deviasi adalah ukuran statistik yang menunjukkan seberapa tersebar atau bervariasi suatu kumpulan data dari nilai rata-ratanya. Semakin besar nilai standar deviasi, maka semakin besar pula penyebaran atau variasi data. Sebaliknya, semakin kecil nilai standar deviasi, maka semakin kecil pula penyebaran atau variasi data.")
    st.write(" %RSD adalah nilai absolut dari koefisien variasi. Hal ini sering dinyatakan sebagai persentase. Sebuah istilah serupa yang kadang-kadang digunakan adalah varians relatif yang merupakan kuadrat dari koefisien variasi. Standar deviasi relatif banyak digunakan dalam kimia analitik untuk mengekspresikan presisi.")
    st.write("**INFORMASI BOBOT EKIVALEN**")
    st.write("Bobot Ekivalen H₂C₂O₄.2H₂O(Asam Oksalat)=63 mg/mgrek")
    st.write("Bobot Ekivalen Na₂B₄O₇.10H₂O(Boraks)=191 mg/mgrek")
    st.write("Bobot Ekivalen K₂Cr₂O₇(Kalium Dikromat)=49 mg/mgrek")
    st.write("Bobot Ekivalen CaCO₃(Kalsium Karbonat)=100 mg/mgrek")

def normalitas():
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
    n1=st.number_input("Masukkan nilai normalitas pertama", min_value=0.0000)
    st.write("normalitas pertama adalah",n1,step=0.0001)
    n2=st.number_input("Masukkan nilai normalitas kedua", min_value=0.0000)
    st.write("normalitas kedua adalah",n2,step=0.0001)
    n3=st.number_input("Masukkan nilai normalitas ketiga", min_value=0.0000)
    st.write("normalitas ketiga adalah",n3,step=0.0001)
    if st.button("hitung rata-rata normalitas"):
        rata2=(n1+n2+n3)/3
        st.write(f"rata-rata normalitas sebesar = {rata2} N")
        st.balloons()

def standardeviasi():
    sd1=st.number_input("Masukkan normalitas pertama",step=0.0001)
    st.write("normalitas pertama adalah",sd1,step=0.0001)
    sd2=st.number_input("masukkan normalitas kedua",step=0.0001)
    st.write("normalitas kedua adalah",sd2,step=0.0001)
    sd3=st.number_input('Masukkan normalitas ketiga',step=0.0001)
    st.write('normalitas ketiga adalah', sd3,step=0.0001)
    sd4=st.number_input("masukkan normalitas rata-rata",step=0.0001)
    st.write("normalitas rata-rata adalah",sd4,step=0.0001)
    if st.button("hitung standar deviasi"):
        p1=(sd1-sd4)**2
        p2=(sd2-sd4)**2
        p3=(sd3-sd4)**2
        p4=((p1+p2+p3)/2)**0.5
        st.write(f"Nilai Standar Deviasi adalah = {p4} N")
        st.balloons()

def RSD():
    sd= st.number_input("Masukkan nilai standar deviasi",step=0.0001)
    st.write("standar deviasi adalah",sd,step=0.0001)
    rt=st.number_input("masukkan nilai rata-rata normalitas",step=0.0001)
    st.write("rata-rata normalitas adalah",rt,step=0.0001)
    if st.button("hitung % RSD"):
        RSD=(sd/rt)*100
        st.write(f"Nilai %RSD adalah = {RSD} %")
        st.balloons()
    

menu_options=["HALAMAN UTAMA","INFORMASI","NORMALITAS","RATA-RATA NORMALITAS","STANDAR DEVIASI (SD)","% RSD"]
selected_menu=st.sidebar.radio("**Options**",menu_options)

if selected_menu=="HALAMAN UTAMA":
   page_bg_img="""
   <style>
   </style>
   """
   st.markdown(page_bg_img,unsafe_allow_html=True)
   halaman_utama()
elif selected_menu=="INFORMASI":
    informasi()
elif selected_menu=="NORMALITAS":
    normalitas()
elif selected_menu=="RATA-RATA NORMALITAS":
    rataratanormalitas()
elif selected_menu=="STANDAR DEVIASI (SD)":
    standardeviasi()
elif selected_menu=="% RSD":
    RSD()



