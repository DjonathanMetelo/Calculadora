def operacoes(opcao):

    while True:

        try:

            num1 = input("Insira o Primeiro Numero: ")
            num2 = input("Insira o Segundo Numero:")

            if opcao == '1':
                resu = float(num1) + float(num2)
                return resu

            elif opcao == '2':
                resu = float(num1) - float(num2)
                return resu

            elif opcao == '3':
                resu = float(num1) * float(num2)
                return resu

            elif opcao == '4':
                try:
                    resu = float(num1) / float(num2)
                    return resu
                except ZeroDivisionError:
                    print("erro: divisão por 0")

        except ValueError:

            print("Insira um numero Valido:")

def loopmenu():

    while True:
        menu = input("deseja voltar ao menu? (S/N) ").strip().lower()
        if menu == 's':
            return True
        elif menu == 'n':
            return False
        else:
            print("Opção Indisponivel")

def calculadora ():
    while True:
        print("")
        print("Calculadora")
        print("Escolha a opção desejada: ")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")
        opcao = input("Opção: ")

        if opcao in {'1', '2', '3', '4'}:
            resultados = operacoes(opcao)
            print("resultado: ", resultados)
            retorno = loopmenu()
            if retorno:
                print("Retornando ao menu...")
            else:
                print("Finalizando o Programa...")
                print("Volte Sempre!")
                break

        elif opcao == '5':
            break
        else:
            print("Opção não disponivel")



calculadora()