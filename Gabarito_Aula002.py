faturamento = 1200
custo = 700
lucro= faturamento - custo
email = "email@gmail.com"
margem_lucro = lucro / faturamento

# Forma de colocar valores dentro de um texto
print("Faturamento da empresa: {}, Custo: {}, Lucro: {}".format(faturamento, custo, lucro))
print(f"Faturamento da empresa: {faturamento}, Custo: {custo}, Lucro: {lucro}")

# Formas de formatar um texto
email = email.upper() # .upper() para deixar a fonte do texto em maiuscula
print(email)
email = email.lower() # .lower() para deixar a fonte do texto em minuscula
print(email)
print(email.capitalize()) # deixa a primeira letra maiuscula
print(email.title()) # deixa em maiusculo cada palavra

# .find para encontrar caracteres dentro do texto Ex:
email1 = "email1@gmail.com"
print(email1.find("@")) # .find mostra a posição do caractere que estra dentro do ("@")
# lembrando que a contagem começa com 0, ou seja... o primeiro caractere é o 0

# (len(email2)) mostra quantos caracteres existe dentro do texto
email2 = "email2@gmail.com"
print(len(email2)) 
# esse comando mostra de fato quantos caracteres existe dentro do texto, começando com 1

# [] elemento usado para pegar um caractere
email3 = "email3@gmail.com"
print(email3[0])
# nesse exemplo o caractere escolhido foi o 0 que é equivalente a primeira letra
# podemos colocar um valor negativo Ex: [-1] que seria equivalente ao ultimo caractere do texto
# colocando [:] podemos escolher uma parte do texto para ultilizar Ex:
print(email3[:6]) #escolhemos a parte "email3" para ser usada
print(email3[6:16]) #podemos colocar um numero em primeiro para iniciar de onde escolher a parte ultilizada do texto 

# .replace() usado para trocar uma parte do texto
email4 = email1.replace("gmail.com", "hotmail.com")
print(email4)
# Ex: variavel_que_vc_quer_criar = variavel_antiga.replace("texto que vc quer editar", "novo texto")


#####casos especiais / exercicios#####
# pegar o servidor do email
# usando .find para encontrar um caractere e denominar uma variante para tal. no caso do "+1", ira começar com o proximo caractere
posicao_arroba = email.find("@") + 1 # posicao_arroba(escolhendo nome da variavel)
servidor = email[posicao_arroba:]
print(servidor)

# pegar o primeiro nome
nome = "Mr robot"
posicao_espaco = nome.find(" ")
primeiro_nome = nome[:posicao_espaco]
print(primeiro_nome)

# pegar o sobrenome
segundo_nome = nome[posicao_espaco+1:] # +1 necessario nessa caso, pois ia aparecer um espaço antes do segundo nome
print(segundo_nome)

#casos especiais - formatações numericas em numeros
margem_lucro = round(margem_lucro, 2)
print(f"Faturamento da empresa: R$:{faturamento:.2f}, Custo: R$:{custo:.2f}, Lucro: R$:{lucro:.2f}, margem: {margem_lucro:+.0%}")
