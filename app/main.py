# from classes.euclides import AlgoritmoEuclidianoEstendido
from algorithms import fermat, euclides, achar_um_fator, diofantina, solve_modular_exp
import streamlit as st
import pandas as pd
import inspect


def validate_input(input):
    try:
        return int(input) != 0
    except ValueError:
        return False


def main():
    st.write("""
            # Algoritmos da Matéria Criptografia e Números Inteiros
            """)

    # Escolha de qual funcao usar:
    algorithms_dict = {
                    "Euclides Estendido": euclides,
                    "Equação Diofantina": diofantina,
                    "Algoritmo de Fermat": fermat,
                    "Exponenciação Modular": solve_modular_exp,
                    "Achar um Fator": achar_um_fator,
                }

    selected_algorithm = st.selectbox("Escolha um Algoritmo:", list(algorithms_dict.keys()))

    if selected_algorithm:
        st.markdown(f"""
        <p style='font-size:20px;'>
            Você selecionou: <strong><span style='color:#FF4B4B'>{selected_algorithm}</span></strong>
        </p>
    """, unsafe_allow_html=True)
        
        # Explicar cada uma das variáveis
        # with st.container():
        #     st.write("##### O que significa cada variavel:")
        #     st.write("xxxxxxxxxxxxxx")
        
        selected_function = algorithms_dict[selected_algorithm]
        params = inspect.signature(selected_function).parameters
        args = {}
        filled_inputs = True

        for param_name, obj_param in params.items():
            value = st.text_input(f"### Valor de {param_name.capitalize()}:", key=param_name)
            if value == "":
                filled_inputs = False
            else:
                if validate_input(value):
                    args[param_name] = int(value)
                else:
                    st.error("Por favor, digite um número inteiro diferente de zero.")
                    filled_inputs = False

        # Botão para rodar a função
        execute = st.button("Executar", type="primary")
        if filled_inputs and execute:
            with st.spinner("Executando..."):
                # df = selected_function(**args)
                # st.write(df)
                selected_function(**args)

    else:
        st.write("Por favor, selecione uma opção para começar.")


if __name__ == "__main__":
    main()
