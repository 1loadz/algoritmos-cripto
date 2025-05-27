import pandas as pd
from euclides import euclides

def find_cicle(a, n):
    remainders = [(0, 0)] * (n-1)

    print("Achando um Cicllo: ")

    i = 1
    while(1):
        remainder = a**i % n

        # Ciclo encontrado
        if remainders[remainder-1][1] != 0:
            # print(remainders)
            return i-1
        
        print(f"{a}^{i} = {remainder} mod {n}")
        
        remainders[remainder-1] = (i, remainder)
        i+=1


def solve_modular_exp(a, b, n):
    exp = find_cicle(a, n)

    parte_inteira = b // exp
    resto = b % exp

    teste = a**resto
    string_latex = r"""
                    \begin{align*}
                    {a}^{b} \pmod{n} \equiv ({a}^{exp})^{parte_inteira} \cdot {a}^{resto} \pmod{n} \\
                    {a}^{b} \pmod{n} \equiv (1)^{parte_inteira} \cdot {a}^{resto} \pmod{n} \\
                    {a}^{b} \pmod{n} \equiv {a}^{resto} \pmod{n} \\
                    {a}^{b} \pmod{n} \equiv {teste} \pmod{n} \\
                    \end{align*}
                    """
    
    print(f"{a}^{b} = ({a}^{exp})^{parte_inteira} * {a}^{resto}")



if __name__ == '__main__':
    a, b, n = 3, 9, 8
    solve_modular_exp(a, b, n)
