# como é uma lista em branco, "[]" fica vazio
lista = []

# leitura dos numeros digitados
for c in range (5):
    numero = int(input(f" Digite o {c + 1}° número: " ))
    lista.append(numero)


soma = sum (lista)

media = soma/len (lista)

pares = []

for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)

maior = max(lista)
menor = min(lista)

print("-" * 30)
print ("A soma dos números é:", soma)
print ("A média dos números é:", media)
print ("O maior número é:", maior)
print ("O menor número é:", menor)
print ("Os números pares são:", pares)