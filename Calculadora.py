import streamlit as st


def main():
    st.title("Calculadora Horário MGF")

    st.write("Cálculo da distribuição do tempo de trabalho dos médicos de família dependendo das características da lista.")
    
    n_crianças_jovens = st.number_input("Número de crianças e jovens (0-18 anos)")
    
    n_mulheres_idade_fertil = st.number_input("Número de mulheres em idade fértil (15-54 anos)")
    
    n_crianças_1_ano = st.number_input("Número de crianças com menos de 1 ano")

    n_crianças_2_anos = st.number_input("Número de crianças com menos de 2 anos")
    
    p_doneça_aguda = st.slider("Percentagem de doença aguda", 0, 100, 30)

if __name__ == "__main__":
    main()
