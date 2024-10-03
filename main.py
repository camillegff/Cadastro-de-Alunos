def menu_professor():
    while True:  # Termina quando o usuário escolher a opção sair
        opcao = int(input("\n[1] adicionar\n[2] editar\n[3] pesquisar\n[4] imprimir\n[5] sair\nInforme a opção desejada: "))
        if opcao == 1:
            print("Editar:")  # Função que captura os dados do aluno
        elif opcao == 2:
            print("Editar:")
        elif opcao == 3:
            print("Pesquisar:")
        elif opcao == 4:
            print("Imprimir:")
        elif opcao == 5:
            print("Saindo...")
            break  # O loop se encerra quando o usuário sai do programa
        else:
            print("Opção inválida. Tente novamente!")

def menu_aluno():
    while True:  # Termina quando o usuário escolher a opção sair
        opcao = int(input("\n[1] pesquisar\n[2] imprimir\n[3] sair\n "))
        if opcao == 1:
            print("Pesquisar:")
        elif opcao == 2:
            print("Imprimir:")
        elif opcao == 3:
            print("Saindo...")
            break  # O loop se encerra quando o usuário sai do programa
        else:
            print("Opção inválida. Tente novamente!")

def menu_principal():
    print("Seha bem vindo\nEste programa tem como finalidade gerar seu boletim de final de ano caso seja aluno\n Ou adicionar alunos, lançar as notas, frequências e revisar as médias caso seja professor! ")
    usuario = input("Você é aluno ou professor? ").upper()  # Recebe o tipo de usuário (professor ou aluno) #podemos fazer uma verificacao para er certeza que este cara é um professor
    if usuario == "PROFESSOR":
        menu_professor()  # Chama o menu do professor
    elif usuario == "ALUNO":
        menu_aluno()  # Chama o menu do aluno
    else:
            print("Esse usuário não existe. Tente novamente!")            

menu_principal()


  # Inicia o programa chamando o menu principal
