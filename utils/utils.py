import streamlit as st


@st.cache_data
def calculos(dados):
    total_horas_trabalho_ano = (
        dados["n_semanas_trabalho"] * dados["n_horas_semanal_base"]
    )

    horas_semana_crianças_1_ano = round(
        dados["n_crianças_1_ano"]
        * dados["n_consultas_crianças_1_ano"]
        * dados["tempo_consulta_crianças_1_ano"]
        / 60
        / dados["n_semanas_trabalho"],
        2,
    )
    n_consultas_semanal_crianças_1_ano = round(
        dados["n_crianças_1_ano"]
        * dados["n_consultas_crianças_1_ano"]
        / dados["n_semanas_trabalho"],
        1,
    )

    horas_semana_crianças_1_2_anos = round(
        dados["n_crianças_1_2_anos"]
        * dados["n_consultas_crianças_1_2_anos"]
        * dados["tempo_consulta_crianças_1_2_anos"]
        / 60
        / dados["n_semanas_trabalho"],
        2,
    )
    n_consultas_semanal_crianças_1_2_anos = round(
        dados["n_crianças_1_2_anos"]
        * dados["n_consultas_crianças_1_2_anos"]
        / dados["n_semanas_trabalho"],
        1,
    )

    horas_semana_crianças_2_18_anos = round(
        dados["n_crianças_2_18_anos"]
        * dados["n_consultas_crianças_2_18_anos"]
        * dados["tempo_consulta_crianças_2_18_anos"]
        / 60
        / dados["n_semanas_trabalho"],
        2,
    )
    n_consultas_semanal_crianças_2_18_anos = round(
        dados["n_crianças_2_18_anos"]
        * dados["n_consultas_crianças_2_18_anos"]
        / dados["n_semanas_trabalho"],
        1,
    )

    horas_total_saude_infantil = round(
        horas_semana_crianças_1_ano
        + horas_semana_crianças_1_2_anos
        + horas_semana_crianças_2_18_anos,
        1,
    )
    n_consultas_total_saude_infantil = round(
        n_consultas_semanal_crianças_1_ano
        + n_consultas_semanal_crianças_1_2_anos
        + n_consultas_semanal_crianças_2_18_anos,
        1,
    )

    return {
        "total_horas_trabalho_ano": total_horas_trabalho_ano,
        "horas_semana_crianças_1_ano": horas_semana_crianças_1_ano,
        "n_consultas_semanal_crianças_1_ano": n_consultas_semanal_crianças_1_ano,
        "horas_semana_crianças_1_2_anos": horas_semana_crianças_1_2_anos,
        "n_consultas_semanal_crianças_1_2_anos": n_consultas_semanal_crianças_1_2_anos,
        "horas_semana_crianças_2_18_anos": horas_semana_crianças_2_18_anos,
        "n_consultas_semanal_crianças_2_18_anos": n_consultas_semanal_crianças_2_18_anos,
        "horas_total_saude_infantil": horas_total_saude_infantil,
        "n_consultas_total_saude_infantil": n_consultas_total_saude_infantil,
    }


@st.cache_data
def session_state_initialization():
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
        st.session_state["n_consultas_crianças_2_18_anos"] = 5

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
