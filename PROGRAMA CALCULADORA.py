v = input("")
opcao = 0
if v == "menu":
    while opcao != 5:
        print("------------")
        print ("1 - soma")
        print ("2 - subtração")
        print ("3 - multiplicação")
        print ("4 - divisão")
        print ("5 - sair")
        opcao = int(input("Digite a opção que você deseja: "))

        if opcao == 1:
            n1 = int(input("Digite o primeiro valor: "))
            n2 = int(input("Digite o segundo valor: "))
            print("------------")
            print("o primeiro valor + o segundo valor é = ", n1+n2)
        elif opcao == 2:
            n1 = int(input("Digite o primeiro valor: "))
            n2 = int(input("Digite o segundo valor: "))
            print("------------")
            print("o primeiro valor - o segundo valor é = ",n1-n2)
        elif opcao == 3:
            n1 = int(input("Digite o primeiro valor: "))
            n2 = int(input("Digite o segundo valor: "))
            print("------------")
            print("o primeiro valor * o segundo valor é =  ", n1*n2)
        elif opcao == 4:
            n1 = int(input("Digite o primeiro valor: "))
            n2 = int(input("Digite o segundo valor: "))
            print("------------")
            print("o primeiro valor / pelo segundo valor é = ", n1/n2)