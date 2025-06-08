import streamlit as st


class ModularExponentiation():
    
    @property
    def input_format(self):
        return r"\text{Calcula: } a^b \bmod n"
    
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

    def solve(self):
        exp = self.find_cicle()

        # Prevenção contra exp = 0, embora find_cicle deva retornar >= 1 se n>=1
        if exp == 0:
            st.error("Erro: 'exp' calculado como zero, verifique a função find_cicle e os inputs.")
            return

        quotient = self.b // exp
        remainder = self.b % exp
        modular_result = pow(self.a, remainder, self.n)

        self.display_results(quotient, remainder, exp, modular_result)

    def display_results(self, quotient, remainder, exp, modular_result):
        string_latex = fr"""
        \begin{{alignat*}}{{2}}
        {self.a}^{{{self.b}}} &\equiv ({self.a}^{{{exp}}})^{{{quotient}}} \cdot {self.a}^{{{remainder}}} && \pmod{{{self.n}}} \\
        {self.a}^{{{self.b}}} &\equiv (1)^{{{quotient}}} \cdot {self.a}^{{{remainder}}} && \pmod{{{self.n}}} \\
        {self.a}^{{{self.b}}} &\equiv {self.a}^{{{remainder}}} && \pmod{{{self.n}}} \\
        {self.a}^{{{self.b}}} &\equiv {modular_result} && \pmod{{{self.n}}}
        \end{{alignat*}}
        """

        st.write("### Substituindo na nossa expressão:")
        st.latex(string_latex)
