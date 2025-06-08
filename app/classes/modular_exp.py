import streamlit as st
import pandas as pd


class ModularExponentiation():
    
    input_format = fr"Calcula: a^b (mod n)"
    params = ["a", "b", "n"]

    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n
    

    def find_cicle(self):
        remainders = [(0, 0)] * (self.n-1)

        st.write("### Achando um Ciclo: ")

        i = 1
        while(1):
            remainder = self.a**i % self.n

            # Ciclo encontrado
            if remainders[remainder-1][1] != 0:
                return i-1
            
            string_latex = fr"{self.a}^{{{i}}} &\equiv {remainder} \pmod{{{self.n}}} \\"
            st.latex(f"\\begin{{align*}} {string_latex} \\end{{align*}}")

            remainders[remainder-1] = (i, remainder)
            i+=1


    def solve_modular_exp(self):
        exp = self.find_cicle()

        # Prevenção contra exp = 0, embora find_cicle deva retornar >= 1 se n>=1
        if exp == 0:
            st.error("Erro: 'exp' calculado como zero, verifique a função find_cicle e os inputs.")
            return

        parte_inteira = self.b // exp
        resto = self.b % exp
        teste = pow(self.a, resto, self.n)

        string_latex = fr"""
        \begin{{alignat*}}{{2}}
        {self.a}^{{{self.b}}} &\equiv ({self.a}^{{{exp}}})^{{{parte_inteira}}} \cdot {self.a}^{{{resto}}} && \pmod{{{self.n}}} \\
        {self.a}^{{{self.b}}} &\equiv (1)^{{{parte_inteira}}} \cdot {self.a}^{{{resto}}} && \pmod{{{self.n}}} \\
        {self.a}^{{{self.b}}} &\equiv {self.a}^{{{resto}}} && \pmod{{{self.n}}} \\
        {self.a}^{{{self.b}}} &\equiv {teste} && \pmod{{{self.n}}}
        \end{{alignat*}}
        """

        st.write("### Substituindo na nossa expressão:")
        st.latex(string_latex)


    def solve(self):
        self.solve_modular_exp()