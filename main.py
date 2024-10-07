import pesquisar as p
import cadastrar as add

def menu_professor():
    while True:  # Termina quando o usuário escolher a opção sair
        opcao = int(input("\n[1]Cadastrar Aluno\n[2]Editar Aluno\n[3]Pesquisar aluno\n[4]Visualizar Turma\n[5]Excluir aluno\n[6]Sair\n\nDigite uma opção: "))
        if opcao == 1:
            add.add_novo_aluno() #pronto 
        elif opcao == 2:
            print("Editar:")
        elif opcao == 3:
            p.pesquisar()#PESQUISAR POR ALUNO
        elif opcao == 4:
            p.pesquisar_turma()
        elif opcao == 5:
            print("Excluir:") 
        elif opcao == 6:
            print("Saindo...")
            print("programa finalizado")
            break  # O loop se encerra quando o usuário sai do programa #pronto
        else:
            print("Opção inválida. Tente novamente!")

def menu_aluno(): #pronto
    while True:  # Termina quando o usuário escolher a opção sair
        opcao = int(input("\nMenu principal\n\n[1]Gerar Boletim\n[2]Sair\n\nDigite uma opção: "))# pesquisar está sendo chamado em gerar boletim
        if opcao == 1:
            print("Pesquisar:")
            p.pesquisar()
        elif opcao == 2:
            print("Saindo...")
            print("programa finalizado")
            break  # O loop se encerra quando o usuário sai do programa
        else:
            print("Opção inválida. Tente novamente!")

def menu_principal():
    print("\nSeja bem vindo :)\n\nEste programa tem como finalidade gerar seu boletim de final de ano caso seja aluno!\n\nCadastrar alunos, lançar as notas, frequências e revisar as médias caso seja professor!\n")
    usuario = input("Você é aluno ou professor? ").upper()  # Recebe o tipo de usuário (professor ou aluno) #podemos fazer uma verificacao para er certeza que este cara é um professor
    if usuario == "PROFESSOR":
        senha_acesso = ""
        menu_professor()  # Chama o menu do professor
    elif usuario == "ALUNO":
        menu_aluno()  # Chama o menu do aluno
    else:
            print("Esse usuário não existe. Tente novamente!")            

menu_principal()
