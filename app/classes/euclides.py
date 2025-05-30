import streamlit as st
import pandas as pd


class AlgoritmoEuclidianoEstendido():

    input_format = "Calcula o valor de MDC(A, B)"

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.params = {"a": self.a, "b": self.b}
        self.results = {}
        

    @st.cache_data
    def euclidean_division(self):
        a = self.a
        b = self.b

        q = a // b
        r = a % b
        if r < 0:
            # ajusta para garantir que o resto seja positivo
            q += 1
            r -= b
        return q, r

    def validate_input():
        ...

    @st.cache_data
    def euclides(self):
        a = self.a
        b = self.b

        df = pd.DataFrame(columns=['resto', 'quociente', 'x', 'y'])
        if(b > a):
            aux = a
            a = b
            b = aux

        df.loc[0] = [a, '-', 1, 0]
        df.loc[1] = [b, '-', 0, 1]

        line = 1
        while(True):
            line += 1
            current_a = df.iloc[line-2, 0]
            current_b = df.iloc[line-1, 0]

            # resto = current_a % abs(current_b)
            # quociente = current_a // current_b
            quociente, resto = self.euclidean_division(current_a, current_b)

            if resto == 0:
                df.loc[line] = [resto, quociente, '-', '-']
                break

            x = df.iloc[line-2, 2] - df.iloc[line-1, 2] * quociente
            y = df.iloc[line-2, 3] - df.iloc[line-1, 3] * quociente
            
            df.loc[line] = [resto, quociente, x, y]

        with st.container():
            st.write("\n")
            st.write("## Resultados do Algoritmo Euclidiano Estendido:")
            st.write(f"#### MDC({a}, {b}) = {df.iloc[line-1, 0]}")
            st.write(f"#### α = {df.iloc[line-1, 2]}  |  β = {df.iloc[line-1, 3]}")
            st.write(df)

        self.results = {
            "df": df,
            "mdc": df.iloc[line-1, 0],
            "alpha": df.iloc[line-1, 2],
            "beta": df.iloc[line-1, 3]
        }

        return self.results
