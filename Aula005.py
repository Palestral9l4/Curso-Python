# se a luz viaja para todo lado sem um determinado fim, então todos os corpos celestes do universo estão ligados
## loop e estrutura de repetição ##
# for = para cada
# in dentro

# tudo oq vc quer q seja executado varias vezes

lista_vendas = [1000, 500, 800, 1500, 2000, 2300]

meta = 1200
percentual_bonus = 0.1

#Para cada venda dentro da minha lista de venda
for vendas in lista_vendas:
    if vendas >= meta: # se a venda for maior ou igual a meta...
        bonus = percentual_bonus * vendas # o bonus vai ser igual o percentual de bonus vezes a venda
    else:#caso contrario...
        bonus = 0#o bonus é 0

    print(bonus)

# for venda in lista_vendas:
#    print(venda)
#    print("Proximo item")









