print("\nMENU INICIAL\n Olá, seja bem vindo!")


def opcao_usuario(): 
    while True: #looping continua até uma opção válida for imformada
        usuario = input("Voce é aluno ou professor? ")
        if usuario in ["professor", "aluno"]: #verifica se a variavel usuario está na lista   
            return usuario #retorna quando a variavel armazenar o valor correto, assim encerrando o looping

def menu_professor():
    while True:  #termina quando o usuário escolher a opção sair
        opcao = int(input("\n[1] adicionar\n[2] editar\n[3] pesquisar\n[4] imprimir\n[5] sair\n ")) 
        if opcao == 1:
            print("Adicionar:")
        elif opcao == 2:
            print("Editar:")
        elif opcao == 3:
                print("Pesquisar:")
        elif opcao == 4:
                print("Imprimir:")
        elif opcao == 5:
            print("Saindo...")
            break #o looping se encerra quando o usuário sai do progchrama
        else:
            print("Opção inválida. Tente novamente!")

def menu_aluno():
    while True: #termina quando o usuário escolher a opção sair
        opcao = int(input("\n[1] pesquise\n[2] imprimir\n[3] sair\n "))
        if opcao == 1:
            print("Pesquisar:")
        elif opcao == 2:
            print("Imprimir:")
        elif opcao == 3:
            print("Saindo...")
            break #o looping se encerra quando o usuário sai do programa
        else:
            print("Opção inválida. Tente novamente!")

def menu_principal():
    usuario = opcao_usuario() #salva a função na variavel usuário
    if usuario == "professor":
        menu_professor() 
    elif usuario == "aluno": 
        menu_aluno()

menu_principal() #retorna a funcao de menu principal para rodar o programa

        
    

    
   
