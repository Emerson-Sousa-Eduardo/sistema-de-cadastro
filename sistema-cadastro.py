
# SISTEMA DE CADASTRO EM PYTHON #

print("=" * 40)
print(" " * 10 + "Cadastre-se no sistema")
print("=" * 40)

# LOOP PARA CADASTRO DE EMAIL #
while True:
    email = input("Digite seu e-mail: ")

    # EXIGÊNCIAS DE VALIDAÇÃO DO EMAIL #
    if "@" and ".com" not in email:
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
    break

# MENSAGEM DE BOAS VINDAS #
nome = input("Digite o seu nome de usuário: ")
print("Cadastro realizado com sucesso!")
print(f"Bem-vindo(a), {nome}!")

# Criar sistema para salvamento de usuários
