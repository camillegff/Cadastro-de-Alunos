def add_nota_freq(path_file, **kwargs):
    dicionario = {}
    nota1 = float(input("Digite a Nota 1: "))
    nota2 = float(input("Digite a Nota 2: "))
    nota3 = float(input("Digite a Nota 3: "))
    media_notas = (nota1 + nota2 + nota3) /3
    frequencia = int(input("Informe a frequência do aluno (%): "))

    with open(path_file,"r", encoding='utf-8' ) as f:
        line = f.readlines()[-1]#pegar a ultima linha
        partes = line.split(' | ')

        for parte in partes:
            chave, valor = parte.split(': ')
            # Se a chave já existe, transforma o valor em uma lista
            dicionario[chave] = valor

    
    if media_notas <= 5 and frequencia < 75:
        dicionario["situação escolar"] = "Reprovado"
    elif media_notas >= 6 and frequencia > 75:
        dicionario["situação escolar"] = "Aprovado"


    dicionario["n1"] = nota1
    dicionario["n2"] = nota2
    dicionario["n3"] = nota3
    dicionario["media_notas"] = media_notas
    dicionario["frequência"] = frequencia


    return dicionario




