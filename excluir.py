#criar funcao excluir

from pesquisar import pesquisar  # Importa a função de pesquisa para buscar aluno

def excluir_aluno():
    print("\n\nExcluir aluno\n\n")
    aluno_encontrado, turma = pesquisar()  #pesquisar para encontrar o aluno e a turma
    nome_aluno = aluno_encontrado.split(" | ")[0].split(": ")[1]
    if aluno_encontrado:  # Verifica se o aluno foi encontrado
        print(f"\nDeseja excluir o aluno {nome_aluno} da turma {turma.replace('.txt', '').upper()}?")
        confirmacao = input("Digite S para confirmar ou N para cancelar: ").upper()
        
        if confirmacao == 'S':
            #excluir
            with open(turma, 'r', encoding='utf-8') as f:
                linhas = f.readlines() #lê as linhas 
            
            with open(turma, 'w', encoding='utf-8') as f:
                for linha in linhas:
                    if aluno_encontrado['nome'] not in linha and aluno_encontrado['sobrenome'] not in linha:
                        f.write(linha)

            
            print(f"Aluno {nome_aluno} foi excluído com sucesso!")
        else:
            print("Operação cancelada.")
    else:
        print("Aluno não encontrado")


