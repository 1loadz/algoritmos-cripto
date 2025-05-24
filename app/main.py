from algorithms import fermat, euclides, achar_um_fator
import streamlit as st
import pandas as pd
import inspect


def print_df(df, n: int = 5, limit: int = 20):
    """
    Exibe um DataFrame no Streamlit, mostrando apenas as primeiras e últimas `n` linhas
    se o DataFrame for muito grande.

    Parâmetros:
    - df: DataFrame a ser exibido.
    - n: número de linhas do topo e do final a serem exibidas.
    """
    total_rows = len(df)

    if total_rows <= limit:
        st.dataframe(df)
    else:
        df_partial = pd.concat([df.head(n), df.tail(n)])
        st.dataframe(df_partial)
        st.markdown(f"⚠️ {total_rows - 2 * n} linhas omitidas no meio.")


def main():
    st.write("""
            # Algoritmos da Matéria Criptografia e Números Inteiros
            """)

    # Escolha de qual funcao usar:
    algorithms_dict = {
                    "Algoritmo de Fermat": fermat,
                    "Euclides Estendido": euclides,
                    "Achar um Fator": achar_um_fator,
                }

    selected_algorithm = st.selectbox("Escolha um Algoritmo:", list(algorithms_dict.keys()))

    if selected_algorithm:
        st.markdown(f"""
        <p style='font-size:20px;'>
            Você selecionou: <strong><span style='color:#FF4B4B'>{selected_algorithm}</span></strong>
        </p>
    """, unsafe_allow_html=True)
        
        selected_function = algorithms_dict[selected_algorithm]
        params = inspect.signature(selected_function).parameters
        args = {}
        inputs_preenchidos = True

        for param_name, obj_param in params.items():
            value = st.text_input(f"### Valor de {param_name.capitalize()}:", key=param_name)
            if value == "":
                inputs_preenchidos = False
            else:
                args[param_name] = int(value)

        # Botão para rodar a função
        if inputs_preenchidos and st.button("Executar"):
            with st.spinner("Executando..."):
                # df = selected_function(**args)
                # st.write(df)
                selected_function(**args)

    else:
        st.write("Por favor, selecione uma opção para começar.")


if __name__ == "__main__":
    main()
