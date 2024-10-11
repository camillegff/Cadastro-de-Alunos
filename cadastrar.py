from clearterminal import limpar_terminal
# cadastrar: opção para adicionar (turma, nome e sobrenome).
def dados_aluno():  # Captar dados do aluno
    print("\nMENU CADASTRO")
    nome = input("\nDigite o nome do aluno: ").upper()
    sobrenome = input("\nDigite o sobrenome do aluno: ").upper()
    aluno = {
        "nome": nome,
        "sobrenome": sobrenome,
        "n1": 0,
        "n2": 0,
        "n3": 0,
        "media_notas": 0,
        "frequencia": 0,  # Adicionar um valor padrão válido como '0'
    }
    return aluno

def escolher_turma():  # Opção de turma 
    while True:
        TURMA = input("INFORME A TURMA:\n Turma [A] ou Turma [B]: ").upper()
        if TURMA == "A":
            return "turma-A.txt"  # nome do arquivo para a turma A
        elif TURMA == "B":
            return "turma-B.txt"  # nome do arquivo para a turma B
        else:
            print("Insira uma turma válida!")
     

def add_novo_aluno():  # adicionar alunos na lista e salvar
    aluno = dados_aluno()
    path_file = escolher_turma()
    nome_turma = path_file.replace(".txt", "").replace("turma-", "").upper() 
    if path_file:  # Verifica se a turma é válida
        salvar_novo_aluno(path_file, **aluno)  # Salva o aluno no arquivo correspondente
        print(f"\nAluno {aluno['nome']} adicionado com sucesso na turma {nome_turma}")  # Mensagem de confirmação
        limpar_terminal()

    else:
        print("\nAluno não adicionado\nTurma inexistente!")  # Mensagem de erro
        limpar_terminal()
    
    
def salvar_novo_aluno(path_file, **kwargs):  # cria arquivo
    with open(path_file, 'a',encoding='utf-8') as file:
        total_items = len(kwargs)  # Número total de itens
        linha_aluno = ''
        for index, (chave, valor) in enumerate(kwargs.items()):
            linha_aluno += f"{chave}: {valor}"
            if index < total_items - 1:  # Se não for o último item, adiciona o separador '|'
                linha_aluno += ' | '
        file.write(linha_aluno + "\n")  # Adicionando os dados do aluno em uma linha
     

