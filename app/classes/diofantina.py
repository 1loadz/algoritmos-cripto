import streamlit as st

from classes.base_algorithm import BaseAlgorithm, classproperty
from classes.euclides import AlgoritmoEuclidianoEstendido


class EquacaoDiofantina(BaseAlgorithm):

    @classproperty
    def input_format(cls):
        return r"\text{Calcula a seguinte Equação Diofantina: } Ax + By = C"
    
    params = ["a", "b", "c"]

    @staticmethod
    def validate_input(input):
        try:
            return int(input) != 0
        except ValueError:
            return False


    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        self.x0 = None
        self.y0 = None

        euclides = AlgoritmoEuclidianoEstendido(a, b)
        self.infos = euclides.solve()

        self.mdc = self.infos["mdc"]
        self.alpha = self.infos["alpha"]
        self.beta = self.infos["beta"]
    

    def compute_particular_solution(self):
        div = self.c // self.mdc
        self.x0 = self.alpha * div
        self.y0 = self.beta * div

    def display_particular_solution(self):
        with st.container():
            st.write("\n")
            st.markdown(f"""
                <style>
                    .hover-red:hover {{
                        color: #FF4B4B !important;
                    }}
                </style>
                <p class='hover-red' style='font-size:34px; color:white;'>
                    <strong>Solução Particular da Equação Diofantina:</strong>
                </p>
                """, unsafe_allow_html=True
            )

            div = self.c // self.mdc
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.latex(rf"""
                        \begin{{align*}}
                        X_0 &= \alpha \cdot \left( \frac{{c}}{{\text{{mdc}}}} \right) \\[2em]
                        X_0 &= {self.alpha} \cdot \left( \frac{{{self.c}}}{{{self.mdc}}} \right) \\[2em]
                        X_0 &= {self.alpha} \cdot {div} = {self.x0}
                        \end{{align*}}
                """)

            with col2:
                st.latex(rf"""
                        \begin{{align*}}
                        Y_0 &= \beta \cdot \left( \frac{{c}}{{\text{{mdc}}}} \right) \\[2em]
                        Y_0 &= {self.beta} \cdot \left( \frac{{{self.c}}}{{{self.mdc}}} \right) \\[2em]
                        Y_0 &= {self.beta} \cdot {div} = {self.y0}
                        \end{{align*}}
                """)

    def display_general_solution(self):
        with st.container():
            st.write("\n")
            st.markdown(f"""
                <style>
                    .hover-red:hover {{
                        color: #FF4B4B !important;
                    }}
                </style>
                <p class='hover-red' style='font-size:34px; color:white;'>
                    <strong>Solução Geral da Equação Diofantina:</strong>
                </p>
                """, unsafe_allow_html=True
            )

            col1, col2 = st.columns([1, 1])
            with col1:
                st.latex(rf"""
                        \begin{{align*}}
                        X &= X_0 + \frac{{b}}{{\text{{mdc}}}} \cdot t \\[2em]
                        X &= {self.x0} + \frac{{{self.b}}}{{{self.mdc}}} \cdot t \\[2em]
                        X &= {self.x0} + ({self.b//self.mdc}) \cdot t
                        \end{{align*}}
                """)

            with col2:
                st.latex(rf"""
                        \begin{{align*}}
                        Y &= Y_0 - \frac{{a}}{{\text{{mdc}}}} \cdot t \\[2em]
                        Y &= {self.y0} - \frac{{{self.a}}}{{{self.mdc}}} \cdot t \\[2em]
                        Y &= {self.y0} - ({self.a//self.mdc}) \cdot t
                        \end{{align*}}
                """)


    def solve(self):
        # Não é divisivel
        if (self.c % self.mdc) != 0:
            st.write(f"### Essa equação diofantina não tem solucão.")
            return
        
        # É divisivel
        self.compute_particular_solution()
        self.display_particular_solution()
        self.display_general_solution()
