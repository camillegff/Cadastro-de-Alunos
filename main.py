
print("\nMENU INICIAL\n Olá, seja bem vindo!")

while True:
    usuario= input("Voce é aluno ou professor? ")
    if usuario == "professor" or usuario == "aluno":
        break
    else:
        print("Opção Inválida. Tente novamente!")    
        
        if usuario == "professor":
            opcao_professor = int(input("\n[1] adicione\n[2] edite\n[3] pesquise\n[4] imprimir\n[5] sair"))
            print(opcao_professor)

        elif usuario == "aluno":
            opcao_aluno = int(input("\n[1] pesquise\n[2] imprimir\n[3] sair "))
            print(f"Você escolheu a opcao: {opcao_aluno}")
   
    

    
   


# if opcao == "aluno":
#  print("Opções para alunos: pesquisar, visualizar ou sair")

# opcao = input("Informe se você é professor ou aluno: ")

# def usuarios():
#     if os.path.exists("cadastro.txt"):


#         variaveis_carregadas = carregar_variaveis("cadastro.txt")

#         if variaveis_carregadas:

#            
#             elif opcao == "professor":



#fazer depois
# def salvar_variaveis(path_file, **kwargs): #criei a função salvar variavel para salvar o nome do aluno quando ele pesquisar no boletim
#     with open(path_file, 'w') as s:
#         for chave, valor in kwargs.items():
#             s.write(f"{chave}: {valor}\n")

# def carregar_variaveis(path_file):
#     variaveis = {}
#     with open(path_file, 'r') as f:
#         for line in f:
#             chave, valor = line.strip().split(': ')
#             variaveis[chave] = valor
#     return variaveis