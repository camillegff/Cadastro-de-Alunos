from cadastrar import escolher_turma

def pesquisar():
    turma = None
    while True:
        turma = escolher_turma()
        if turma:
            try:
                print(f"\n{turma} localizada\n\n")
                break
            except FileNotFoundError:
                print("Turma não encontrada. Tente novamente.")
        else:
            print("Nenhuma turma escolhida.")
        
    boletim_aluno = input("\n\nNome do aluno: ").upper()
    alunos_encontrados = []  # Lista para armazenar todos os alunos encontrados

    try:
        with open(turma, "r", encoding='utf-8') as f:
            for linha in f:
                if boletim_aluno in linha.upper():  # Verifica se o nome está na linha
                    alunos_encontrados.append(linha.strip())  # Adiciona à lista de alunos encontrados
    except FileNotFoundError:
        print("Erro ao abrir a turma. Verifique se o arquivo existe.")
        return None, turma

    # Verifica a quantidade de alunos encontrados
    if len(alunos_encontrados) == 0:
        print("Aluno não encontrado.")
        return None, turma  # Retorna None se não encontrar o aluno
    elif len(alunos_encontrados) == 1:
        aluno_encontrado = alunos_encontrados[0]
        print(f"\n\nBoletim Anual: {aluno_encontrado}\n\n")
    else:
        print("Existem mais de um aluno com este nome na turma:\n")
        sobrenome = input("Informe o sobrenome do aluno: ").upper()
        aluno_encontrado = None

        # Verifica se o sobrenome corresponde a algum aluno encontrado
        for aluno in alunos_encontrados:
            if sobrenome in aluno.upper():
                aluno_encontrado = aluno
                break

        if aluno_encontrado:
            print(f"\n\nBoletim Anual: {aluno_encontrado}\n\n")
        else:
            print("Ocorreu um erro ao localizar o aluno.")  
            return None, turma  # Retorna None se não encontrar o aluno

    return aluno_encontrado, turma  # Retorna o aluno encontrado e a turma

def pesquisar_turma():
    print("\n\nPesquisar turma\n\n")
    turma = escolher_turma() 
    nome_turma = turma.replace(".txt", "").upper()
    
    if turma:
        try:
            print(f"\n{nome_turma} localizada\n\n")
            with open(turma, "r", encoding='utf-8') as f:
                for linha in f:
                    print(linha.strip())
        except FileNotFoundError:
            print("Turma não encontrada. Tente novamente.")
    else:
        print("Nenhuma turma válida foi selecionada.")
