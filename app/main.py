from classes.euclides import AlgoritmoEuclidianoEstendido
from classes.diofantina import EquacaoDiofantina
from classes.fermat import AlgoritmoDeFermat
from classes.modular_exp import ModularExponentiation
from classes.achar_fator import AcharUmFator
import streamlit as st


def main():
    st.write("""
            # Algoritmos da Matéria Criptografia e Números Inteiros
            """)

    # Escolha do algoritmo:
    algorithms_dict = {
                    "Euclides Estendido": AlgoritmoEuclidianoEstendido,
                    "Equação Diofantina": EquacaoDiofantina,
                    "Algoritmo de Fermat": AlgoritmoDeFermat,
                    "Exponenciação Modular": ModularExponentiation,
                    "Achar um Fator": AcharUmFator,
                }

    selected_algorithm = st.selectbox("Escolha um Algoritmo:", list(algorithms_dict.keys()))

    if selected_algorithm:
        st.markdown(f"""
        <p style='font-size:20px;'>
            Você selecionou: <strong><span style='color:#FF4B4B'>{selected_algorithm}</span></strong>
        </p>
    """, unsafe_allow_html=True)
        
        # Cria uma instância da classe correspondente ao algoritmo selecionado
        algorithm_class = algorithms_dict[selected_algorithm]
        params = algorithm_class.params
        args = {}

        # Explicar cada uma das variáveis
        with st.container():
            st.latex(algorithm_class.input_format)

        filled_inputs = True
        for param in params:
            value = st.text_input(f"### Valor de {param.capitalize()}:", key=param)
            if value == "":
                filled_inputs = False

            elif algorithm_class.validate_input(value):
                    args[param] = int(value)

            else:
                st.error("Por favor, digite um número inteiro diferente de zero.")
                filled_inputs = False


        # Botão para rodar a função
        execute = st.button("Executar", type="primary")
        if filled_inputs and execute:
            with st.spinner("Executando..."):
                # Instanciando a classe do algoritmo e chamando o método correspondente
                algorithm_object = algorithm_class(**args)
                algorithm_object.solve()
        else:
            st.write("Por favor, selecione uma opção para começar.")


if __name__ == "__main__":
    main()
