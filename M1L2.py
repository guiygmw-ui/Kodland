import random

# Caracteres possíveis
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# Comprimento da senha
tamanho = int(input("Digite o comprimento da senha: "))

# Senha gerada
senha = ""

# Gera a senha
for i in range(tamanho):
    senha += random.choice(caracteres)

# Exibe a senha
print("Senha gerada:", senha)
