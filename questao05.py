#Declare str com nome da cidade
#Um inteiro com ano de nascimento
#Um float com altura em metros
#Um boolean de se você gosta de programar
#Mostrar em um texto pro usuário

#cidade = "Biguaçu"
#ano_nascimento = 1997
#altura = 1.61
#gosta_programar = True
#
#print(f"Adoro a cidade {cidade}, \n"
#      f"Nasci em {ano_nascimento} \n"
#      f"Tenho {altura} metros \n"
#      f"Eu {'gosto'if gosta_programar else 'não gosto'} de programar")

cidade = input("Digite sua cidade favorita: ")
ano_nascimento = int(input("Digite seu ano de nascimento: "))
altura = float(input("Digite sua altura em metros: "))
gosta_programar = True if input("Você gosta de programar ? ") == "gosto" else False

print(f"Adoro a cidade {cidade}, \n"
      f"Nasci em {ano_nascimento} \n"
      f"Tenho {altura} metros \n"
      f"Eu {'gosto'if gosta_programar else 'não gosto'} de programar")



