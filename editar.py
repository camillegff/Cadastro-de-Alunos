import cadastrar as add

def editar_notas_menu():
    turma = add.escolher_turma()
    
    if turma:
        nome_aluno = input("Informe o nome do aluno que deseja editar as notas: ").upper()
        editar_notas(turma, nome_aluno)
    else:
        print("Nenhuma turma válida foi selecionada.")     
        
        
        

def add_nota(path_file, nome_aluno):
    
    dicionario = {}
    nota1 = float(input("Digite a Nota 1: "))
    nota2 = float(input("Digite a Nota 2: "))
    nota3 = float(input("Digite a Nota 3: "))
    media_notas = (nota1 + nota2 + nota3) /3

    with open(path_file,"r", encoding='utf-8' ) as f:
        line = f.readlines()[-1]#pegar a ultima linha
        partes = line.split(' | ')

        for parte in partes:
            chave, valor = parte.split(': ')
            # Se a chave já existe, transforma o valor em uma lista
            dicionario[chave] = valor

    dicionario["n1"] = nota1
    dicionario["n2"] = nota2
    dicionario["n3"] = nota3
    dicionario["media_notas"] = media_notas


add_nota()   