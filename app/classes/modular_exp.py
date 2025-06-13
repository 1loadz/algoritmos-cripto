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

        self.remainders = {}
        self.cycle_start_exp = None
        self.cycle_start_value = None

    
    def find_cicle(self):
        i = 1
        while(True):
            remainder = self.a**i % self.n
            
            # Ciclo encontrado
            if remainder in self.remainders.values():
                self.cycle_start_exp = i-1
                # st.write(self.remainders)
                break
            
            # string_latex = fr"{self.a}^{{{i}}} &\equiv {remainder} \pmod{{{self.n}}} \\"
            # st.latex(f"\\begin{{align*}} {string_latex} \\end{{align*}}")

            self.remainders[i] = remainder
            i+=1
        
        self.display_cicle()
        self.remainders[0] = 1

    def display_cicle(self):
        st.write("### Achando um Ciclo:")
        for key, value in self.remainders.items():
            string_latex = fr"{self.a}^{{{key}}} &\equiv {value} \pmod{{{self.n}}} \\"
            st.latex(f"\\begin{{align*}} {string_latex} \\end{{align*}}")
        
        #     st.write(f"#### Ciclo começa em {self.cycle_start_exp} com valor {self.remainders[self.cycle_start_exp]}")
        #     st.markdown(f"""
        #     <p style='font-size:24px;'>
        #         <strong><span style='color:#FF4B4B'>Ciclo começa em {self.cycle_start_exp} com valor {self.remainders[self.cycle_start_exp]}</span></strong>
        #     </p>
        # """, unsafe_allow_html=True)


    def solve(self):
        self.find_cicle()
        self.cycle_start_value = self.remainders[self.cycle_start_exp]

        # Prevenção contra cycle_start_exp = 0, embora find_cicle deva retornar >= 1 se n>=1
        if self.cycle_start_exp == 0:
            st.error("Erro: 'cycle_start_exp' calculado como zero, verifique a função find_cicle e os inputs.")
            return

        quotient = self.b // self.cycle_start_exp
        remainder = self.b % self.cycle_start_exp

        self.display_results(quotient, remainder, self.cycle_start_exp)


    def display_results(self, quotient, remainder, cycle_start_exp):
        string_latex = fr"""
        \begin{{alignat*}}{{2}}
        {self.a}^{{{self.b}}} &\equiv ({self.a}^{{{cycle_start_exp}}})^{{{quotient}}} \cdot {self.a}^{{{remainder}}} && \pmod{{{self.n}}} \\
        {self.a}^{{{self.b}}} &\equiv ({{{self.cycle_start_value}}})^{{{quotient}}} \cdot {self.a}^{{{remainder}}} && \pmod{{{self.n}}} \\
        {self.a}^{{{self.b}}} &\equiv ({{{self.cycle_start_value ** quotient}}}) \cdot {self.a}^{{{remainder}}} && \pmod{{{self.n}}} \\
        {self.a}^{{{self.b}}} &\equiv {(self.cycle_start_value ** quotient * self.remainders[remainder])%self.n} && \pmod{{{self.n}}}
        \end{{alignat*}}
        """

        st.write("### Substituindo na nossa expressão:")
        st.latex(string_latex)


if __name__ == "__main__":
    # Test the class with example values
    mod_exp = ModularExponentiation(3, 10, 7)
    mod_exp.solve()
