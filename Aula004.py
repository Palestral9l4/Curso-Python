## if lógica e condições ##

# if condicao/comparacao:
    #tudo oq acontece se a condicao for verdadeira

# else:
    #tudo oq acontece se a condicao for falsa

# > maior que
# < menor que
# >= maior ou igual
# <=menor ou igual
# == igual
# != diferente

vendas = 1500
meta = 1200

if vendas > meta:
    print("Vendedor ganha bônus")
    bonus = 0.1 * vendas
    print("Bonus do vendedor:", bonus)
else:
    print("Vendedor não bateu a meta")


vendas = 2100
vendas_empresa = 10000
metas_empresa = 20000
meta1 = 1300 #ganhar 10%
meta2 = 2000 #ganhar 13%

if vendas >= 2000 and vendas_empresa >= metas_empresa: #and ou or
    bonus = 0.13 * vendas #13%
elif vendas >= 1300 and vendas_empresa >= metas_empresa:
    bonus = 0.1 * vendas #10%
else:
    bonus = 0

print("Bonus:", bonus)

lista_de_produtos = ["tv", "carro", "celular", "chaves"]
produtos_procurados = input("Procure um produto:")
produtos_procurados = produtos_procurados.lower()
if produtos_procurados in lista_de_produtos:
    print("Produto no estoque.")
else:
    print("Não temos esse produto.")