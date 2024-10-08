from cadastrar import escolher_turma

def pesquisar_aluno():
    turma = escolher_turma()
    boletim_aluno = input("\n\nNome do aluno: ").upper()

    if aluno_encontrado: 
        print(f"\n\nBoletim Anual: {aluno_encontrado}\n\n")
        try:
            with open(turma, "r", encoding='utf-8') as f:
                for linha in f:
                    if boletim_aluno in linha.upper():  
                            aluno_encontrado = linha.strip()
        except:
            print("Aluno não encontrado.")

 
def pesquisar_turma():# funcao do menu professor para imprimir a turma
    turma = escolher_turma()
    if turma:  
        nome_turma = turma.replace(".txt", "").upper()
        print(f"\n{nome_turma} localizada:\n\n")
            
        try:
            with open(turma, "r", encoding='utf-8') as f:  # Abre o arquivo da turma
                for linha in f:  # percorre linhas do arquivo
                    print(linha.strip())  # Exibe as linhas, tira espaços em branco
        except FileNotFoundError:
            print("Arquivo de turma não encontrado.")
    else:
        print("Nenhuma turma válida foi selecionada.")    

