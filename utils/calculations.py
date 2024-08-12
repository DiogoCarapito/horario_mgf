import streamlit as st


@st.cache_data
def calculos(dados):
    
    st.write(dados)
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
    
    horas_consultas_planeamento_familiar = round(
        dados["n_mulheres_idade_fertil"]
        * dados["taxa_utilização_mulheres_idade_fertil"]
        / 100
        * dados["tempo_consulta_mulheres_idade_fertil"]
        / 60
        / dados["n_semanas_trabalho"],
        2,
    )
    
    n_consultas_planeamento_familiar = round(
        dados["n_mulheres_idade_fertil"]
        * dados["taxa_utilização_mulheres_idade_fertil"]
        / 100
        / dados["n_semanas_trabalho"],
        1,
    )
    
    horas_consultas_saude_materna = round(
        dados["n_nascimentos_ano_anterior"]
        * dados["n_consultas_gravidas"]
        * dados["tempo_consulta_gravidas"]
        / 60
        / dados["n_semanas_trabalho"],
        2,
    )

    n_consultas_saude_materna = round(
        dados["n_nascimentos_ano_anterior"]
        * dados["n_consultas_gravidas"]
        / dados["n_semanas_trabalho"],
        1,
    )
    
    horas_consultas_diabetes = round(
        dados["n_diabeticos"]
        * dados["n_consultas_diabeticos"]
        * dados["tempo_consulta_diabeticos"]
        / 60
        / dados["n_semanas_trabalho"],
        2,
    )
    n_consultas_diabetes = round(
        dados["n_diabeticos"]
        * dados["n_consultas_diabeticos"]
        / dados["n_semanas_trabalho"],
        1,
    )
    
    resultados = {
        "Total":{
            "Horas": total_horas_trabalho_ano,
            "Consultas": 0,
            },

        "Saúde Infantil":{
            "Horas": horas_total_saude_infantil,
            "Consultas": n_consultas_total_saude_infantil,
            "crianças_1_ano":{
                "Horas": horas_semana_crianças_1_ano,
                "Consultas": n_consultas_semanal_crianças_1_ano,
                },
            "crianças_1_2_anos":{
                "Horas": horas_semana_crianças_1_2_anos,
                "Consultas": n_consultas_semanal_crianças_1_2_anos,
                },
            "crianças_2_18_anos":{
                "Horas": horas_semana_crianças_2_18_anos,
                "Consultas": n_consultas_semanal_crianças_2_18_anos,
                },
            },
        "Planeamento Familiar":{
            "Horas": horas_consultas_planeamento_familiar,
            "Consultas": n_consultas_planeamento_familiar,
            },
        "Saúde Materna":{
            "Horas": horas_consultas_saude_materna,
            "Consultas": n_consultas_saude_materna,
            },
        "Diabetes":{
            "Horas": horas_consultas_diabetes,
            "Consultas": n_consultas_diabetes,
            },
    }

    return resultados