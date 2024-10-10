from pesquisar import pesquisar  # Função para localizar aluno e turma

def editar_notas_ou_frequencia():
    aluno_encontrado, turma = pesquisar()  # Usa a função pesquisar para obter o aluno e a turma
    
    if aluno_encontrado:  # Verifica se o aluno foi encontrado antes de continuar
        editar_notas(turma, aluno_encontrado)  # Função para editar notas
        
        # Perguntar se deseja editar a frequência
        editar_freq = input("Deseja editar a frequência do aluno? (S/N): ").upper()
        if editar_freq == "S":
            editar_frequencia(turma, aluno_encontrado)
        else:
            print("Frequência não editada.")
    else:
        print("Aluno não encontrado. Não será possível editar notas ou frequência.")


def editar_notas(turma, aluno):
   
    with open(turma, 'r', encoding='utf-8') as f: #abre o arquivo da turma e lÊ os alunos
        linhas = f.readlines()
    
    for i, linha in enumerate(linhas):
        if aluno in linha:
            partes = linha.strip().split(' | ')
            aluno_dict = {}
            for parte in partes:
                if ': ' in parte:
                    chave, valor = parte.split(': ', 1)
                    aluno_dict[chave] = valor
                else:
                    print(f"Erro ao processar a parte: {parte}")
            
            # Editar notas
            for nota in ['n1', 'n2', 'n3']:
                if aluno_dict[nota] == '0':  # Se a nota estiver zerada
                    nova_nota = float(input(f"{nota.upper()} está zerada. Digite a nova nota (0-10): "))
                    if 0 <= nova_nota <= 10:
                        aluno_dict[nota] = str(nova_nota)
                    else:
                        print("Nota inválida. Deve ser entre 0 e 10.")
                else:
                    editar = input(f"{nota.upper()} já possui a nota {aluno_dict[nota]}. Deseja alterar? (S/N): ").upper()
                    if editar == 'S':
                        nova_nota = float(input(f"Digite a nova nota para {nota.upper()} (0-10): "))
                        if 0 <= nova_nota <= 10:
                            aluno_dict[nota] = str(nova_nota)
                        else:
                            print("Nota inválida. Deve ser entre 0 e 10.")
            
            # Calcular média
            aluno_dict["media_notas"] = (float(aluno_dict["n1"]) + float(aluno_dict["n2"]) + float(aluno_dict["n3"])) / 3
            print(f"Nova média: {aluno_dict['media_notas']:.2f}")
            
            # Atualizar a linha do aluno
            novas_informacoes = ' | '.join([f'{chave}: {valor}' for chave, valor in aluno_dict.items()])
            linhas[i] = novas_informacoes + '\n'

    
    # Escrever as atualizações no arquivo
    with open(turma, 'w', encoding='utf-8') as f:
        f.writelines(linhas)
    
    print(f"Notas do aluno {aluno_dict['nome']} atualizadas com sucesso!")

def editar_frequencia(turma, aluno):
    # Abrir o arquivo da turma e ler os alunos
    with open(turma, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
    
        for i, linha in enumerate(linhas):#percorre as linhas do arquivo, enumerando pra ter o índice e a linha
            if aluno == linha.split("\n")[0]: #verifica se o nome do aluno (variável 'aluno') está presente na linha
                partes = linha.strip().split(' | ')#divide a linha em partes 
                aluno_dict = {}#cria um dicionario vazio  guarda os dados do aluno
                for parte in partes:#percorre cada parte da lista partes
                    if ': ' in parte:#se tem : na parte
                        chave, valor = parte.split(': ', 1)#divide chave-valor no dicionário
                        aluno_dict[chave] = valor #salva chave-valor no dicionário
                
                # Editar frequência
                while True:
                    try:
                        nova_frequencia = float(input(f"Frequência atual: {aluno_dict['frequencia']}%. Digite a nova frequência (0-100): "))
                        if 0 <= nova_frequencia <= 100:
                            aluno_dict['frequencia'] = str(nova_frequencia)
                            break  # Se o valor for válido, saímos do loop
                        else:
                            print("Por favor, insira um número entre 0 e 100")
                    except ValueError:
                        print("Por favor, insira um número entre 0 e 100.")

                # Atualizando a situação escolar
                media = float(aluno_dict["media_notas"])
                frequencia = float(aluno_dict['frequencia'])
                if media >= 7 and frequencia >= 75:
                    aluno_dict["situacao_escolar"] = "Aprovado"
                else:
                    aluno_dict["situacao_escolar"] = "Reprovado"
                
                print(f"Situação escolar atualizada para: {aluno_dict['situacao_escolar']}")
                
                # Atualizar a linha do aluno
                novas_informacoes = ' | '.join([f'{chave}: {valor}' for chave, valor in aluno_dict.items()])
                linhas[i] = novas_informacoes + '\n'
                break
    
    # Atualiza no arquivo
    with open(turma, 'w', encoding='utf-8') as f:
        f.writelines(linhas)
    
    # print(f"Frequência do aluno {aluno_dict["nome"]} atualizada com sucesso!")

