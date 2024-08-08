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
        * dados["taxa_utilização_crianças_2_18_anos"]
        / 100
        * dados["tempo_consulta_crianças_2_18_anos"]
        / 60
        / dados["n_semanas_trabalho"],
        2,
    )
    n_consultas_semanal_crianças_2_18_anos = round(
        dados["n_crianças_2_18_anos"]
        * dados["taxa_utilização_crianças_2_18_anos"]
        / 100
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
