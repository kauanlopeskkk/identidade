import getpass
SENHA_CORRETA = "Allany"
Nome = "Kauan"
while True:
    try:
        senha = input("Digite a senha: ")

        if senha == SENHA_CORRETA and senha.isalpha():
            print(f"{senha}: essa senha está correta (Somente Letras)")
            print(f"Ola {Nome}: seja bem vindo ao overwatch ")
            break  

        elif not senha.isalpha():
            raise ValueError("Senha Incorreta: não use números e símbolos")

        elif senha !=SENHA_CORRETA:
            print(f"{senha}: essa senha está incorreta (Letras estão corretas, mas a senha não confere)")

    except ValueError as erro:
        print(f"Erro: {erro}")



