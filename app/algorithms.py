from utils import print_df
import streamlit as st
import pandas as pd
import math


@st.cache_data
def euclides(a, b):
    df = pd.DataFrame(columns=['resto', 'quociente', 'x', 'y'])
    if(b > a):
        aux = a
        a = b
        b = aux

    df.loc[0] = [a, '-', 1, 0]
    df.loc[1] = [b, '-', 0, 1]

    line = 1
    while(True):
        line += 1
        current_a = df.iloc[line-2, 0]
        current_b = df.iloc[line-1, 0]

        resto = current_a % current_b
        quociente = current_a // current_b

        if resto == 0:
            df.loc[line] = [resto, quociente, '-', '-']
            break

        x = df.iloc[line-2, 2] - df.iloc[line-1, 2] * quociente
        y = df.iloc[line-2, 3] - df.iloc[line-1, 3] * quociente
        
        df.loc[line] = [resto, quociente, x, y]

    st.write(f"### MDC({a}, {b}) = {df.iloc[line-1, 0]}")
    st.write(f"### Alfa = {df.iloc[line-1, 2]} | Beta = {df.iloc[line-1, 3]}")
    st.write(df)
    
    infos = {
        "df": df,
        "mdc": df.iloc[line-1, 0],
        "alpha": df.iloc[line-1, 2],
        "beta": df.iloc[line-1, 3]
    }
    return infos


@st.cache_data
def fermat(n):
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


@st.cache_data
def achar_um_fator(n):
    df = pd.DataFrame(columns=['Número', 'Fator?'])

    steps = 1
    f = 2
    while(True):
        if (n/f).is_integer():
            st.write(f"### {f} é um fator de {n}")
            df.loc[steps-1] = [f, "Sim"]
            break
        else:
            df.loc[steps-1] = [f, "Não"]

        f += 1

        if f > n**(1/2):
            st.write(f"### {n} é primo")
            break

        steps += 1
    st.write(f"### Quantidade de Passos: {steps}")
    # st.write(df)
    print_df(df)


@st.cache_data
def diofantina(a, b, c):
    infos = euclides(a, b)

    # Não é divisivel
    if (c % (infos["mdc"])) != 0:
       st.write(f"### Essa equação diofantina não tem solucão.")
       return
    
    # É divisivel
    div = c // (infos["mdc"])
    x = infos["alpha"]*div
    y = infos["beta"]*div

    st.write(f"### X =  {infos["alpha"]} * {div} = {x}")
    st.write(f"### Y =  {infos["beta"]} * {div} = {y}")

    return {"x": x, "y": y}


def find_cicle(a, n):
    if n <= 0:
        st.error("O módulo n deve ser um inteiro positivo.")
        return None

    remainders = [(0, 0)] * (n-1)

    st.write("### Achando um Ciclo: ")
    string_latex = r"\begin{{alignat*}}{{2}}"

    i = 1
    while(1):
        remainder = pow(a, i, n)

        # Ciclo encontrado
        if remainders[remainder-1][1] != 0:
            return i-1
        
        string_latex += fr"{a}^{{{i}}} &\equiv {{{remainder}}} \pmod{{{n}}} \\"        
        remainders[remainder-1] = (i, remainder)
        i+=1
    
    # print(remainders)
    string_latex += r"\end{{alignat*}}"
    st.latex(string_latex)


def find_cicle(a, n):
    remainders = [(0, 0)] * (n-1)

    st.write("### Achando um Ciclo: ")
    # string_latex = r""

    i = 1
    while(1):
        remainder = a**i % n

        # Ciclo encontrado
        if remainders[remainder-1][1] != 0:
            return i-1
        
        string_latex = fr"{a}^{{{i}}} &\equiv {{{remainder}}} \pmod{{{n}}} \\"
        st.latex(string_latex)      
        remainders[remainder-1] = (i, remainder)
        i+=1
    
    # print(remainders)
    # string_latex += r"\end{{alignat*}}"
    # st.latex(string_latex)


@st.cache_data
def solve_modular_exp(a, b, n):
    exp = find_cicle(a, n)

    # Prevenção contra exp = 0, embora find_cicle deva retornar >= 1 se n>=1
    if exp == 0:
        st.error("Erro: 'exp' calculado como zero, verifique a função find_cicle e os inputs.")
        return

    parte_inteira = b // exp
    resto = b % exp
    teste = pow(a, resto, n)

    # Usando alignat*{2}
    # X_1 & \equiv Y_1 && X_2
    # Onde X_1 é o LHS, Y_1 é a parte central do RHS.
    # X_2 é o \pmod{n} do RHS, que será alinhado à direita no segundo grupo de alinhamento.
    # Y_2 (a parte esquerda do segundo grupo) está implícita e vazia.
    string_latex = fr"""
    \begin{{alignat*}}{{2}}
    {a}^{{{b}}} \pmod{{{n}}} &\equiv ({a}^{{{exp}}})^{{{parte_inteira}}} \cdot {a}^{{{resto}}} && \pmod{{{n}}} \\
    {a}^{{{b}}} \pmod{{{n}}} &\equiv (1)^{{{parte_inteira}}} \cdot {a}^{{{resto}}} && \pmod{{{n}}} \\
    {a}^{{{b}}} \pmod{{{n}}} &\equiv {a}^{{{resto}}} && \pmod{{{n}}} \\
    {a}^{{{b}}} \pmod{{{n}}} &\equiv {teste} && \pmod{{{n}}}
    \end{{alignat*}}
    """

    st.write("### Substituindo na nossa expressão:")
    st.latex(string_latex)