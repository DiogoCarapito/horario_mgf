import streamlit as st


def sidebar_results(resultados):
    st.session_state["radio_horas_consultas"] = st.sidebar.radio(
        "Horas/Nº de consultas",
        ["Horas", "Consultas"],
        horizontal=True,
        label_visibility="collapsed",
    )

    st.sidebar.subheader("Saúde Infantil")

    if st.session_state["radio_horas_consultas"] == "Horas":
        st.sidebar.metric(
            "Nº de horas semanais: ",
            resultados["horas_total_saude_infantil"],
        )
    else:
        st.sidebar.metric(
            "Nº de consultas semanais: ",
            resultados["n_consultas_total_saude_infantil"],
        )

    st.sidebar.subheader("Planeamento Familiar")

    st.sidebar.subheader("Saude Materna")

    st.sidebar.subheader("Diabetes")

    st.sidebar.subheader("Saúde Adulto")

    st.sidebar.subheader("Doença Aguda")

    st.sidebar.subheader("Não assistencial")

    st.sidebar.subheader("Total")
