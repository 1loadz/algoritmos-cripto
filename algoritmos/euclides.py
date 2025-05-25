import pandas as pd

def euclides(a, b):
    df = pd.DataFrame(columns=['resto', 'quociente', 'x', 'y'])

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

    # print(df)
    # print(f"\nMDC({a}, {b}) = {df.iloc[line-1, 0]}")
    # print(f"Alpha = {df.iloc[line-1, 2]} / Beta = {df.iloc[line-1, 3]}")

    infos = {
        "df": df,
        "mdc": df.iloc[line-1, 0],
        "alpha": df.iloc[line-1, 2],
        "beta": df.iloc[line-1, 3]
    }
    return infos


if __name__ == '__main__':
    a, b = 1801, 1301
    euclides(a, b)
