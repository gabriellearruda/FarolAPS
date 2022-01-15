import streamlit as st


st.markdown("""
    # Atenção Primária à Saúde: O impacto que teríamos em melhorar o sistema de saúde
    
    A Atenção Primária à Saúde (APS) tem sido apontada como essencial para construir sistemas de saúde mais eficientes e equitativos. Em países com sistemas de saúde de forte orientação para APS, observa-se **resultados melhores em termos de mortalidade geral, mortalidade prematura, bem como mortalidade por condições preveníveis e tratáveis** (World Bank, 2017).
    
    Estudos mostram que a **maior continuidade de atendimento por um mesmo profissional** **(longitudinalidade)** **está associada com menor probabilidade de hospitalização** por qualquer condição (Gill & Mainous, 1998).
    
    Relatório do Banco Mundial sobre eficiência do SUS aponta uma correlação positiva entre a eficiência da APS e a da atenção de média e alta complexidade (MAC), a **expansão da APS a 100% resultaria em ganhos de eficiência de pelo menos 0,03% do PIB (World Bank, 2017).**
    
    O Previne Brasil é a nova política de financiamento federal da Atenção Primária à Saúde. Instituído em 2019, o Previne visa fortalecer o Sistema Único de Saúde (SUS) a partir de uma estrutura de financiamento que leve em consideração a dependência da população do SUS e o **desempenho e os resultados dos municípios no cuidado da Atenção Primária**.
    
    Atualmente temos 7 dos 21 indicadores com desempenho municipal sendo acompanhado pelo programa Previne Brasil, correspondendo as ações estratégicas de Saúde da Mulher, Pré-Natal, Saúde da Criança e Doenças Crônicas (Hipertensão Arterial e Diabetes Melittus). Apesar do empenho da importância das ações na atenção primária e do empenho das equipes de saúde, os nossos resultados nos indicadores desenhados tem sido aquém do esperado. Podemos observar esses resultados abaixo através do Indíce Sintético Final (ISF), que é calculado como a média ponderada dos 7 indicadores:
    
    &nbsp;""")

st.write("""
    <iframe title="" aria-label="map" id="datawrapper-chart-6L8ly" src="https://datawrapper.dwcdn.net/6L8ly/1/" scrolling="no" frameborder="0" style="width: 100%; min-width: 100% !important; border: none;" height="650px"></iframe>
    """,
    unsafe_allow_html=True)

st.markdown("""
    Melhorar nossos resultados nos indicadoress de saúde permitiria prevenir casos de cancêr, amputações e reduzir a mortalidade infantil. Nossos desempenho atual é de 26% do atendimento possível, abaixo você pode observar quantas pessoas seriam impactadas se conseguissemos melhorar hoje os indicadores vigentes:
    &nbsp;
    """)

capacidade = st.slider('', 27, 100, 52)
melhoria = round(capacidade/26, 2)
st.write("Com a capacidade do atendimento em ", capacidade, " % teria-se um desempenho ", melhoria, " vezes melhor do que atendimento atual e resultaria em:")

diff = round((capacidade-26)/74*100, 1)

gestantes = f"{int(603858*0.87*diff/100):,}"
st.write(gestantes, " **Gestantes** com melhorias no pré-natal, exames e saude odontologica.")

mulheres = f"{int(39107641*0.87*diff/100):,}"
st.write(mulheres, " **Mulheres** que teriam realização de exame citopatológico, e consequentemente menos incidência de cancêr de útero.")

criancas = f"{int(1325117*0.51*diff/100):,}"
st.write(criancas, " **Crianças** a mais vacinadas com polio ou penta.")

hipertensos = f"{int(30438732*0.94*diff/100):,}"
st.write(hipertensos, " **Hipertensos** com pressão arterial aferida.")

diabeticos = f"{int(8735583*0.87*diff/100):,}"
st.write(diabeticos, " **Diabéticos** teriam a medição de hemoglobina glicada realizada, diminuindo as amputações por diabétes que hoje é responsável por 70% das amputações dos membros inferiores.")

st.write("""
    &nbsp;

    Você pode obter mais informações sobre o programa e como melhorar os indicadores <a href="https://impulsoprevine.org/">aqui</a>. 
    &nbsp;
    """,
    unsafe_allow_html=True)


# streamlit run inicio.py --theme.primaryColor "#34758A"
