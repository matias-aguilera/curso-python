#tipos de datos
# en python todo es un objeto

# tipos de datos (int integer)
# 1-numero entero (float flotante)
# 2- numeros decimales 
# 3- cadena de texo
# 4- booleanos


#3-cadena de texto
cadena_de_texto = "esto es una 'cadena' de texto"
comillas_simples= 'esto es una "cadena" de texto'
#comillas_triples= """ "comillas dobles" 'comillas simples' ""

cadena_1="hola"
cadena_2="mundo"
print(cadena_1 +""+ cadena_2)

#booleanos
estudiante= True
trabaja=False
print(estudiante)
print(trabaja)


#convertir tipos de datos
numero_1= input("ingrese un numero 1: ")
numero_2= input("ingrese un numero 2: ") 

print (numero_1 + numero_2)
print(int(numero_1) + int(numero_2))

decimal_2=125.12 
print(int(decimal_2))

numero_entero=45
print(float(numero_entero))

print("el numero entero es: " + str(numero_entero))