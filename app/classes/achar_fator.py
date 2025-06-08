import pandas as pd
import streamlit as st

from classes.base_algorithm import BaseAlgorithm, classproperty


class AcharUmFator(BaseAlgorithm):
    
    @classproperty
    def input_format(cls):
        return r"\text{Calcula um fator de N}"
    
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
        isPrime = False
        fator = 1
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
                isPrime = True
                break

            steps += 1
        
        self.display_results(df, fator, steps, isPrime)
    
    def display_results(self, df, fator, steps, isPrime):
        with st.container():
            st.write("\n")
            st.write("## Resultado do Algoritmo Achar um Fator:")

            if isPrime:
                st.write(f"### {self.n} é um número primo")
            else:
                st.write(f"#### {fator} é um fator de {self.n}")

            st.write(f"#### Quantidade de Passos: {steps}")
            self.display_df(df)
    
    def display_df(self, df, n: int = 5, limit: int = 20):

        total_rows = len(df)

        if total_rows <= limit:
            st.dataframe(df)
        else:
            df_partial = pd.concat([df.head(n), df.tail(n)])
            st.dataframe(df_partial)
            st.markdown(f"⚠️ {total_rows - 2 * n} linhas omitidas no meio.")

    def solve(self):
        self.find_factor()
