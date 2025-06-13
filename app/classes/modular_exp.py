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
        self.remainders[1] = self.a % self.n

        i = 2
        while(True):
            remainder = (self.remainders[i-1]*self.a) % self.n
            
            # Ciclo encontrado
            if remainder in self.remainders.values():
                self.cycle_start_exp = i-1
                # st.write(self.remainders)
                break

            self.remainders[i] = remainder
            i+=1
        
        self.display_cicle()
        self.remainders[0] = 1

    def display_cicle(self):
        st.write("### Achando um Ciclo:")

        items = list(self.remainders.items())
        limit = 3
        total_rows = self.cycle_start_exp

        if total_rows <= limit * 5:
            for key, value in items:
                string_latex = fr"{self.a}^{{{key}}} &\equiv {value} \pmod{{{self.n}}} \\"
                st.latex(f"\\begin{{align*}} {string_latex} \\end{{align*}}")

        else:
            for key, value in items[:limit]:
                string_latex = fr"{self.a}^{{{key}}} &\equiv {value} \pmod{{{self.n}}} \\"
                st.latex(f"\\begin{{align*}} {string_latex} \\end{{align*}}")

            st.latex(r"\text{... } ")

            for key, value in items[-limit:]:
                string_latex = fr"{self.a}^{{{key}}} &\equiv {value} \pmod{{{self.n}}} \\"
                st.latex(f"\\begin{{align*}} {string_latex} \\end{{align*}}")
            
            st.write(f"⚠️ {total_rows - 2 * limit} linhas omitidas no meio.")


    def solve(self):
        self.find_cicle()
        self.cycle_start_value = self.remainders[self.cycle_start_exp]

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
