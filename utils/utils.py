import streamlit as st


def valores_iniciais():
    return {
        "radio_horas_consultas": "Horas",
        "n_horas_base": 40,
        "n_semanas_trabalho_anual": 44,
        "n_horas_nao_assistencial": 4,
        "p_doneça_aguda": 30,
        "tempo_consulta_doença_aguda": 15,
        "tempo_consulta_crianças_1_ano": 30,
        "n_crianças_1_ano": 15,
        "n_consultas_crianças_1_ano": 6,
        "n_crianças_1_2_anos": 20,
        "tempo_consulta_crianças_1_2_anos": 30,
        "n_consultas_crianças_1_2_anos": 3,
        "n_crianças_2_18_anos": 40,
        "tempo_consulta_crianças_2_18_anos": 30,
        "taxa_utilização_crianças_2_18_anos": 50,
        "n_mulheres_idade_fertil": 200,
        "tempo_consulta_mulheres_idade_fertil": 20,
        "taxa_utilização_mulheres_idade_fertil": 50,
        "n_nascimentos_ano_anterior": 10,
        "tempo_consulta_gravidas": 30,
        "n_consultas_gravidas": 7,
        "n_diabeticos": 150,
        "tempo_consulta_diabeticos": 30,
        "n_consultas_diabeticos": 2,
    }


@st.cache_data
def initial_values():
    if "radio_horas_consultas" not in st.session_state:
        st.session_state["radio_horas_consultas"] = "Horas"

    if "n_crianças_1_ano" not in st.session_state:
        st.session_state["n_crianças_1_ano"] = 15
    if "tempo_consulta_crianças_1_ano" not in st.session_state:
        st.session_state["tempo_consulta_crianças_1_ano"] = 30
    if "n_consultas_crianças_1_ano" not in st.session_state:
        st.session_state["n_consultas_crianças_1_ano"] = 6

    if "n_crianças_1_2_anos" not in st.session_state:
        st.session_state["n_crianças_1_2_anos"] = 17
    if "tempo_consulta_crianças_1_2_anos" not in st.session_state:
        st.session_state["tempo_consulta_crianças_1_2_anos"] = 30
    if "n_consultas_crianças_1_2_anos" not in st.session_state:
        st.session_state["n_consultas_crianças_1_2_anos"] = 5

    if "n_crianças_2_18_anos" not in st.session_state:
        st.session_state["n_crianças_2_18_anos"] = 40
    if "tempo_consulta_crianças_2_18_anos" not in st.session_state:
        st.session_state["tempo_consulta_crianças_2_18_anos"] = 30
    if "n_consultas_crianças_2_18_anos" not in st.session_state:
        st.session_state["taxa_utilização_crianças_2_18_anos"] = 50

    if "n_mulheres_idade_fertil" not in st.session_state:
        st.session_state["n_mulheres_idade_fertil"] = 200
    if "taxa_utilização_mulheres_idade_fertil" not in st.session_state:
        st.session_state["taxa_utilização_mulheres_idade_fertil"] = 50
    if "tempo_consulta_mulheres_idade_fertil" not in st.session_state:
        st.session_state["tempo_consulta_mulheres_idade_fertil"] = 20

    if "n_nascimentos_ano_anterior" not in st.session_state:
        st.session_state["n_nascimentos_ano_anterior"] = 5
    if "tempo_consulta_gravidas" not in st.session_state:
        st.session_state["tempo_consulta_gravidas"] = 30
    if "n_consultas_gravidas" not in st.session_state:
        st.session_state["n_consultas_gravidas"] = 7

    if "n_diabeticos" not in st.session_state:
        st.session_state["n_diabeticos"] = 100
    if "tempo_consulta_diabeticos" not in st.session_state:
        st.session_state["tempo_consulta_diabeticos"] = 30
    if "n_consultas_diabeticos" not in st.session_state:
        st.session_state["n_consultas_diabeticos"] = 2

    if "n_horas_base" not in st.session_state:
        st.session_state["n_horas_base"] = 40
    if "n_horas_nao_assistencial" not in st.session_state:
        st.session_state["n_horas_nao_assistencial"] = 4
    if "p_doneça_aguda" not in st.session_state:
        st.session_state["p_doneça_aguda"] = 30
    if "tempo_consulta_doença_aguda" not in st.session_state:
        st.session_state["tempo_consulta_doença_aguda"] = 15
    if "n_semanas_trabalho" not in st.session_state:
        st.session_state["n_semanas_trabalho"] = 44
