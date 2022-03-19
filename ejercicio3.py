# Ejercicio 3 Menu
opcionSeleccionada = 10;
productos = [];

while opcionSeleccionada!=0:
    print('1. Agregar producto.');
    print('2. Ver productos registrados.');
    print('3. Actualizar el precio de un producto.');
    print('4. Eliminar un producto.');
    print('0. Salir.');
    opcionSeleccionada = int(input('Digite una opcion: '))
    if opcionSeleccionada == 1:
        print('Crear un producto: ')
        producto = {};
        producto['idProducto'] = input('Ingrese codigo del producto: ')
        producto['nombreProducto'] = input('Ingrese nombre del producto: ')
        producto['precioProducto'] = int(input('Ingrese precio del producto: '))

        productos.append(producto);

    elif opcionSeleccionada == 2:
        print('Ver productos.')
        print(productos)

    elif opcionSeleccionada == 3:
        print('Editar el precio de un producto.')
        buscar = input('Ingrese codigo del producto: ')
        for index, producto in enumerate(productos):
            productObj = productos[productos.index(producto)]
            if productObj.get('idProducto') == buscar:
                productObj['precioProducto'] = int(input('Ingrese nuevo precio del producto: '))
                print(productObj.get('precioProducto'))


    elif opcionSeleccionada == 4:
        print('seleccionaste 4.')
        buscar = input('Ingrese codigo del producto: ')
        for index, producto in enumerate(productos):
            productObj = productos[productos.index(producto)]
            if productObj.get('idProducto') == buscar:
                 productos.remove(producto)

print(productos)