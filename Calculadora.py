cont = 1
while (int(cont) == 1):
    print("")
    print("Calculadora")
    print("Escolha a opção desejada: ")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    opcao = input("Opção: ")

    menuLoop = 1

    if opcao == '1':
        num1 = input("Insira o Primeiro Numero: ")
        num2 = input("Insira o Segundo Numero:")
        x = float(num1) + float(num2)
        print("Resultado: ", float(x))
        while (int(menuLoop) == 1):
            menu = input("deseja voltar ao menu? (S/N) ")
            if (menu == "s") or (menu == "S"):
                print("Retornando ao menu...")
                menuLoop = 0
            elif (menu == "n") or (menu == "N"):
                print("Finalizando o Programa...")
                print("Volte Sempre!")
                menuLoop = 0
                cont = 0
            else:
                print("Opção Indisponivel")

    elif opcao == '2':
        num1 = input("Insira o Primeiro Numero: ")
        num2 = input("Insira o Segundo Numero:")
        x = float(num1) - float(num2)
        print("Resultado: ", float(x))
        while (int(menuLoop) == 1):
            menu = input("deseja voltar ao menu? (S/N) ")
            if (menu == "s") or (menu == "S"):
                print("Retornando ao menu...")
                menuLoop = 0
            elif (menu == "n") or (menu == "N"):
                print("Finalizando o Programa...")
                print("Volte Sempre!")
                menuLoop = 0
                cont = 0
            else:
                print("Opção Indisponivel")

    elif opcao == '3':
        num1 = input("Insira o Primeiro Numero: ")
        num2 = input("Insira o Segundo Numero:")
        x = float(num1) * float(num2)
        print("Resultado: ", float(x))
        while (int(menuLoop) == 1):
            menu = input("deseja voltar ao menu? (S/N) ")
            if (menu == "s") or (menu == "S"):
                print("Retornando ao menu...")
                menuLoop = 0
            elif (menu == "n") or (menu == "N"):
                print("Finalizando o Programa...")
                print("Volte Sempre!")
                menuLoop = 0
                cont = 0
            else:
                print("Opção Indisponivel")

    elif opcao == '4':
        divZero = 0
        while (int(divZero) == 0):
            num1 = input("Insira o Primeiro Numero: ")
            num2 = input("Insira o Segundo Numero:")
            if (int(num2) == 0):
                print("erro: divisão por zero")
                opDiv = input("deseja fazer outra divisão? (S/N)")
                if (opDiv == "s") or (opDiv == "S"):
                    print("Entendido...")
                elif (opDiv == "n") or (opDiv == "N"):
                    while (int(menuLoop) == 1):
                        menu = input("deseja voltar ao menu? (S/N) ")
                        if (menu == "s") or (menu == "S"):
                            print("Retornando ao menu...")
                            divZero = 1
                            menuLoop = 0
                        elif (menu == "n") or (menu == "N"):
                            print("Finalizando o Programa...")
                            print("Volte Sempre!")
                            divZero = 1
                            menuLoop = 0
                            cont = 0
                        else:
                            print("Opção Indisponivel")
                else:
                    print("Opção Indisponivel")

            else:
                divZero = 1
                x = float(num1) / float(num2)
                print("Resultado: ", float(x))
                while (int(menuLoop) == 1):
                    menu = input("deseja voltar ao menu? (S/N) ")
                    if (menu == "s") or (menu == "S"):
                        print("Retornando ao menu...")
                        menuLoop = 0
                    elif (menu == "n") or (menu == "N"):
                        print("Finalizando o Programa...")
                        print("Volte Sempre!")
                        menuLoop = 0
                        cont = 0
                    else:
                        print("Opção Indisponivel")

    elif opcao == '5':
        print("Volte Sempre")
        cont = 0

    else:
        print("Opção não disponivel")