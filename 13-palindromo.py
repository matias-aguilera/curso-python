#palindromo 

def palindromo(palabra):
    palabra=palabra.strip()
    palabra=palabra.lower()
    palabra=palabra.replace(" ", "")

    palabra2=palabra[::-1]

    if palabra == palabra2:
        return True
    else:
        return False




def main():
    
        palabra = (input("ingrese palabra:"))
        resultado= palindromo(palabra)

        if resultado :
            print("es palindromo")
        else:
            print("no es palindromo")


#punto de entrada
#es una buena practica

if __name__ == '__main__':
    main()
