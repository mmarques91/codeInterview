def gas_perc(custo, gas):
    id = 0
    resto = 0
    prej = 0
    for i in range(len(gas)):
        resto = gas[i] - custo[i]
        if resto < 0:
            id = i+1
            prej += resto
            resto = 0
    if id == len(gas) or resto + prej < 0:
        return -1
    else:
        return id
