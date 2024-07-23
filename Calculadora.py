import streamlit as st

def main():
    st.title("Calculadora Horário MGF")

    st.write("Cálculo da distribuição do tempo de trabalho dos médicos de família dependendo das características da lista.")
    
    if st.session_state.get("n_crianças_1_ano") is None:
        st.session_state["n_crianças_1_ano"] = 20
    if st.session_state.get("tempo_consulta_crianças_1_ano") is None:
        st.session_state["tempo_consulta_crianças_1_ano"] = 30
    if st.session_state.get("n_consultas_crianças_1_ano") is None:
        st.session_state["n_consultas_crianças_1_ano"] = 6
    
    
    st.subheader("Crianças < 1 ano")
    col_crianças_1_ano_1, col_crianças_1_ano_2, n_crianças_1_ano_3 = st.columns(3, vertical_alignment="bottom")

    with col_crianças_1_ano_1:
        st.session_state["n_crianças_1_ano"] = st.number_input(
            "Número de crianças < 1 ano",
            step=1,
            value=20
            )
    with col_crianças_1_ano_2:
        st.session_state["tempo_consulta_crianças_1_ano"] = st.number_input(
            "Tempo por consulta crinaças < 1 ano",
            step=5,
            value=30
            )
        
    with n_crianças_1_ano_3:
        st.session_state["n_consultas_crianças_1_ano"] = st.number_input(
            "Número de consultas a crianças com menos de 1 ano por ano",
            step=1,
            value=6
            )

    st.subheader("Crianças entre 1 e 2 anos")

    col_crianças_2_ano_1, col_crianças_2_ano_2, n_crianças_2_ano_3 = st.columns(3, vertical_alignment="bottom")

    with col_crianças_2_ano_1:
        st.session_state["n_crianças_1_ano"] = st.number_input(
            "Número de crianças entre 1 e 2 anos",
            step=1,
            value=20
            )
    with col_crianças_2_ano_2:
        st.session_state["tempo_consulta_crianças_1_ano"] = st.number_input(
            "Tempo por consulta crinaças entre 1 e 2 anos",
            step=5,
            value=30
            )
        
    with n_crianças_2_ano_3:
        st.session_state["n_consultas_crianças_1_ano"] = st.number_input(
            "Número de consultas a crianças entre 1 e 2 anos por ano",
            step=1,
            value=6
            )

    st.subheader("Crianças e jovens (2-18 anos)")
    
    col_crianças_jovens_1, col_crianças_jovens_2, col_crianças_jovens_3 = st.columns(3, vertical_alignment="bottom")

    with col_crianças_jovens_1:
        st.session_state["n_crianças_2_18_anos"] = st.number_input(
            "Número de crianças entre 2 e 18 anos",
            step=1,
            value=20
            )
    with col_crianças_jovens_2:
        st.session_state["tempo_crianças_2_18_anos"] = st.number_input(
            "Tempo por consulta crinaças entre 2 e 18 anos",
            step=5,
            value=30
            )
        
    with col_crianças_jovens_3:
        st.session_state["n_consultas_crianças_2_18_anos"] = st.number_input(
            "Número de consultas a crianças entre 2 e 18 anos por ano",
            step=1,
            value=6
            )
    
    st.divider()
    
    st.subheader("Mulheres em idade fértil")
    
    col_mulheres_idade_fertil_1, col_mulheres_idade_fertil_2, col_mulheres_idade_fertil_3 = st.columns(3, vertical_alignment="bottom")
    
    with col_mulheres_idade_fertil_1:
        st.session_state["n_mulheres_idade_fertil"] = st.number_input(
            "Número de mulheres em idade fértil (15-54 anos)",
            step=1
            )
    with col_mulheres_idade_fertil_2:
        st.session_state["taxa_utilização"] = st.number_input(
            "Taxa de utilização de consultas",
            step=1
            )
    
    with col_mulheres_idade_fertil_3:
        st.session_state["tempo_consulta_mulheres_idade_fertil"] = st.number_input(
            "Tempo por consulta",
            step=5,
            value=30
            )
    
    
    st.divider()
    
    st.subheader("Grávidas")
    
    col_gravidas_1, col_gravidas_2, col_gravidas_3 = st.columns(3, vertical_alignment="bottom")
    with col_gravidas_1:
        st.session_state["n_nascimentos_ano_anterior"] = st.number_input(
            "Número de nascimentos no ano anterior",
            step=1
            )
    with col_gravidas_2:
        st.session_state["tempo_consulta_gravidas"] = st.number_input(
            "Tempo por consulta gravida",
            step=5,
            value=30
            )
    with col_gravidas_3:
        st.session_state["n_consultas_gravidas"] = st.number_input(
            "Número de consultas por ano",
            step=1,
            value=7
            )


    st.divider()
    
    st.subheader("Diabéticos")
    
    col_diabeticos_1, col_diabeticos_2, col_diabeticos_3 = st.columns(3, vertical_alignment="bottom")
    
    with col_diabeticos_1:
        st.session_state["n_diabeticos"] = st.number_input(
            "Número de diabéticos",
            step=1,
            value=100
            )
    with col_diabeticos_2:
        st.session_state["tempo_diabeticos"] = st.number_input(
            "Tempo por consulta diabéticos",
            step=5,
            value=30
            )
    with col_diabeticos_3:
        st.session_state["n_consultas_diabeticos"] = st.number_input(
            "Número de consultas por ano",
            step=1,
            value=2
            )
        

    st.divider()

    st.session_state["n_horas_base"] = st.slider(
        "Número de horas base",
        0,
        60,
        40
        )
    
    st.session_state["n_horas_nao_assistencial"] = st.slider(
        "Número de horas não assistencial",
        0, 40, 4
    )
    
    st.session_state["p_doneça_aguda"] = st.slider(
        "Percentagem de doença aguda",
        0,
        100,
        30
        )
    
    
st.sidebar.title("Horario")



if __name__ == "__main__":
    main()
