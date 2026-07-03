print ("=" * 50)
print (" " * 10 + "Bem Vindo ao Sistema de Cadastro")
print ("=" * 50)

print("Escolha uma opção:")

# MENU DE OPÇÕES #
while True:
    try:
        print("1 - Criar uma nova conta")
        print("2 - Já possuo uma conta")
        print("3 - Sair do sistema")
        opcao = input("Digite a opção desejada: ")
    except ValueError:
        print("Digite uma opção válida.")
        continue

     # OPÇÃO DE CADASTRAR CONTA #
    if opcao == "1":
        print("=" * 50)
        print(" " * 10 + "Crie sua conta")
        print("=" * 50)

        # LOOP PARA CADASTRO DE EMAIL #
        while True:
            email = input("Digite seu e-mail: ")

          # EXIGÊNCIAS DE VALIDAÇÃO DO EMAIL #
            if "@" not in email or ".com" not in email:
                print("Digite um e-mail válido.")
                continue
            else:
                break

         # LOOP PARA CADASTRO DE SENHA #
        while True:    
            senha = input("Crie a sua senha: ")

          # EXIGÊNCIAS DE SEGURANÇA DA SENHA #
            if len (senha) < 6 and not "!@#*$%&" in senha:
                print("A senha deve ter no mínimo 6 caracteres e conter pelo menos um caractere especial.") 
                continue

         # LOOP PARA CONFIRMAÇÃO DE SENHA #
            confirm_senha = input("Confirme a sua senha: ")
            if senha != confirm_senha:
                print("As senhas não coincidem. Tente novamente.")
                continue
            else:
                break

         # MENSAGEM DE BOAS VINDAS #
        nome = input("Digite o seu nome de usuário: ")
        print("Cadastro realizado com sucesso!")
        print(f"Bem-vindo(a), {nome}!")

        arquivo = open("usuarios.txt", "a")
        arquivo.write(f"{email},{senha},{nome}\n")
        arquivo.close()

    elif opcao == "2":
        print("=" * 50)
        print(" " * 10 + "Faça o login do email e senha cadastrados")
        print("=" * 50)

        login_email = input("Digite o seu e-mail: ")
        login_senha = input("Digite a sua senha: ")

        arquivo = open("usuarios.txt", "r")
        for linha in arquivo:
            email_salvo, senha_salva, nome_salvo = linha.strip().split(",")
            if login_email == email_salvo and login_senha == senha_salva:
                print(f"Login realizado com sucesso! Bem-vindo(a), {nome_salvo}!")
                break
        else:
            print("E-mail ou senha incorretos. Tente novamente.")
                #COLOCR LOOP PARA VERIFICAR SE ESTÁ CORRETO#
        arquivo.close()
        
    elif opcao == "3":
        print("Saindo do sistema...")
        break

















# Criar sistema para salvamento de usuários
