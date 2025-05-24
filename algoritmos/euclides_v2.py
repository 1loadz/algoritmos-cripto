from sympy import symbols, div, Poly, factorial, sympify
import pandas as pd


def poly_div(var, exp1, exp2):
    n = symbols(var)

    dividendo = Poly(sympify(exp1), n, domain='QQ')
    divisor = Poly(sympify(exp2), n, domain='QQ')

    # Quociente e resto normal (pode ter fração)
    quociente, resto = div(dividendo, divisor)

    # Arredondamos os coeficientes do quociente para baixo (parte inteira)
    quociente_int = Poly([int(c) for c in quociente.all_coeffs()], n, domain='ZZ')

    # Recalculamos o resto com base no novo quociente inteiro
    resto_int = (dividendo - quociente_int * divisor)

    quociente_str = str(quociente_int.as_expr())
    resto_str = str(resto_int.as_expr())

    return quociente_str, resto_str


def euclides(a, b):
    df = pd.DataFrame(columns=['resto', 'quociente', 'x', 'y'])

    df.loc[0] = [a, '-', 1, 0]
    df.loc[1] = [b, '-', 0, 1]

    mdc = 0
    line = 1
    while(line<10):
        line += 1
        current_a = df.iloc[line-2, 0]
        current_b = df.iloc[line-1, 0]

        quociente, resto = poly_div('n', current_a, current_b)

        if resto == 0 or resto == '0':
            df.loc[line] = [resto, quociente, '-', '-']
            mdc = df.iloc[line-1, 0]
            break
            
        x = sympify(df.iloc[line-2, 2]) - sympify(df.iloc[line-1, 2]) * sympify(quociente)
        y = sympify(df.iloc[line-2, 3]) - sympify(df.iloc[line-1, 3]) * sympify(quociente)

        df.loc[line] = [resto, quociente, x, y]

        if resto.isnumeric():
            if int(resto) > 1:
                mdc = f"MDC({df.iloc[line-1, 0]}, {df.iloc[line, 0]})"
                break

        # print(df.loc[line])

    print(df)

    print(f"\nMDC({a}, {b}) = {mdc}")
    print(f"Alpha = {df.iloc[line-1, 2]} / Beta = {df.iloc[line-1, 3]}")


if __name__ == '__main__':
    a, b = '3*n+1', '2*n+1'
    euclides(a, b)
