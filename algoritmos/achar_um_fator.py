import pandas as pd

def achar_um_fator(n):
    df = pd.DataFrame(columns=['Número', 'Fator?'])

    steps = 1
    f = 2
    while(True):
        if (n/f).is_integer():
            print(f"{f} é um fator de {n}")
            df.loc[steps-1] = [f, "Sim"]
            break
        else:
            df.loc[steps-1] = [f, "Não"]

        f += 1

        if f > n**(1/2):
            print(f"{n} é primo")
            break

        steps += 1
    print(f"Quantidade de Passos: {steps}")
    print(df)


if __name__ == '__main__':
    n = 7963
    achar_um_fator(n)
