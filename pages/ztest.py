import streamlit as st #import = ambil semua bagian 
import pandas as pd
from statistics import NormalDist #from = ambil satu bagian dari statistik
from statsmodels.stats.weightstats import ztest #ada statsmodels ada stats ada weightstats ada ztest
from scipy.stats import shapiro #google shapiro wik test python



st.title('ZTEST')

with st.expander('view data'):
    df= pd.read_csv('https://raw.githubusercontent.com/ethanweed/pythonbook/main/Data/zeppo.csv') #pd untuk baca data internet ke laptop
    st.dataframe(df.transpose()) #df untuk nampilkan data ke web #transpose biar kesamping

with st.expander('view statistics'):
    st.dataframe(df.describe().transpose())

st.write('## Constructing') #write buat sub judul, semakin banyak tanda pagar (#) semakin kecil fontnya
st.latex('H_{0}: \mu=\mu_{0}') #latex untuk menuliskan fungsi otomatis
st.latex('H_{1}: \mu \neq \mu_{0}') #ne adalah non equal (tidak sama dengan)

alpha = st.number_input('masukkan nilai alpha', step=0.001, min_value = 0., max_value=1.)
null_mean = st.number_input('masukkan nilai mu_0', step=0.001)

clicked = st.button('do the Z test !!')

if clicked:
    alpha_z = NormalDist().inv_cdf(p=1-alpha/2) #uji dua sisi
    z_score, p_value = ztest(df['grades'], value=null_mean, alternative='two-sided')
    if abs(z_score) > alpha_z:
        st.latex('REJECT H0')
    else:
        st.latex('CAN NOT REJECT H0')
    st.write(f'titik kritis = {alpha_z}, hitung z = {z_score}, p value = {p_value}') #karena ambil nilai jadi pake f
#DEBUG untuk cek salah/error


#Buat check shapiro
st.write('## CHECK NORMALITY')
clicked_2 = st.button('do the shapiro test')
if clicked_2:
    result = shapiro(df['grades'])
    st.write(result)
    st.bar_chart(df['grades'])

