#Inserção de informações no modelo de bd

print("Escolha uma das seguintes opções")
print("1-Listas")
print("2-Dicionarios")
print("3-Sair")

opcao = input("Escolha entre uma das opções:")

minha_lista = []
meu_dicionario = {}

while opcao != "3":
    if opcao == "1":
        print("1-Criar uma lista vazia.")
        print("2-Adicionar elementos à lista.")
        print("3-Remover elementos da lista.")
        print("4-Imprimir a lista completa.")

        opcao_lista = input("Escolha entre uma das opções:")

        if opcao_lista == "1":
            minha_lista = []
        elif opcao_lista == "2":
            elemento = input("Digite um elemento para adicionar à lista: ")
            minha_lista.append(elemento)
        elif opcao_lista == "3":
            if len(minha_lista) == 0:
                print("A lista está vazia.")
            else:
                elemento = input("Digite um elemento para remover da lista: ")
                minha_lista.remove(elemento)
        elif opcao_lista == "4":
            if minha_lista:
                print("Lista completa:")
                for elemento in minha_lista:
                    print(elemento)
            else:
                print("A lista está vazia.")

    elif opcao == "2":
        print("1-Criar um dicionário vazio.")
        print("2-Adicionar pares chave-valor ao dicionário.")
        print("3-Remover pares chave-valor do dicionário.")
        print("4-Imprimir o dicionário completo.")

        opcao_dicio = input("Escolha entre uma das opções:")

        if opcao_dicio == "1":
            meu_dicionario = {}
        elif opcao_dicio == "2":
            chave = input("Digite uma chave: ")
            valor = input("Digite um valor: ")
            meu_dicionario[chave] = valor
        elif opcao_dicio == "3":
            chave = input("Digite a chave a ser removida: ")
            if chave in meu_dicionario:
                del meu_dicionario[chave]
            else:
                print("Chave não encontrada no dicionário.")
        elif opcao_dicio == "4":
            if meu_dicionario:
                print("Dicionário completo:")
                for chave, valor in meu_dicionario.items():
                    print(f"{chave}: {valor}")
            else:
                print("O dicionário está vazio.")

    opcao = input("Escolha entre uma das opções (1-Listas, 2-Dicionarios, 3-Sair):")

print("Programa encerrado.")
