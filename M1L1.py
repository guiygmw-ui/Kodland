meme_dict = {
    "CRINGE": "Algo vergonhoso ou constrangedor",
    "STALKEAR": "Investigar a vida de alguém online",
    "VDD": "Abreviação da palavra verdade",
    "BISCOITAR": "Postar algo apenas para chamar atenção",
    "HATER": "Pessoa que critica os outros o tempo todo",
    "VLW": "Abreviação da palavra valeu"
}

print("Dicionário de Gírias Modernas")
print("--------------------------------")

for i in range(5):
    word = input("Digite uma palavra em MAIÚSCULO: ")

    if word in meme_dict.keys():
        print("Significado:", meme_dict[word])
    else:
        print("Essa palavra não está no dicionário!")

    print()
