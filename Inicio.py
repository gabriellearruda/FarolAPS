import imp
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd


st.markdown("""
    ### Selecione  """)
competencias_notas = pd.read_csv("competencias_notas.csv")
iniciativas = pd.read_csv('https://docs.google.com/spreadsheets/d/' + '196uk3iKUF5g1bsjsinwsZ5RY91-7zGk_llSakfGApls' + '/export?gid=253431840&format=csv', index_col=0)
municipio = st.selectbox('', competencias_notas['Município'].unique())
competencias_unicas_aderidas = f"{competencias_notas[(competencias_notas['Município'] == municipio) & (competencias_notas['Pactuado?'] == 'Sim')]['Competência'].nunique():,}"
iniciativas_unicas_aderidas = f"{len(iniciativas[(iniciativas['Município'] == municipio) & (iniciativas['Status Geral'] == '3 - Concluída')]):,}"
competencias_notas = competencias_notas[(competencias_notas['Município'] == municipio)]
competencias_notas = competencias_notas[['Município', 'Temática', 'Baseline Temática Nota', 'Baseline Temática Classificação']]
st.write("""
     """)
text = "Seu municipio aderiu a " + competencias_unicas_aderidas + " competências e já realizou " + iniciativas_unicas_aderidas + " iniciativas para melhora-las."
st.markdown(text)
st.markdown("""

    ## """)
competencias_notas = competencias_notas.drop_duplicates(subset=['Município', 'Temática', 'Baseline Temática Nota'])
for i in competencias_notas.index.tolist():
    str = competencias_notas.loc[i]['Temática'] + ' - ' + competencias_notas.loc[i]['Baseline Temática Classificação'][4:]
    if competencias_notas.loc[i]['Baseline Temática Classificação'][0:1] == '1':
        st.error(str)
    if competencias_notas.loc[i]['Baseline Temática Classificação'][0:1] == '2':
        st.warning(str)
    if competencias_notas.loc[i]['Baseline Temática Classificação'][0:1] == '3':
        st.success(str)
    if competencias_notas.loc[i]['Baseline Temática Classificação'][0:1] == '4':
        st.info(str)



# with st.expander("annotated_text"):
#      st.write("""
#          The chart above shows some numbers I picked for you.
#          I rolled actual dice for these, so they're *guaranteed* to
#          be random.
#      """)

# streamlit run inicio.py --theme.primaryColor "#34758A"
