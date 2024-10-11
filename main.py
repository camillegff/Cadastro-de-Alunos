import pesquisar as p
import cadastrar as add
import editar as edit
import excluir as dell
from clearterminal import limpar_terminal
from acesso import usuario_senha 

def menu_professor():
    limpar_terminal()
    while True:  # Termina quando o usuário escolher a opção sair
        print("Bem-vindo ao menu do professor.\n\nSelecione uma opção:")
        opcao = input("\n[1]Cadastrar Aluno\n[2]Editar Aluno\n[3]Pesquisar aluno\n[4]Visualizar Turma\n[5]Excluir aluno\n[6]Sair\n\nDigite uma opção: ")
        limpar_terminal()
        if opcao == "1":
            add.add_novo_aluno() #pronto  
        elif opcao == "2":
            edit.editar_notas_ou_frequencia()
        elif opcao == "3":
            p.pesquisar()#PESQUISAR POR ALUNO
        elif opcao == "4":
            p.pesquisar_turma()#PESQUISAR POR TURMA
        elif opcao == "5":
            dell.excluir_aluno()
        elif opcao == "6":
            print("Saindo...")
            print("programa finalizado")
            break  # O loop se encerra quando o usuário sai do programa #pronto
        else:
            print("Opção inválida. Tente novamente!")

def menu_aluno(): #pronto
    limpar_terminal()
    
    while True:  # Termina quando o usuário escolher a opção sair
        print("Bem-vindo ao menu do aluno.\n\nSelecione uma opção:\n")
        opcao = input("\nMenu principal\n\n[1]Gerar Boletim\n[2]Sair\n\nDigite uma opção: ")# pesquisar está sendo chamado em gerar boletim
        limpar_terminal()
        if opcao == "1":
            p.pesquisar()
        elif opcao == "2":
            print("Saindo...")
            print("programa finalizado")
            break  # O loop se encerra quando o usuário sai do programa
        else:
            print("Opção inválida. Tente novamente!")

def menu_principal():#pronto
    print("\nSeja bem vindo :)\n\nEste programa tem como finalidade gerar seu boletim de final de ano caso seja aluno!\n\nCadastrar alunos, lançar as notas, frequências e revisar as médias caso seja professor!\n")
    usuario = input("Você é aluno ou professor? ").upper()  # Recebe o tipo de usuário (professor ou aluno) #podemos fazer uma verificacao para er certeza que este cara é um professor
    limpar_terminal()
    if usuario == "PROFESSOR":
        if usuario_senha():
            menu_professor()
        else:
            print("Você não tem permição para acessar este usuário")    
    elif usuario == "ALUNO":
        menu_aluno()  # Chama o menu do aluno
    else:
            print("Esse usuário não existe. Tente novamente!")            

menu_principal()