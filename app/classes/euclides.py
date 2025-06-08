import streamlit as st
import pandas as pd


class AlgoritmoEuclidianoEstendido():

    input_format = r"\text{Calcula } \mathrm{MDC}(A, B)"
    params = ["a", "b"]

    @staticmethod
    def validate_input(input):
        try:
            return int(input) != 0
        except ValueError:
            return False

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.results = {}        

    def euclidean_division(self, a, b):
        quociente = a // b
        resto = a % b
        
        # Ajusta para garantir que o resto seja positivo
        if resto < 0:
            quociente += 1
            resto -= b

        return quociente, resto

    def display_results(self, df, line):
        with st.container():
            st.write("\n")
            st.write("## Resultados do Algoritmo Euclidiano Estendido:")
            st.write(f"#### MDC({self.a}, {self.b}) = {df.iloc[line-1, 0]}")
            st.write(f"#### α = {df.iloc[line-1, 2]}  |  β = {df.iloc[line-1, 3]}")
            st.write(df)

    def euclides_algorithm(self):
        df = pd.DataFrame(columns=['resto', 'quociente', 'x', 'y'])
        if(self.b > self.a):
            aux = self.a
            self.a = self.b
            self.b = aux

        df.loc[0] = [self.a, '-', 1, 0]
        df.loc[1] = [self.b, '-', 0, 1]

        line = 1
        while(True):
            line += 1
            current_a = df.iloc[line-2, 0]
            current_b = df.iloc[line-1, 0]

            quociente, resto = self.euclidean_division(current_a, current_b)

            if resto == 0:
                df.loc[line] = [resto, quociente, '-', '-']
                break

            x = df.iloc[line-2, 2] - df.iloc[line-1, 2] * quociente
            y = df.iloc[line-2, 3] - df.iloc[line-1, 3] * quociente
            
            df.loc[line] = [resto, quociente, x, y]

        self.display_results(df, line)

        self.results = {
            "df": df,
            "mdc": df.iloc[line-1, 0],
            "alpha": df.iloc[line-1, 2],
            "beta": df.iloc[line-1, 3]
        }

    def solve(self):
        self.euclides_algorithm()
        return self.results
