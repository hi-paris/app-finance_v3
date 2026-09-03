# app_exec_irina.py (ou remplace app.py)
import streamlit as st
from PIL import Image

# 👉 on importe les versions "exec" que tu as créées
from labs.lab1_exec_irina import lab1_code
from labs.lab2_exec_irina import lab2_code

st.set_page_config(
    page_title="Finance (Executive Education)",
    layout="wide",
    page_icon="./images/flask.png"
)

# Logos
image_hec = Image.open('images/hec.png')
image_hiparis = Image.open('images/hi-paris.png')

##################################################################################
############################# SIDEBAR (ÉPURÉE) ###################################
##################################################################################

st.sidebar.header("**Dashboard**")
st.sidebar.markdown("  ")

# ✅ On garde UNIQUEMENT le choix d'exercice dans l'app principale
lab_numbers = st.sidebar.selectbox('Select the exercise ➡️', [
    '01 - One risky and one risk-free asset',
    '02 - Two risky assets'
])

# ❌ PAS de section code
# ❌ PAS d'IDs étudiants
# ❌ PAS de boutons Submit / note (gérés & masqués dans les labs avec simple_mode=True)

##################################################################################
############################# EN-TÊTE MAIN PANEL ################################
##################################################################################

st.image(image_hec, width=300)
st.title("HEC Paris - Finance Labs (Executive Education)")
st.subheader("Portfolio theory 📈")
st.markdown("##### **Course provided by Irina Zviadadze**")

st.markdown("Made with the help of the **[Hi! PARIS Engineering Team](https://www.hi-paris.fr/)**")
st.image(image_hiparis, width=150)

st.markdown("  ")
st.markdown("---")

##################################################################################
############################# CONTENU DES EXERCICES ##############################
##################################################################################

select_teacher = "Irina Zviadadze"

if lab_numbers == "01 - One risky and one risk-free asset":
    # simple_mode=True => pas d'upload, pas de submit, pas de note, etc.
    lab1_code(select_teacher, None, None, simple_mode=True)
else:
    lab2_code(select_teacher, None, None, simple_mode=True)
