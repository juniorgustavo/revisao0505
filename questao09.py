frutas = ["banana", "maçã", "abacaxi", "maracujá", "melancia"]
fruta = input(f"Qual fruta você quer adicionar na lista ? {frutas}\n")
frutas.append(fruta)
frutas.pop(1)
#frutas.insert
print("A lista de frutas é ", frutas)