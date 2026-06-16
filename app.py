import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="MindScroll",
    layout="centered"
)


st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#e0e7ff,#dbeafe,#fce7f3);
}

.card{
background:white;
padding:25px;
border-radius:25px;
box-shadow:0 10px 30px rgba(0,0,0,.15);
margin-bottom:20px;
}

.logo{
width:100px;
height:100px;
background:linear-gradient(135deg,#2563eb,#9333ea);
border-radius:50%;
display:flex;
align-items:center;
justify-content:center;
margin:auto;
font-size:50px;
font-weight:bold;
color:white;
}

.title{
text-align:center;
font-size:45px;
font-weight:900;
background:linear-gradient(90deg,#2563eb,#9333ea);
-webkit-background-clip:text;
color:transparent;
}

.section{
background:linear-gradient(90deg,#2563eb,#9333ea);
padding:15px;
border-radius:15px;
color:white;
font-size:22px;
font-weight:bold;
}

.stButton button{
width:100%;
height:50px;
border-radius:25px;
background:linear-gradient(90deg,#2563eb,#9333ea);
color:white;
font-weight:bold;
}

</style>
""",unsafe_allow_html=True)



st.markdown("""
<div class="card">

<div class="logo">M</div>

<div class="title">
MINDSCROLL
</div>

<p style="text-align:center">
Digital Behavior Analysis
</p>

</div>
""",unsafe_allow_html=True)



st.markdown("""
<div class="card">

MindScroll membantu kamu memahami kebiasaan penggunaan media sosial,
tingkat kontrol diri digital,
pengaruh terhadap emosi,
dan dampaknya terhadap aktivitas sehari-hari.

</div>
""",unsafe_allow_html=True)



nama = st.text_input(
"Masukkan nama kamu"
)



st.markdown("""
<div class="section">
Evaluasi Kebiasaan Digital Kamu
</div>
""",unsafe_allow_html=True)



durasi = st.selectbox(
"Berapa lama kamu menggunakan media sosial dalam sehari?",
[
"Kurang dari 1 jam",
"1 - 3 jam",
"3 - 5 jam",
"5 - 8 jam",
"Lebih dari 8 jam"
]
)



pertanyaan=[

"Seberapa sering kamu membuka media sosial tanpa tujuan yang jelas?",

"Apakah kamu sering melewati waktu yang sudah kamu rencanakan ketika scrolling?",

"Apakah kamu merasa sulit berhenti walaupun sadar sudah terlalu lama menggunakan media sosial?",

"Bagaimana perasaan kamu ketika tidak membuka media sosial?",

"Apakah media sosial pernah membuat kamu menunda kegiatan penting?",

"Apakah kamu menggunakan media sosial ketika sedang stres, bosan, atau ingin menghindari masalah?",

"Apakah komentar, jumlah suka, atau perhatian di media sosial memengaruhi perasaan kamu?",

"Apakah waktu kamu lebih banyak habis di media sosial dibanding melakukan hal yang sebenarnya ingin kamu lakukan?",

"Apakah kamu sulit menikmati waktu luang tanpa membuka media sosial?"

]



jawaban=[]


for p in pertanyaan:

    jawaban.append(
        st.selectbox(
            p,
            [
            "Tidak pernah",
            "Jarang",
            "Kadang",
            "Sering",
            "Sangat sering"
            ]
        )
    )



if st.button("Mulai Analisis"):


    if nama.strip()=="":
        nama="Kamu"


    skor=0



    if durasi=="Kurang dari 1 jam":
        skor+=1

    elif durasi=="1 - 3 jam":
        skor+=2

    elif durasi=="3 - 5 jam":
        skor+=3

    else:
        skor+=4



    for j in jawaban:

        if j=="Tidak pernah":
            skor+=1

        elif j=="Jarang":
            skor+=2

        elif j=="Kadang":
            skor+=3

        else:
            skor+=4

    # menentukan indikator
    if skor <= 15:
        status = "Aman"
    elif skor <= 28:
        status = "Perlu Perhatian"
    else:
        status = "Buruk"


    # simpan ke excel
    data_baru = pd.DataFrame({
        "Nama": [nama],
        "Link": ["Form MindScroll"],
        "Indikator": [status]
    })


    file="hasil_mindscroll.xlsx"


    if os.path.exists(file):
        data_lama = pd.read_excel(file)
        data_akhir = pd.concat([data_lama, data_baru], ignore_index=True)
    else:
        data_akhir = data_baru


    data_akhir.to_excel(file, index=False)


    st.markdown(f"""

<div class="card">

<h2>📊 Grafik Analisis Kebiasaan Digital {nama}</h2>

<p>
Grafik ini menggambarkan pola penggunaan media sosial
berdasarkan durasi penggunaan, kontrol diri,
pengaruh aktivitas, dan kondisi emosional.
</p>

</div>

""",unsafe_allow_html=True)



    grafik=pd.DataFrame({

    "Aspek":[
    "Penggunaan",
    "Kontrol Diri",
    "Aktivitas",
    "Emosi"
    ],


    "Nilai":[

    skor,
    40-skor,
    int(skor*0.8),
    int(skor*0.7)

    ]

    })



    st.bar_chart(
        grafik.set_index("Aspek")
    )



    st.write(f"""

# interpretasi Grafik berdasarkan data pengguna {nama}


Berdasarkan hasil grafik,
kebiasaan digital {nama} terlihat dari beberapa aspek penting.


Penggunaan media sosial tidak hanya dinilai dari lama waktu memakai aplikasi,
tetapi juga bagaimana media sosial memengaruhi:

• kemampuan mengontrol diri

• fokus terhadap aktivitas utama

• kebiasaan membuka aplikasi

• kondisi emosional


Semakin tinggi pengaruh penggunaan,
semakin penting bagi {nama} untuk memperhatikan keseimbangan digital.


""")




    if skor <=15:


        st.success(
        f"Penggunaan Media Sosial {nama} Masih Terkontrol"
        )


        st.write(f"""

## Analisis Mendalam berdasarkan data pengguna {nama}


Berdasarkan jawaban kamu,
terlihat bahwa hubungan {nama} dengan media sosial masih cukup sehat.


Kamu masih mampu mengatur waktu,
menentukan prioritas,
dan menggunakan media sosial tanpa mengganggu kehidupan nyata.


Media sosial lebih menjadi alat komunikasi,
hiburan,
dan informasi.


Saran untuk {nama}:

Pertahankan kebiasaan ini.
Tetap gunakan media sosial secara sadar
dan hindari membuka aplikasi tanpa tujuan.

""")



    elif skor <=28:


        st.warning(
        f"Penggunaan Media Sosial {nama} Mulai Perlu Perhatian"
        )


        st.write(f"""

## Analisis Mendalam {nama}


Hasil menunjukkan bahwa media sosial mulai memberikan pengaruh
terhadap kebiasaan sehari-hari {nama}.


Kemungkinan kamu mulai membuka media sosial
karena kebiasaan,
bukan hanya kebutuhan.


Dampak yang mungkin muncul:

• waktu produktif berkurang

• fokus mudah terganggu

• sulit membatasi penggunaan


Saran untuk {nama}:

Mulai atur batas waktu,
kurangi scrolling tanpa tujuan,
dan berikan waktu untuk aktivitas lain.

""")



    else:


        st.error(
        f"Penggunaan Media Sosial {nama} Menunjukkan Risiko Tinggi"
        )


        st.write(f"""

## Analisis Mendalam {nama}


Berdasarkan hasil evaluasi,
terlihat bahwa penggunaan media sosial {nama}
mulai sulit dikendalikan.


Media sosial dapat memengaruhi waktu,
fokus,
produktivitas,
dan kondisi emosional.


Tanda yang terlihat:

• sulit berhenti scrolling

• membuka aplikasi berulang kali

• menggunakan media sosial saat stres

• terlalu bergantung pada aktivitas digital


Langkah perubahan untuk {nama}:

Mulai kurangi durasi penggunaan,
buat waktu tanpa media sosial,
dan lakukan aktivitas lain.


Tujuannya bukan meninggalkan media sosial,
tetapi membuat {nama} kembali mengendalikan teknologi.

""")


st.caption(
"MindScroll | Digital Behavior Analysis"
)


st.markdown("""
<div class="section">
Data Hasil Pengguna
</div>
""", unsafe_allow_html=True)


if st.button("analisis hasil pengguna"):

    data = pd.read_excel("hasil_mindscroll.xlsx")

    st.dataframe(data) 

    