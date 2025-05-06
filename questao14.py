cod_produto = int(input("Digite o código do produto: "))

match cod_produto:
    case 1:
        print("Eletrônicos")
    case 2:
        print("Roupas")
    case 3:
        print("Alimentos")
    case 4:
        print("Livros")
    case 5:
        print("Brinquedos")
    case _:
        print("Código inválido")