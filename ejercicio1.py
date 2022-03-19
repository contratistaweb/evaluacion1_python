# Ejercicio 1
# Construir un programa que permita ingresar N (cantidad digitada por el
# usuario) números enteros y cuente cuantos múltiplos de 2 y de 3 fueron
# ingresados (+1)

arrNumeros = []
contador2 = 0
contador3 = 0
cantidadNumeros = int(input("Ingrese la cantidad de numeros a evaluar: "))

for i in range(cantidadNumeros):
    numero = int(input('Ingrese un numero: '))
    arrNumeros.append(numero)

    multiplo2 = arrNumeros[i] % 2
    multiplo3 = arrNumeros[i] % 3
    
    if(multiplo2 == 0 and multiplo3 == 0):
        contador2 += 1
        contador3 += 1
    elif(multiplo2 == 0):
        contador2 += 1
    elif(multiplo3 == 0):
        contador3 += 1    

print(f'La cantidad de multiplos de dos es: {contador2} y de tres es: {contador3}')
