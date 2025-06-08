import streamlit as st
import pandas as pd
import math


class AlgoritmoDeFermat():

    input_format = "Aplica o Algoritmo de Fermat para N"
    params = ["n"]

    def __init__(self, n):
        self.n = n
        # self.param = {"n": self.n}


    def fermat(self):
        n = self.n
        df = pd.DataFrame(columns=['n', 'x', 'y', 'z'])

        x = math.floor(math.sqrt(n))
        y = 0
        z = n - x**2 + y**2
        df.loc[0] = [n, x, 0, z]

        line = 0
        while(df.iloc[line, 3] != 0):
            line += 1
            x = df.iloc[line-1, 1] + 1
            y = math.floor(math.sqrt(x**2 - n))
            z = n - x**2 + y**2
            df.loc[line] = ['-', x, y, z]


        x = df.iloc[line, 1]
        y = df.iloc[line, 2]

        if (x == (n+1)/2):
            st.write(f"## {n} é primo")
        else:
            st.write(f"## Fator 1: {x-y} | Fator 2: {x+y}")
        st.write(df)
    

    def solve(self):
        self.fermat()