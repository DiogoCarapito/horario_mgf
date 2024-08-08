import streamlit as st

from utils.utils import initial_values
from utils.calculations import calculos
from utils.sidebar import sidebar_results


def main():
    st.title("Calculadora Horário MGF")

    st.write(
        "Cálculo da distribuição do tempo de trabalho dos médicos de família dependendo das características da lista."
    )

    
    
    if "input_horario" not in st.session_state:
        st.session_state["input_horario"] = initial_values()

    st.subheader("Horário Base")
    col_horario_base_1, col_horario_base_2, col_horario_base_3 = st.columns(
        3, vertical_alignment="bottom"
    )

    with col_horario_base_1:
        st.session_state["n_horas_semanal_base"] = st.number_input(
            "Nº de horas base", 0, 60, 40
        )

    with col_horario_base_2:
        st.session_state["n_semanas_trabalho"] = st.number_input(
            "Nº de semanas por ano", 0, 52, 44
        )

    with col_horario_base_3:
        st.session_state["n_horas_nao_assistencial"] = st.number_input(
            "Nº de horas não assistencial", 0, 40, 4
        )

    col_doença_aguda_1, col_doença_aguda_2 = st.columns(
        [2, 1], vertical_alignment="bottom"
    )
    with col_doença_aguda_1:
        st.session_state["p_doneça_aguda"] = st.slider(
            "Percentagem de doença aguda", 0, 100, 30
        )

    with col_doença_aguda_2:
        st.session_state["tempo_consulta_doença_aguda"] = st.number_input(
            "Tempo por consulta doença aguda", 0, 30, 15
        )

    st.divider()

    st.subheader("Crianças < 1 ano")
    col_crianças_1_ano_1, col_crianças_1_ano_2, n_crianças_1_ano_3 = st.columns(
        3, vertical_alignment="bottom"
    )

    with col_crianças_1_ano_1:
        st.session_state["n_crianças_1_ano"] = st.number_input(
            "Nº de crianças < 1 ano", step=1, value=15
        )
    with col_crianças_1_ano_2:
        st.session_state["tempo_consulta_crianças_1_ano"] = st.number_input(
            "Tempo por consulta crianças < 1 ano", step=5, value=30
        )

    with n_crianças_1_ano_3:
        st.session_state["n_consultas_crianças_1_ano"] = st.number_input(
            "Nº de consultas a crianças com menos de 1 ano por ano", step=1, value=6
        )

    st.subheader("Crianças entre 1 e 2 anos")

    col_crianças_2_ano_1, col_crianças_2_ano_2, n_crianças_2_ano_3 = st.columns(
        3, vertical_alignment="bottom"
    )

    with col_crianças_2_ano_1:
        st.session_state["n_crianças_1_2_anos"] = st.number_input(
            "Nº de crianças entre 1 e 2 anos", step=1, value=17
        )
    with col_crianças_2_ano_2:
        st.session_state["tempo_consulta_crianças_1_2_anos"] = st.number_input(
            "Tempo por consulta crianças entre 1 e 2 anos", step=5, value=30
        )

    with n_crianças_2_ano_3:
        st.session_state["n_consultas_crianças_1_2_anos"] = st.number_input(
            "Nº de consultas a crianças entre 1 e 2 anos por ano", step=1, value=5
        )

    st.subheader("Crianças e jovens 2-18 anos")

    col_crianças_jovens_1, col_crianças_jovens_2, col_crianças_jovens_3 = st.columns(
        3, vertical_alignment="bottom"
    )

    with col_crianças_jovens_1:
        st.session_state["n_crianças_2_18_anos"] = st.number_input(
            "Nº de crianças/jovens entre 2 e 18 anos", step=1, value=50
        )
    with col_crianças_jovens_2:
        st.session_state["tempo_consulta_crianças_2_18_anos"] = st.number_input(
            "Tempo por consulta crianças/jovens entre 2 e 18 anos", step=5, value=30
        )

    with col_crianças_jovens_3:
        st.session_state["taxa_utilização_crianças_2_18_anos"] = st.slider(
            "Taxa de consulta crianças/jovens entre 2 e 18 anos (%)",
            0,
            100,
            50,
        )

    st.divider()

    st.subheader("Mulheres em idade fértil")

    (
        col_mulheres_idade_fertil_1,
        col_mulheres_idade_fertil_2,
        col_mulheres_idade_fertil_3,
    ) = st.columns(3, vertical_alignment="bottom")

    with col_mulheres_idade_fertil_1:
        st.session_state["n_mulheres_idade_fertil"] = st.number_input(
            "Nº de mulheres em idade fértil (15-54 anos)", step=1, value=200
        )
    with col_mulheres_idade_fertil_2:
        st.session_state["tempo_consulta_mulheres_idade_fertil"] = st.number_input(
            "Tempo por consulta mulheres em idade fértil (min)", step=5, value=20
        )

    with col_mulheres_idade_fertil_3:
        st.session_state["taxa_utilização_mulheres_idade_fertil"] = st.slider(
            "Taxa de utilização de consultas (%) anual", 0, 100, 50
        )

    st.divider()

    st.subheader("Grávidas")

    col_gravidas_1, col_gravidas_2, col_gravidas_3 = st.columns(
        3, vertical_alignment="bottom"
    )
    with col_gravidas_1:
        st.session_state["n_nascimentos_ano_anterior"] = st.number_input(
            "Nº de nascimentos no ano anterior", step=1
        )
    with col_gravidas_2:
        st.session_state["tempo_consulta_gravidas"] = st.number_input(
            "Tempo por consulta gravida", step=5, value=30
        )
    with col_gravidas_3:
        st.session_state["n_consultas_gravidas"] = st.number_input(
            "Nº de consultas por ano", step=1, value=7
        )

    st.divider()

    st.subheader("Diabéticos")

    col_diabeticos_1, col_diabeticos_2, col_diabeticos_3 = st.columns(
        3, vertical_alignment="bottom"
    )

    with col_diabeticos_1:
        st.session_state["n_diabeticos"] = st.number_input(
            "Nº de diabéticos", step=1, value=100
        )
    with col_diabeticos_2:
        st.session_state["tempo_consulta_diabeticos"] = st.number_input(
            "Tempo por consulta diabéticos", step=5, value=30
        )
    with col_diabeticos_3:
        st.session_state["n_consultas_diabeticos"] = st.number_input(
            "Nº de consultas por ano", step=0.25, value=2.0
        )

    st.divider()

    dados = {
        "n_crianças_1_ano": st.session_state["n_crianças_1_ano"],
        "tempo_consulta_crianças_1_ano": st.session_state[
            "tempo_consulta_crianças_1_ano"
        ],
        "n_consultas_crianças_1_ano": st.session_state["n_consultas_crianças_1_ano"],
        "n_crianças_1_2_anos": st.session_state["n_crianças_1_2_anos"],
        "tempo_consulta_crianças_1_2_anos": st.session_state[
            "tempo_consulta_crianças_1_2_anos"
        ],
        "n_consultas_crianças_1_2_anos": st.session_state[
            "n_consultas_crianças_1_2_anos"
        ],
        "n_crianças_2_18_anos": st.session_state["n_crianças_2_18_anos"],
        "tempo_consulta_crianças_2_18_anos": st.session_state[
            "tempo_consulta_crianças_2_18_anos"
        ],
        "taxa_utilização_crianças_2_18_anos": st.session_state[
            "taxa_utilização_crianças_2_18_anos"
        ],
        "n_mulheres_idade_fertil": st.session_state["n_mulheres_idade_fertil"],
        "taxa_utilização_mulheres_idade_fertil": st.session_state[
            "taxa_utilização_mulheres_idade_fertil"
        ],
        "tempo_consulta_mulheres_idade_fertil": st.session_state[
            "tempo_consulta_mulheres_idade_fertil"
        ],
        "n_nascimentos_ano_anterior": st.session_state["n_nascimentos_ano_anterior"],
        "tempo_consulta_gravidas": st.session_state["tempo_consulta_gravidas"],
        "n_consultas_gravidas": st.session_state["n_consultas_gravidas"],
        "n_diabeticos": st.session_state["n_diabeticos"],
        "tempo_consulta_diabeticos": st.session_state["tempo_consulta_diabeticos"],
        "n_consultas_diabeticos": st.session_state["n_consultas_diabeticos"],
        "n_horas_semanal_base": st.session_state["n_horas_semanal_base"],
        "n_horas_nao_assistencial": st.session_state["n_horas_nao_assistencial"],
        "p_doneça_aguda": st.session_state["p_doneça_aguda"],
        "tempo_consulta_doença_aguda": st.session_state["tempo_consulta_doença_aguda"],
        "n_semanas_trabalho": st.session_state["n_semanas_trabalho"],
    }

    resultados = calculos(dados)

    st.title("Resultados detalhados")

    st.metric("Nº de horas de trabalho anual: ", resultados["total_horas_trabalho_ano"])

    st.divider()
    # st.header("Saúde Infantil")
    # st.metric(
    #     "Nº total de horas dedicadas à saúde infantil: ",
    #     resultados["horas_total_saude_infantil"],
    # )
    # st.metric(
    #     "Nº total de consultas de saúde infantil: ",
    #     resultados["n_consultas_total_saude_infantil"],
    # )

    st.subheader("Crianças < 1 ano")
    st.metric(
        "Nº de horas semanais dedicadas a crianças < 1 ano: ",
        resultados["horas_semana_crianças_1_ano"],
    )
    st.metric(
        "Nº de conusltas semanais a crianças < 1 anos",
        resultados["n_consultas_semanal_crianças_1_ano"],
    )

    st.subheader("Crianças entre 1 e 2 anos")
    st.metric(
        "Nº de horas semanais dedicadas a crianças entre 1 e 2 anos: ",
        resultados["horas_semana_crianças_1_2_anos"],
    )
    st.metric(
        "Nº de consultas semanais a crianças entre 1 e 2 anos",
        resultados["n_consultas_semanal_crianças_1_2_anos"],
    )

    st.subheader("Crianças e jovens entre 2 e 18 anos")
    st.metric(
        "Nº de horas semanais dedicadas a crianças e jovens entre 2 e 18 anos: ",
        resultados["horas_semana_crianças_2_18_anos"],
    )
    st.metric(
        "Nº de consultas semanais a crianças e jovens entre 2 e 18 anos",
        resultados["n_consultas_semanal_crianças_2_18_anos"],
    )

    # Sidebar

    st.sidebar.title("Resultados")

    sidebar_results(resultados)


if __name__ == "__main__":
    main()
