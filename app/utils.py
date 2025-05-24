import streamlit as st
import pandas as pd


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
