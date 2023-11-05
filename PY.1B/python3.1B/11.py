usuario_correto= "usuario123"
senha_correta="senha456"

usuario= input("Digiter seu usuario: ")
senha=input("Digite sua senha: ")

login_correto= (usuario == usuario_correto) and (senha == senha_correta)

if login_correto :
    print("Login bem-sucedido!") 
else :
   print("Nome de usuario ou senha incorreta")