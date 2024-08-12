import streamlit as st

if "radio_horas_consultas" not in st.session_state:
    st.session_state["radio_horas_consultas"] = "Horas"

def sidebar_metrics(results):
    for key, value in results.items():
        if st.session_state["radio_horas_consultas"] == "Horas":
            final_value = value["Horas"]
            final_label = "Nº de horas semanais: "
        else:
            final_value = value["Consultas"]
            final_label = "Nº de consultas semanais: "
        st.sidebar.metric(key, final_value)

def sidebar_results(resultados):
    st.session_state["radio_horas_consultas"] = st.sidebar.radio(
        "Horas/Nº de consultas",
        ["Horas", "Consultas"],
        horizontal=True,
        label_visibility="collapsed",
    )


    sidebar_metrics(resultados)
    # for key, value in resultados.items():
    #     sidebar_metrics(key,value)

    # st.sidebar.subheader("Total")

    # st.sidebar.subheader("Saúde Infantil")

    # # if st.session_state["radio_horas_consultas"] == "Horas":
    # #     st.sidebar.metric(
    # #         "Nº de horas semanais: ",
    # #         resultados["horas_total_saude_infantil"],
    # #     )
    # # else:
    # #     st.sidebar.metric(
    # #         "Nº de consultas semanais: ",
    # #         resultados["n_consultas_total_saude_infantil"],
    # #     )


    # st.sidebar.subheader("Planeamento Familiar")

    # st.sidebar.subheader("Saude Materna")

    # st.sidebar.subheader("Diabetes")

    # st.sidebar.subheader("Saúde Adulto")

    # st.sidebar.subheader("Doença Aguda")

    # st.sidebar.subheader("Não assistencial")


