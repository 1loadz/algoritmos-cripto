import streamlit as st

from classes.base_algorithm import BaseAlgorithm, classproperty


class ModularExponentiation(BaseAlgorithm):
    
    @classproperty
    def input_format(cls):
        return r"\text{Calcula: } A^B \bmod N"
    
    params = ["a", "b", "n"]

    @staticmethod
    def validate_input(input):
        try:
            return int(input) != 0
        except ValueError:
            return False

    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n
    
    def find_cicle(self):
        st.write("### Achando um Ciclo: ")
        remainders = {}

        i = 1
        while(True):
            remainder = self.a**i % self.n
            
            # Ciclo encontrado
            if remainder in remainders.values():
                # st.write(remainders)
                return i-1, remainders
            
            string_latex = fr"{self.a}^{{{i}}} &\equiv {remainder} \pmod{{{self.n}}} \\"
            st.latex(f"\\begin{{align*}} {string_latex} \\end{{align*}}")

            remainders[i] = remainder
            i+=1


    def solve(self):
        exp, remainders = self.find_cicle()
        valor_repetido = remainders[exp]
        # st.write(remainders)
        # st.write(f"### Ciclo encontrado: {exp} e valor repetido: {valor_repetido}")

        # Prevenção contra exp = 0, embora find_cicle deva retornar >= 1 se n>=1
        if exp == 0:
            st.error("Erro: 'exp' calculado como zero, verifique a função find_cicle e os inputs.")
            return

        quotient = self.b // exp
        remainder = self.b % exp
        modular_result = pow(self.a, remainder, self.n)

        self.display_results(quotient, remainder, exp, modular_result, valor_repetido, remainders)


    def display_results(self, quotient, remainder, exp, modular_result, valor_repetido, remainders):
        string_latex = fr"""
        \begin{{alignat*}}{{2}}
        {self.a}^{{{self.b}}} &\equiv ({self.a}^{{{exp}}})^{{{quotient}}} \cdot {self.a}^{{{remainder}}} && \pmod{{{self.n}}} \\
        {self.a}^{{{self.b}}} &\equiv ({{{valor_repetido}}})^{{{quotient}}} \cdot {self.a}^{{{remainder}}} && \pmod{{{self.n}}} \\
        {self.a}^{{{self.b}}} &\equiv ({{{valor_repetido ** quotient}}}) \cdot {self.a}^{{{remainder}}} && \pmod{{{self.n}}} \\
        {self.a}^{{{self.b}}} &\equiv {(valor_repetido ** quotient * remainders[remainder])%self.n} && \pmod{{{self.n}}}
        \end{{alignat*}}
        """

        st.write("### Substituindo na nossa expressão:")
        st.latex(string_latex)




    # def display_results(self, quotient, remainder, exp, modular_result):
    #     string_latex = fr"""
    #     \begin{{alignat*}}{{2}}
    #     {self.a}^{{{self.b}}} &\equiv ({self.a}^{{{exp}}})^{{{quotient}}} \cdot {self.a}^{{{remainder}}} && \pmod{{{self.n}}} \\
    #     {self.a}^{{{self.b}}} &\equiv (1)^{{{quotient}}} \cdot {self.a}^{{{remainder}}} && \pmod{{{self.n}}} \\
    #     {self.a}^{{{self.b}}} &\equiv {self.a}^{{{remainder}}} && \pmod{{{self.n}}} \\
    #     {self.a}^{{{self.b}}} &\equiv {modular_result} && \pmod{{{self.n}}}
    #     \end{{alignat*}}
    #     """

    #     st.write("### Substituindo na nossa expressão:")
    #     st.latex(string_latex)
