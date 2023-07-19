#los telefonos de una empresa tienen el siguiente formato  prefico-numero-prefico donde el prefijo es el codigo del pais +34, y la extencion 
#tiene dos digitos(por ejemplo +34-913724710-56). escribir un programa que pregunte por un numero de telefono con este formato en la consola y
#muestre por pantalla el numero de telefono sin el prefijo y la extencion


def telefono(num):
     num = num[4:13]
     print(num)
    




def main():
    telefono(input("ingrese numero de telefono"))


if __name__=="__main__":
     main()

