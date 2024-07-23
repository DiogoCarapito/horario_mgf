import streamlit as st

def main():
    st.title("Calculadora Horário MGF")

    st.write("Cálculo da distribuição do tempo de trabalho dos médicos de família dependendo das características da lista.")
    
    col_1_1, col_1_2, col_1_3 = st.columns(3, vertical_alignment="bottom")
    
    with col_1_1:
        n_crianças_jovens = st.number_input(
            "Número de crianças e jovens (0-18 anos)",
            step=1
            )
        
    with col_1_2:
        n_crianças_1_ano = st.number_input(
            "Número de crianças com menos de 1 ano",
            step=1
            )
    with col_1_3:
        n_crianças_2_anos = st.number_input(
            "Número de crianças com menos de 2 anos",
            step=1
            )
    col_2_1, col_2_2, col_2_3 = st.columns(3, vertical_alignment="bottom")
    
    with col_2_1:
        n_mulheres_idade_fertil = st.number_input(
            "Número de mulheres em idade fértil (15-54 anos)",
            step=1
            )
    with col_2_2:   
        n_nascimentos_ano_anterior = st.number_input(
            "Número de nascimentos no ano anterior",
            step=1
            )
    with col_2_3:

        n_diabeticos = st.number_input(
            "Número de diabéticos",
            step=1
            )

    p_doneça_aguda = st.slider(
        "Percentagem de doença aguda",
        0,
        100,
        30
        )

if __name__ == "__main__":
    main()
