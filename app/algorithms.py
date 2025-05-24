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
    st.write(f"### Alpha = {df.iloc[line-1, 2]} | Beta = {df.iloc[line-1, 3]}")
    st.write(df)
    # return df


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
