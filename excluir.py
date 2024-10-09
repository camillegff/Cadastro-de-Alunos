#criar funcao excluir
from cadastrar import escolher_turma

def excluir_aluno():
    turma = escolher_turma()
    
    listar_alunos(turma)
    alunos = retorne_lista_alunos(turma)
    aluno = int(input("Número do aluno que deseja excluir: "))

    if aluno < 0 or aluno >= len(alunos):
        print("Número inválido.")
        return
    
    
    alunos_update = []

    with open(turma, "r", encoding='utf-8') as f:
        linhas = f.readlines()
        for linha in linhas:
            try:
                if linha.split(": ")[1].split(" | ")[0] == alunos[aluno]["nome"]:
                    pass
                else:
                    alunos_update.append(linha)
            except IndexError:
                print("Erro ao acessar linha.")

    #print(alunos_update)

    with open(turma, "w", encoding='utf-8') as f:
        for aluno in alunos_update:
            f.write(aluno)

    
                         
def listar_alunos(path_file):
    alunos = []
    with open(path_file, 'r', encoding='utf-8') as file:
        for linha in file:
            alunos = []
            campos = linha.strip().split(' | ')
            for i, campo  in enumerate(campos):
                if i == len(campos) - 1:
                    pass

                else:
                    chave, valor = campo.split(': ')
                    aluno[chave] = valor

            alunos.append(aluno)

    for i,aluno in enumerate(alunos):
        print(f"{i} - {aluno}")

def retorne_lista_alunos(path_file):
    alunos = []
    with open(path_file, 'r', encoding='utf-8') as file:
        for linha in file:
            aluno = {}                                               
            campos = linha.strip().split(' | ')
            for i, campo  in enumerate(campos):
                if i == len(campos) - 1:
                    pass
                else:
                    chave, valor = campo.split(': ')
                    aluno[chave] = valor
            alunos.append(aluno)

    return alunos

excluir_aluno()