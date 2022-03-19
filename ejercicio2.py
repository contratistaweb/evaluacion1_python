# Ejercicio 2
# frutas invertidas 

frutas = [];
print('*** Hagamos salpicon, acontinuacion ingresa cada una de las frutas. ***')
for  i in range(10):
    nuevaFruta = input('- ingrese el nombre de la fruta: ');
    frutas.append(nuevaFruta);
    
print(frutas[::-1]);
