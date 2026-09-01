
# A função calcula o preço final com desconto baseado no preço original do produto
def calculodesconto(preco):
    if preco <= 100:
        print("\nSEM DESCONTO")
        desconto = 0  
    elif preco <=200:
        desconto = 10
    else:
        desconto = 20   

    valordesconto = preco * desconto/100
    precofinal = preco - valordesconto
    return precofinal

print("\nSISTEMA DE DESCONTO")
print("Nas compras acima de R$ 100,00 o desconto é de 10%")
print("A partir de R$ 200,00 é 20% e a partir de R$ 300,00 é 30%")
# Entrada de dados
preco = float(input("\nDigite o preço do produto: R$"))

# Cálculo do preço com desconto 
precocomdesconto = calculodesconto (preco)

# Saída de dados
print (f"\nPreço com desconto: R$ {precocomdesconto:.2f}")
print (f"O desconto foi de: R$ {preco - precocomdesconto:.2f}")
print (f"A porcentagem de desconto foi de: {(preco - precocomdesconto) / preco * 100:.2f}%")

# Variáveis: desconto, valordesconto, precofinal, preco, precocomdesconto
# Estruturas de decisão: if, elif, else
# Estruturas de repetição: não há 
# Tipos de dados: float 
