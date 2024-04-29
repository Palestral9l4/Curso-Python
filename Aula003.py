##imputs e listas##
# input serve pra coletar dados

email = input("Escreva seu e-mail: ")
nome = input("Seu primeiro nome: ")
sobrenome = input("Seu sobrenome: ")
print(email, nome, sobrenome)

faturamento = float(input("Escreva o faturamento: ")) #função float serve para deixar o input como numero com casa decimal e int para numeros inteiros(só assim da para trabalhar com numeros)
imposto = faturamento * 0.1
print(imposto)
print(f"{nome} {sobrenome}, verifique seu email: {email} que enviamos um link de confirmação.") # O f serve para formatar e inserir variaveis dentro, pode conter numeros ou não
 

##listas##
vendas = [100, 50, 25, 150, 1000, 1500, 7900]
# sum usado para soma dos elementos dentro de uma lista
total_de_vendas = sum(vendas)
print(total_de_vendas)

#len usado para ver a quantidade de elementos que tem em uma lista
quantidades_de_vendas = len(vendas) #ou seja, criar uma variavel "quantidades de vendas" e puxar da lista de vendas para ter o resultado
print(quantidades_de_vendas)

#max e min são usado para saber o maior numero e o menor
print(max(vendas))
print(min(vendas))

# Pegar posição de um item em uma lista - sempre em [0] para o primeiro item ou[-1] para o ultimo
print(vendas[0])

# Verificar se existe um elemento em uma lista
lista_de_produtos = ["iphone", "airpod", "ipad" "macbook"]
print("apple watch" in lista_de_produtos) #ou seja "nome do elemento" in(na) "nome da variavel"
produto_procurado = input("Pesquise pelo nome do produto: ")

#formatar as letras de pesquisa para n conter erro na hora de encontrar o produto
produto_procurado = produto_procurado.lower() 
print(produto_procurado in lista_de_produtos)

# Adicionar um item a lista
lista_de_produtos.append("tv")
print(lista_de_produtos)

# Remover um item
lista_de_produtos.pop(0)
print(lista_de_produtos)

# Editar um item
precos = [200, 300 ,500 ,7941]
precos[0] = 199 #colocando o indice e o valor ja da pra mudar
#ou
precos[0] = precos[0] * 1.5 #assim da pra aumentar 50% de um item
print(precos)

# Contar quantas vezes o mesmo item aparece
lista_de_produtos = ["iphone", "airpod", "ipad" "macbook"]
print(lista_de_produtos.count("iphone"))

# Ordenar uma lista
lista_de_produtos = ["iphone", "airpod", "ipad" "macbook"]
lista_de_produtos.sort(reverse=True)





















