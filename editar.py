def add_nota(path_file, **kwargs):
    dicionario = {}
    nota1 = float(input("Digite a Nota 1: "))
    nota2 = float(input("Digite a Nota 2: "))
    nota3 = float(input("Digite a Nota 3: "))
    media_notas = (nota1 + nota2 + nota3) /3

    with open(path_file,"r") as f:
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