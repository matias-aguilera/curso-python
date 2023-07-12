
entrada= int(input ("1 para usd, 2 para mxn, 3 para ars:"))

if entrada == 1:

        valor1=input("ingrese pesos chilenos: ")
        valor2=797
        valor3 =(int(valor1)/int(valor2))
        valor3=round(valor3,2)
        print("el valor es: " + str(valor3) +" "+"usd")

elif entrada ==2:        

        valor1=input("ingrese pesos chilenos: ")
        valor2=47.87
        valor3 =(int(valor1)/int(valor2))
        valor3=round(valor3,2)
        print("el valor es: " + str(valor3) +" "+"mxn")

elif entrada ==3:         

        valor1=input("ingrese pesos chilenos: ")
        valor2=3.10
        valor3 =(int(valor1)/int(valor2))
        valor3=round(valor3,2)
        print("el valor es: " + str(valor3) +" "+"ars")

else: 
        print("elija un numero entre 1 a 3")        