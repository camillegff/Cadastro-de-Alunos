from cadastrar import escolher_turma

def pesquisar():
    turma = escolher_turma()
    boletim_aluno = input("Informe seu nome para consultar seu boletim: ").upper()

    aluno_encontrado = None

    with open(turma, "r") as f:
        for linha in f:
            if boletim_aluno in linha.upper():  
                aluno_encontrado = linha.strip()
                break


    if aluno_encontrado:
        print(f"Boletim Anual: {aluno_encontrado}")  
    else:
        print("Aluno não encontrado.") 

    opcao = int(input("\n\nParece que sua busca foi bem sucedida :)\nPor favor, me informe uma das três opções de acordo com seu desejo:\n[1]continuar a busca\n[2]sair\n[3]editar dados"))
    while True:
        if opcao == 1:
            return pesquisar
        elif opcao == 2:
            print("Busca encerrada.")
            break
        elif opcao == 3:
            print("função editar")
        else:
            print("Opção inválida. Tente novamente!")

pesquisar()

