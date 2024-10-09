def usuario_senha():  # Função para verificar a senha do professor
    try:
        with open('senhas.txt', 'r') as arquivo:
            senha_arquivo = arquivo.readline().strip()  # Lê a única linha do arquivo que contém a senha

            tentativas = 0
            while tentativas < 3:
                senha = input("Olá professor :)\nDigite a sua senha: ")

                if senha == senha_arquivo:  # Compara a senha fornecida com a senha no arquivo
                    print("Acesso concedido.")
                    return True  # Acesso permitido se a senha estiver correta

                tentativas += 1
                print(f"Senha incorreta. Tentativas restantes: {3 - tentativas}")

            # Se o número de tentativas for excedido
            print("Tentativas excedidas. Acesso negado.")
            return False

    except FileNotFoundError:
        print("Arquivo de senhas não encontrado.")
        return False
