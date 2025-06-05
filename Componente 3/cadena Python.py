def multiplos_de_n(lista, n):
    nueva_lista = []
    for numero in lista:
        if numero % n == 0:
            nueva_lista.append(numero)
    return nueva_lista

numeros = [12, 5, 18, 7, 24, 9, 30]
n = 3
resultado = multiplos_de_n(numeros, n)
print(f"Lista original: {numeros}")
print(f"Múltiplos de {n}: {resultado}")

print("\n" + "="*50 + "\n")


while True:
    entrada = input("Ingrese un número entero positivo: ")
    
    try:
        numero = int(entrada)
        if numero > 0:
            print(f"Número válido ingresado: {numero}")
            break
        else:
            print("Error: El número debe ser mayor que 0. Intente de nuevo.")
    except ValueError:
        print("Error: Debe ingresar un número entero válido. Intente de nuevo.")

print("\n" + "="*50 + "\n")


def son_anagramas(cadena1, cadena2):
    cadena1 = cadena1.replace(" ", "").lower()
    cadena2 = cadena2.replace(" ", "").lower()
    
    if len(cadena1) != len(cadena2):
        return False
    
    return sorted(cadena1) == sorted(cadena2)

print("=== EJEMPLOS DE ANAGRAMAS ===")

resultado1 = son_anagramas("amor", "roma")
print(f"Ejemplo 1: 'amor' y 'roma' -> {resultado1}")

resultado2 = son_anagramas("hola", "casa")  
print(f"Ejemplo 2: 'hola' y 'casa' -> {resultado2}")

resultado3 = son_anagramas("La Cena", "CANELA")
print(f"Ejemplo 3: 'La Cena' y 'CANELA' -> {resultado3}")