idade = int(input("Qual sua idade ?"))
preco_inteiro = 100
e_estudante = input("Você é estudante ? S para sim, N para não. ")
preco_desconto = None

if idade < 12:
    preco_desconto = preco_inteiro-(preco_inteiro * 0.5)
elif idade > 60:
    preco_desconto = preco_inteiro-(preco_inteiro * 0.3)
elif e_estudante=="S":
    preco_desconto = preco_inteiro-(preco_inteiro * 0.1)

print("O preço do ingresso é ", preco_desconto or preco_inteiro)