#ejercicio 1 
#escribir un programa que pregunte el nombre al usuario y el numero entero .
#imprima por consola el nombre del usuario, uno por linea, tantas veces como el numero introduciso

#print("hola"* 3)

nombre=input("ingrese nombre")
numero=int(input("ingrese numero"))

print((nombre + "\n") * numero)




#ejercicio 2 
#escribir por pantalla el resultado de la siguiente operacion aritmetica:

calculo=((3+2)/(2*5))**2
print(calculo)

#ejercicio3
#una jugeteria tiene mucho exito en dos de sus productos: payasos y muñecas. suele hacer venta por correo y la empresa de logistica
#les cobra por peso de cada paquete asi que deberan calcular el peso de los payasos y muñecas que saldran en cada paquete a demanda. 
#cada payaso pesa 112g y cada muñeca 75g. escribir un programa que lea el numero de payasos y muñecas vendidos en el ultimo pedido y 
#calcule el peso total del paquete que sera anviado


peso_payaso=112
peso_muneca=75
cant_payaso=int(input("ingrese cantidad para payasos"))
cant_muneca=int(input("ingrese cantidad para muñecas"))

peso_total=(peso_payaso*cant_payaso)+(peso_muneca*cant_muneca)
print("el peso total es :" +str(peso_total)+"gr")
