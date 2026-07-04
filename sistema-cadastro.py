# SISTEMA DE CADASTRO DE USUÁRIOS #
# O sistema permite que os usuários criem uma conta, façam login e armazenem seus dados em um arquivo de texto. O sistema também valida o e-mail e a senha do usuário durante o cadastro.
# FORAM UTILZADAS ESTRUTURAS DE REPETIÇÃO, CONDIÇÕES E TRATAMENTO DE ERROS PARA GARANTIR A FUNCIONALIDADE DO SISTEMA.


# MENSAGEM DE BOAS VINDAS #
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
        print("Certifique-se de digitar apenas números.")
        continue

     # OPÇÃO DE CADASTRAR CONTA #
    if opcao == "1":
        print("=" * 50)
        print(" " * 18 + "Crie sua conta")
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

         # MENSAGEM DE BOAS VINDAS APÓS CADASTRO DE CONTA #
        nome = input("Digite o seu nome de usuário: ")
        print("Cadastro realizado com sucesso!")
        print(f"Bem-vindo(a), {nome}!")

        # SALVANDO OS DADOS DO USUÁRIO EM UM ARQUIVO DE TEXTO #
        arquivo = open("usuarios.txt", "a")
        arquivo.write(f"{email},{senha},{nome}\n")
        arquivo.close()

    # OPÇÃO DE LOGIN #
    elif opcao == "2":
        print("=" * 50)
        print(" " * 13 + "Faça o login da sua conta")
        print("=" * 50)
        
        # LOOP PARA LOGIN DE USUÁRIO #
        while True:
            login_email = input("Digite o seu e-mail: ")
            login_senha = input("Digite a sua senha: ")

            # VERIFICAÇÃO DE LOGIN EM ARQUIVO #
            arquivo = open("usuarios.txt", "r")
            for linha in arquivo:
                email_salvo, senha_salva, nome_salvo = linha.strip().split(",")
                if login_email == email_salvo and login_senha == senha_salva:
                    print(f"Login realizado com sucesso! Bem-vindo(a), {nome_salvo}!")
                    break
                else:
                    print("E-mail ou senha incorretos. Tente novamente.")
                    continue
            arquivo.close()

    # OPÇÃO DE SAIR DO SISTEMA #    
    elif opcao == "3":
        print("Saindo do sistema...")
        break

    # TRATAMENTO DE OPÇÃO INVÁLIDA #
    else:
        print("Opção inválida. Digite uma opção válida.")
        continue
