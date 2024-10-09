import streamlit as st

st.set_page_config(page_title='Compteur', layout='wide')

st.title('Page du Compteur')

if 'compteur' not in st.session_state:
    st.session_state.compteur = 0

increment = st.number_input('Valeur à ajouter', min_value=1, value=1)

if st.button('Incrémenter'):
    st.session_state.compteur += increment
    st.success(f'Compteur incrémenté de {increment}.')

st.write('Valeur actuelle du compteur : ', st.session_state.compteur)