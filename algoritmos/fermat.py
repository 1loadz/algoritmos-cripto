import pandas as pd
import math

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

    print(df)

    x = df.iloc[line, 1]
    y = df.iloc[line, 2]

    if (x == (n+1)/2):
        print(f"\n{n} é primo")
    else:
        print(f"\nFator 1: {x-y} / Fator 2: {x+y}")

if __name__ == '__main__':
    # n = 69939029
    n = 1234
    fermat(n)
