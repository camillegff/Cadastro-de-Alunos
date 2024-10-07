# cadastrar: opção para adicionar (turma, nome e sobrenome).
def dados_aluno(): #captar dados do aluno
    print("Ola\n Cadestre o aluno")
    nome = input("Digite o nome do aluno: ").upper()
    sobrenome = input("Digite o sobrenome do aluno: ").upper()
    aluno = {
        "nome": nome,
        "sobrenome": sobrenome,
        "n1": "0",
        "n2": "0",
        "n3": "0",
        "media_notas":"0",
        "frequência":" ",#adicionar nota e frequencia
        "situação escolar":" ",# adicionar se passou ou não
    }
    return aluno

def escolher_turma():  # Opção de turma 
    TURMA = input("INFORME A TURMA:\n Turma [A] ou Turma [B]: ").upper()
    if TURMA == "A":
        return "turma-A.txt"  # nome do arquivo para a turma A
    elif TURMA == "B":
        return "turma-B.txt"  # nome do arquivo para a turma B
    else:
        print("Insira uma turma válida!")  # Mensagem de erro
        return None  # Retorna nada para entrada errada   

def add_novo_aluno():  # adicionar alunos na lista e salvar
    aluno = dados_aluno()
    path_file = escolher_turma()
    nome_turma = path_file.replace(".txt", "").replace("turma-", "").upper() 
    if path_file:  # Verifica se a turma é válida
        salvar_novo_aluno(path_file, **aluno)  # Salva o aluno no arquivo correspondente
        print(f"Aluno {aluno['nome']} adicionado com sucesso na turma {nome_turma}")  # Mensagem de confirmação
    else:
        print("Aluno não adicionado\nTurma inexistente!")  # Mensagem de erro
    
    
def salvar_novo_aluno(path_file, **kwargs):  # cria arquivo
    with open(path_file, 'a',encoding='utf-8') as file:
        total_items = len(kwargs)  # Número total de itens
        linha_aluno = ''
        for index, (chave, valor) in enumerate(kwargs.items()):
            linha_aluno += f"{chave}: {valor}"
            if index < total_items - 1:  # Se não for o último item, adiciona o separador '|'
                linha_aluno += ' | '
        file.write(linha_aluno + "\n")  # Adicionando os dados do aluno em uma linha
     

