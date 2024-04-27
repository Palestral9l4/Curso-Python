print("Ola, Mundo!") # Função print para mostrar algo
email = "emailqualquer@gmail.com" # tipo de variavel string -> texto
faturamento = 1200 # Variavel do tipo: int -> numero inteiro
custo = 750.32 # Variavel do tipo: float -> numero com casa decimal (que deve ser separado por ponto e nao virgula)
novas_vendas = 100 # Codigo tem que ser escrito para ser execultado de cima para baico, caso essa linha esteja em um lugar errado o codigo vai ter um erro
faturamento = faturamento + novas_vendas # Da pra mudar o numero da primeira variavel
imposto = faturamento * 0.1 # A porcentagem deve ser escrita como 0.1(para 10%) ou 1.0(para 100%) e não com "%"
lucro = faturamento - custo - imposto
margem_de_lucro = lucro / faturamento

print("Faturamento foi de", faturamento)
print("O custo foi de", custo)
print("O lucro foi de", lucro)
print("A margem de lucro foi de", round(margem_de_lucro, 3)) # Funçãp round usado para arredondar numeros decimais Ex:round(variavel, 3(numero de casas decimais que você queira que apareça))

teve_lucro = True # Variavel usada para dizer verdadeiro ou falso

# Mod -> O resto da divisão Ex:
tempo_de_contrato = 170
tempo_em_anos = 170 / 12
print("tempo em anos", int(tempo_em_anos)) # int é uma variavel usada para mostrar numeros inteiros
tempo_em_meses = 170 % 12
print("tempo em meses", tempo_em_meses)


