import streamlit as st
import pandas as pd


class AlgoritmoEuclidianoEstendido():

    input_format = "Calcula o valor de MDC(A, B)"
    params = ["a", "b"]

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.results = {}
        # self.params = {"a": self.a, "b": self.b}
        

    
    def euclidean_division(_self, _a, _b):
        a = _a
        b = _b

        q = a // b
        r = a % b
        
        # Ajusta para garantir que o resto seja positivo
        if r < 0:
            q += 1
            r -= b

        return q, r

    def validate_input():
        ...

    
    def euclides(_self):
        df = pd.DataFrame(columns=['resto', 'quociente', 'x', 'y'])
        if(_self.b > _self.a):
            aux = _self.a
            _self.a = _self.b
            _self.b = aux

        df.loc[0] = [_self.a, '-', 1, 0]
        df.loc[1] = [_self.b, '-', 0, 1]

        line = 1
        while(True):
            line += 1
            current_a = df.iloc[line-2, 0]
            current_b = df.iloc[line-1, 0]

            quociente, resto = _self.euclidean_division(current_a, current_b)

            if resto == 0:
                df.loc[line] = [resto, quociente, '-', '-']
                break

            x = df.iloc[line-2, 2] - df.iloc[line-1, 2] * quociente
            y = df.iloc[line-2, 3] - df.iloc[line-1, 3] * quociente
            
            df.loc[line] = [resto, quociente, x, y]

        with st.container():
            st.write("\n")
            st.write("## Resultados do Algoritmo Euclidiano Estendido:")
            st.write(f"#### MDC({_self.a}, {_self.b}) = {df.iloc[line-1, 0]}")
            st.write(f"#### α = {df.iloc[line-1, 2]}  |  β = {df.iloc[line-1, 3]}")
            st.write(df)

        _self.results = {
            "df": df,
            "mdc": df.iloc[line-1, 0],
            "alpha": df.iloc[line-1, 2],
            "beta": df.iloc[line-1, 3]
        }

        return _self.results


    def solve(self):
        return self.euclides()
