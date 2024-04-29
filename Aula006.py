## dicionarios e estruturas de dados ##
dic_produtos = {"tv": 5000, "celular": 2500, "carro": 25000, "microfone": 950}

# Pegar um valor de uma chave dentro do dicionario
#print(dic_produtos["tv"])

# Editar um valor dentro de um dicionario
#dic_produtos["tv"] = dic_produtos["tv"] * 1.3 #nova chave = chave antiga vezes 1.3 ou 30%

# quantidade de itens
#print(len(dic_produtos))

# retirar um item do dicionario
#dic_produtos.pop("tv") #

# adicionar um item no dicionario
#dic_produtos["iphone"] = 6000

# Verificar se um item existe no dicionario
# if "tv" in dic_produtos:
#    print("Existe o produto.")
# else:
#    print("Não existe.")

# Verificar se um valor existe nos valores dos dicionario
#if 5000 in dic_produtos.values():
#    print("Existe, sim!")
#else:
#    print("Não existe.")

# nome_produto = input("Nome do produto: ")
# preco_produto = input("Preço do produto: ")

# nome_produto = nome_produto.lower()
# preco_produto = float(preco_produto)

# dic_produtos[nome_produto] = preco_produto
# print(dic_produtos)

# produto = "tv"

for produto in dic_produtos:
    novo_preco = dic_produtos[produto] * 1.1
    dic_produtos[produto] = novo_preco
print(dic_produtos)    

























