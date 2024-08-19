#Método que tem retorno e não recebe parâmetro
def getPI():
    return 3.14



#Método que não tem retorno e não recebe parâmetro
def imprimirPI():
    print( getPI() )
#Método que não tem retorno e recebe parâmetro
def imprimirAreaCirculo(radius):
    print(calcularAreaCirculo( radius ))

#Método que tem retorno e não recebe parâmetro
def calcularAreaCirculo(raio):
    area = getPI() * ( raio * raio )
    return area

produtos = ["Computador","Celular","Teclado","Mouse"]
precos = [2000,1500,500,200]
quantidades = [6,15,10,5]
def imprimir_produtos(pos):
    try:
        return print(produtos[pos])
    except IndexError:
        print("Digite uma posição válida")

def retirar_produto(pos):
    try:
        produtos.pop(pos)
        precos.pop(pos)
        quantidades.pop(pos)
    except IndexError:
        print("Digite uma posição válida")

imprimir_produtos(1)
retirar_produto(1)
imprimir_produtos(1)
