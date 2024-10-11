from clearterminal import limpar_terminal
from pesquisar import pesquisar  # Função para localizar aluno e turma

def editar_notas_ou_frequencia():
    aluno_encontrado, turma = pesquisar()  # Usa a função pesquisar para obter o aluno e a turma

    if aluno_encontrado:  # Verifica se o aluno foi encontrado antes de continuar
        aluno_dict = editar_notas(turma, aluno_encontrado)  # Função para editar notas
        
        # Perguntar se deseja editar a frequência
        editar_freq = input("Deseja editar a frequência do aluno? (S/N): ").upper()
        while editar_freq not in ["S", "N"]:  # Garantir que o input seja "S" ou "N"
            editar_freq = input("Entrada inválida. Deseja editar a frequência do aluno? (S/N): ").upper()
        
        if editar_freq == "S":
            editar_frequencia(turma, aluno_dict)  # Passar aluno_dict atualizado
        else:
            print("Frequência não editada.")
    else:
        print("Aluno não encontrado. Não será possível editar notas ou frequência.")
limpar_terminal()        

def editar_notas(turma, aluno):
    with open(turma, 'r', encoding='utf-8') as f:  # Abre o arquivo da turma e lê os alunos
        linhas = f.readlines()
    
    aluno_dict = None  # Inicializa a variável para o dicionário do aluno

    for i, linha in enumerate(linhas):
        if aluno in linha:  # Encontra o aluno na linha
            partes = linha.strip().split(' | ')
            aluno_dict = {parte.split(': ')[0]: parte.split(': ')[1] for parte in partes if ': ' in parte}
            break  # Sai do loop assim que o aluno é encontrado

    if aluno_dict is None:  # Verifica se o aluno foi encontrado
        print("Aluno não encontrado. Não é possível editar notas.")
        return  # Retorna para não prosseguir se o aluno não for encontrado

    # Editar notas
    for nota in ['n1', 'n2', 'n3']:
        if aluno_dict[nota] == '0':  # Se a nota estiver zerada
            nova_nota = input(f"{nota.upper()} está zerada. Digite a nova nota (0-10): ")
            while not validar_nota(nova_nota):
                nova_nota = input(f"Digite novamente a nova nota para {nota.upper()} (0-10): ")
            aluno_dict[nota] = nova_nota
        else:
            editar = input(f"{nota.upper()} já possui a nota {aluno_dict[nota]}. Deseja alterar? (S/N): ").upper()
            while editar not in ["S", "N"]:
                editar = input("Entrada inválida. Deseja alterar a nota? (S/N): ").upper()
            if editar == 'S':
                nova_nota = input(f"Digite a nova nota para {nota.upper()} (0-10): ")
                while not validar_nota(nova_nota):
                    nova_nota = input(f"Digite novamente a nova nota para {nota.upper()} (0-10): ")
                aluno_dict[nota] = nova_nota
    
    # Calcular média e formatar com 2 casas decimais
    aluno_dict["media_notas"] = round(calcular_media(aluno_dict), 2)
    print(f"Nova média: {aluno_dict['media_notas']:.2f}")
    
    # Atualizar a linha do aluno
    novas_informacoes = ' | '.join([f'{chave}: {valor}' for chave, valor in aluno_dict.items()])
    linhas[i] = novas_informacoes + '\n'

    # Escrever as atualizações no arquivo
    with open(turma, 'w', encoding='utf-8') as f:
        f.writelines(linhas)
    
    print(f"Notas do aluno {aluno_dict['nome']} atualizadas com sucesso!")
    return aluno_dict  # Retorna o dicionário atualizado


def validar_nota(nota):
    try:
        nota_float = float(nota)
        return 0 <= nota_float <= 10
    except ValueError:
        return False

def calcular_media(aluno_dict):
    return (float(aluno_dict["n1"]) + float(aluno_dict["n2"]) + float(aluno_dict["n3"])) / 3

def atualizar_situacao_escolar(aluno_dict):
    media = float(aluno_dict["media_notas"])
    frequencia = float(aluno_dict['frequencia'])
    aluno_dict["situacao_escolar"] = "Aprovado" if media >= 7 and frequencia >= 7 else "Reprovado"
    print(f"Situação escolar atualizada para: {aluno_dict['situacao_escolar']}")

def validar_frequencia(frequencia):
    try:
        frequencia_float = float(frequencia)
        return 0 <= frequencia_float <= 100
    except ValueError:
        return False

def editar_frequencia(turma, aluno_dict):
    with open(turma, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
    
    for i, linha in enumerate(linhas):
        if aluno_dict['nome'] in linha:  # Verifica se o aluno está na linha
            partes = linha.strip().split(' | ')
            aluno_dict = {parte.split(': ')[0]: parte.split(': ')[1] for parte in partes if ': ' in parte}
            break  # Sai do loop assim que o aluno é encontrado

    if aluno_dict is None:  # Verifica se o aluno foi encontrado
        print("Aluno não encontrado para editar a frequência.")
        limpar_terminal()
        return

    while True:  # Loop para garantir que a frequência seja válida
        nova_frequencia = input(f"Frequência atual: {aluno_dict['frequencia']}%. Digite a nova frequência (0-100): ")
        
        # Validação da nova frequência
        if validar_frequencia(nova_frequencia):
            aluno_dict['frequencia'] = str(int(float(nova_frequencia)))  # Salvar como número inteiro
            print(f"Frequência atualizada para: {aluno_dict['frequencia']}%.")
            limpar_terminal()
            break  # Sai do loop se a entrada for válida
        else:
            print("Por favor, insira um número válido entre 0 e 100.")
    
    # Atualizando a situação escolar
    atualizar_situacao_escolar(aluno_dict)

    # Atualizar a linha do aluno
    novas_informacoes = ' | '.join([f'{chave}: {valor}' for chave, valor in aluno_dict.items()])
    linhas[i] = novas_informacoes + '\n'
    
    with open(turma, 'w', encoding='utf-8') as f:
        f.writelines(linhas)
    
    print(f"Frequência do aluno {aluno_dict['nome']} atualizada com sucesso!")
    limpar_terminal()