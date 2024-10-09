from cadastrar import escolher_turma

def pesquisar_aluno():
    turma = escolher_turma()
    boletim_aluno = input("\n\nNome do aluno: ").upper()

    aluno_encontrado = ''

    try:
        with open(turma, "r", encoding='utf-8') as f:
            for linha in f:
                if boletim_aluno in linha.upper():  
                    aluno_encontrado = linha.strip()

    except FileNotFoundError:
            print("Arquivo da turma não encontrado.")


    if aluno_encontrado != '': 
        print(f"\n\nBoletim Anual: {aluno_encontrado}\n\n")
    else:
        print("Aluno não encontrado na turma.")

 
def pesquisar_turma():
    turma = escolher_turma()
    if turma:  
        nome_turma = turma.replace(".txt", "").upper()
        print(f"\n{nome_turma} localizada:\n\n")
            
        try:
            with open(turma, "r", encoding='utf-8') as f: 
                for linha in f: 
                    print(linha.strip())  
        except FileNotFoundError:
            print("Arquivo de turma não encontrado.")
    else:
        print("Nenhuma turma válida foi selecionada.")    

