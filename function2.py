# cadastrar: opção para adicionar (turma, nome e sobrenome).



def dados_aluno(): #captar dados do aluno
    print("Ola\n Cadestre o aluno")
    nome = input("Digite o nome do aluno: ").upper()
    sobrenome = input("Digite o sobrenome do aluno: ").upper()
    aluno = {
        "nome": nome,
        "sobrenome": sobrenome 
    }
    return aluno

def escolher_turma():  # Opção de turma 
    TURMA = input("Informe a que turma o aluno está matriculado\n turma [A] ou turma [B]: ").upper()
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
    if path_file:  # Verifica se a turma é válida
        salvar_novo_aluno(path_file, **aluno)  # Salva o aluno no arquivo correspondente
        print(f"Aluno adicionado: {aluno}")  # Mensagem de confirmação
    else:
        print("Aluno não adicionado devido a erro na seleção da turma.")  # Mensagem de erro
    print(f"Aluno adicionado: {aluno}")
    
def salvar_novo_aluno(path_file, **kwargs):  # cria arquivo
    with open(path_file, 'a') as file:
        linha_aluno = '|'.join([f"{chave}: {valor}" for chave, valor in kwargs.items()])
        file.write(linha_aluno + "\n")  # Adicionando os dados do aluno em uma linha
    
            
def add_nota():
    nota1 = float(input("Digite a Nota 1: "))
    nota2 = float(input("Digite a Nota 2: "))
    nota3 = float(input("Digite a Nota 3: "))
    media_notas = (nota1 + nota2 + nota3) / 3

def add_freqencia():
    freq1 = float(input("Digite a Frequência 1 (em %): "))
    freq2 = float(input("Digite a Frequência 2 (em %): "))
    freq3 = float(input("Digite a Frequência 3 (em %): "))
    media_frequencia = (freq1 + freq2 + freq3) / 3        
    
            


add_novo_aluno()

    