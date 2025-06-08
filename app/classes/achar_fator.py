import streamlit as st
import pandas as pd
from utils import print_df


class AcharUmFator():
    input_format = r"Calcula um fator de n"
    params = ["n"]

    def __init__(self, n):
        self.n = n
    

    def achar_um_fator(self):
        df = pd.DataFrame(columns=['Número', 'Fator?'])
        fator = 0
        steps = 1
        f = 2
        while(True):
            if (self.n/f).is_integer():
                fator = f
                df.loc[steps-1] = [f, "Sim"]
                break
            else:
                df.loc[steps-1] = [f, "Não"]

            f += 1

            if f > self.n**(1/2):
                st.write(f"### {self.n} é primo")
                break

            steps += 1
        
        with st.container():
            st.write("\n")
            st.write("## Resultado do Algoritmo Achar um Fator:")
            st.write(f"#### {f} é um fator de {self.n}")
            st.write(f"#### Quantidade de Passos: {steps}")
            print_df(df)
    

    def solve(self):
        self.achar_um_fator()
