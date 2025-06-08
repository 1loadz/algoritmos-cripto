import streamlit as st
import pandas as pd
from utils import print_df


class AcharUmFator():
    input_format = r"\text{Calcula um fator de N}"
    params = ["n"]

    @staticmethod
    def validate_input(input):
        try:
            return int(input) != 0
        except ValueError:
            return False

    def __init__(self, n):
        self.n = n
    

    def find_factor(self):
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

            if f**2 > self.n:
                st.write(f"### {self.n} é primo")
                break

            steps += 1
        
        self.display_results(df, fator, steps)
    
    def display_results(self, df, f, steps):
        with st.container():
            st.write("\n")
            st.write("## Resultado do Algoritmo Achar um Fator:")
            st.write(f"#### {f} é um fator de {self.n}")
            st.write(f"#### Quantidade de Passos: {steps}")
            print_df(df)

    def solve(self):
        self.find_factor()
