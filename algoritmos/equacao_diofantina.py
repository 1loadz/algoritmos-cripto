import pandas as pd
from euclides import euclides

def diofantina(a, b, c):
    infos = euclides(a, b)

    # Não é divisivel
    if(c % (infos["mdc"] != 0)):
       return f"Essa equacao diofantina não tem solucão."
    
    # É divisivel
    div = c // (infos["mdc"])
    x = infos["alpha"]*div
    y = infos["beta"]*div

    print(f"X = {infos["alpha"]} x {div} = {x}")
    print(f"Y = {infos["beta"]} x {div} = {y}")

    return {"x": x, "y": y}


if __name__ == '__main__':
    a, b, c = 1801, 1301, 19112
    diofantina(a, b, c)
