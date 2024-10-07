import pesquisar as p

def menu_professor():
    while True:  # Termina quando o usuário escolher a opção sair
        opcao = int(input("\n[1]Cadastrar Aluno\n[2]Editar Aluno\n[3]Pesquisar\n[4]Visualizar Turma\n[5]Sair\n\nDigite uma opção: "))
        if opcao == 1:
            print("cadastrar:")  # Função que captura os dados do aluno
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
        opcao = int(input("\nMenu principal\n\n[1]Pesquisar por aluno\n[2]Gerar Boletim\n[3]Sair\n\nDigite uma opção: "))
        if opcao == 1:
            print("Pesquisar:")
            p.pesquisar()
        elif opcao == 2:
            print("Imprimir:")
        elif opcao == 3:
            print("Saindo...")
            break  # O loop se encerra quando o usuário sai do programa
        else:
            print("Opção inválida. Tente novamente!")

def menu_principal():
    print("\nSeja bem vindo :)\n\nEste programa tem como finalidade gerar seu boletim de final de ano caso seja aluno!\n\nCadastrar alunos, lançar as notas, frequências e revisar as médias caso seja professor!\n")
    usuario = input("Você é aluno ou professor? ").upper()  # Recebe o tipo de usuário (professor ou aluno) #podemos fazer uma verificacao para er certeza que este cara é um professor
    if usuario == "PROFESSOR":
        menu_professor()  # Chama o menu do professor
    elif usuario == "ALUNO":
        menu_aluno()  # Chama o menu do aluno
    else:
            print("Esse usuário não existe. Tente novamente!")            

menu_principal()
