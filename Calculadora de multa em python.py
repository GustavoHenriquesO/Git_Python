#Calculadora de multa em python

velocidade = float(input("Qual a velocidade? (Km/h)"))

if velocidade > 60:
    if velocidade < 80:
        multa = 129.90 + ((velocidade - 60) * 7)
    elif velocidade < 100:
        multa = 129.90 + 20 * 7 + ((velocidade - 80) * 14)
    else:
        multa = 129.90 + 20 * 7 + 20 * 14 + ((velocidade - 100) * 39)

    print("Multa a ser paga:", multa)
else:
    print("velocidade dentro dos limites")


