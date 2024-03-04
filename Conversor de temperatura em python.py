#Conversor de temperatura em python

temperatura = float(input("Digite a temperatura: "))
origem = input("De escala (Celsius, Fahrenheit, Kelvin): ").capitalize()

destino = [
    "Celsius",
    "Fahrenheit",
    "Kelvin",
]
destino.remove(origem)

print("\nConversões de temperatura:")
for escala in destino:
  if origem == "Celsius":
    if escala == "Fahrenheit":
      resultado = (temperatura * 9 / 5) + 32
    elif escala == "Kelvin":
      resultado = temperatura + 273.15

  elif origem == "Fahrenheit":
    if escala == "Celsius":
      resultado = (temperatura - 32) * 5 / 9
    elif escala == "Kelvin":
      resultado = (temperatura - 32) * 5 / 9 + 273.15

  elif origem == "Kelvin":
    if escala == "Celsius":
      resultado = temperatura - 273.15
    elif escala == "Fahrenheit":
      resultado = (temperatura - 273.15) * 9 / 5 + 32

  else:
    resultado = temperatura

  print(f"{temperatura} graus {origem} é igual a {resultado} graus {escala}.")