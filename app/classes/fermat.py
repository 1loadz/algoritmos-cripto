import streamlit as st
import pandas as pd
import math


class AlgoritmoDeFermat():

    input_format = r"\text{Aplica o Algoritmo de Fermat para } N"
    params = ["n"]

    def __init__(self, n):
        self.n = n
        self.results = {}


    def display_results(self, df, x, y):
        if (x == (self.n+1)/2):
            st.write(f"## {self.n} é primo")
        else:
            st.write(f"## Fator 1: {x-y} | Fator 2: {x+y}")
        st.write(df)


    def fermat_algorithm(self):
        df = pd.DataFrame(columns=['n', 'x', 'y', 'z'])

        x = math.floor(math.sqrt(self.n))
        y = 0
        z = self.n - x**2 + y**2
        df.loc[0] = [self.n, x, 0, z]

        line = 0
        while(df.iloc[line, 3] != 0):
            line += 1
            x = df.iloc[line-1, 1] + 1
            y = math.floor(math.sqrt(x**2 - self.n))
            z = self.n - x**2 + y**2
            df.loc[line] = ['-', x, y, z]


        x = df.iloc[line, 1]
        y = df.iloc[line, 2]

        self.display_results(df, x, y)

        self.results = {
            "factor1": x - y,
            "factor2": x + y,
        }
    

    def solve(self):
        self.fermatalgorithm()
        return self.results