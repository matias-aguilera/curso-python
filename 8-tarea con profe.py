#peso_mexicano= 17
#peso_chileno= 797
#peso_argentino= 263

def conversor_moneda(valor_dolar):
        valor1=input("ingrese pesos chilenos: ")
        valor3 =(int(valor1)/int(valor_dolar))
        valor3=round(valor3,2)
        print("el valor es: " + str(valor3) +" "+"usd")
      
        
        


print(""" 
         convertidor de moneda:
          1- peso chileno a dolar
          2- peso mexicano a dolar
          3- peso argentino a dolar

""")

opcion = int (input("ingrese opcion a convertir:"))

if opcion ==1:
        conversor_moneda(767)
elif opcion ==2:
           conversor_moneda(17)
elif opcion ==3:
           conversor_moneda(263)           
else: 
        print("elija un numero entre 1 a 3")           

