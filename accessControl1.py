password = input("Digite a senha: ")

if password == "admin": #teste de comentário
    print("Bem vindo Admin")
elif password == "user":
    print("Bem vindo usuário")
else:
    print("Senha errada")

print("a senha digitada é: ", password)