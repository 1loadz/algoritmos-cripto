import math

import pandas as pd
import streamlit as st

from classes.base_algorithm import BaseAlgorithm, classproperty


class AlgoritmoDeFermat(BaseAlgorithm):

    @classproperty
    def input_format(cls):
        return r"\text{Aplica o Algoritmo de Fermat para } N"
    
    @classproperty
    def params(cls):
        params = ["n"]
        return params

    @staticmethod
    def validate_input(input):
        try:
            input = int(input)
            if input <= 0:
                st.error("Por favor, digite um número inteiro maior que zero.")
                return False
            if input%2 == 0:
                st.error("Por favor, digite um número inteiro ímpar.")
                return False
            return True
        
        except ValueError:
            st.error("Por favor, digite um número inteiro válido.")
            return False

    def __init__(self, n):
        self.n = n
        self.results = {}
    
    def display_results(self, values):
        if (self.results["factor1"] == 1 or self.results["factor2"] == 1):
            st.latex(rf"\LARGE {self.n} \text{{ é primo}}")
        else:
            st.latex(rf"\LARGE 1^\circ \text{{ Fator}}: {self.results['factor1']} \quad \mid \quad 2^\circ \text{{ Fator}}: {self.results['factor2']}")

        df = pd.DataFrame(values, columns=['n', 'x', 'y', 'z'])
        st.write(df)
        

    def fermat_algorithm(self):
        x = math.isqrt(self.n)
        x_squared = x * x
        y = 0
        z = self.n - x_squared + y**2

        values = []
        values.append((self.n, x, y, z))

        while z != 0:
            x += 1
            x_squared += 2*x - 1
            diff = x_squared - self.n
            if diff < 0:
                continue  # ou break, dependendo do contexto
            y = math.isqrt(diff)
            z = self.n - x_squared + y**2
            values.append(('-', x, y, z))

        self.results = {
            "factor1": x - y,
            "factor2": x + y,
        }

        return values

    def solve(self):
        values = self.fermat_algorithm()
        self.display_results(values)
        # return self.results
