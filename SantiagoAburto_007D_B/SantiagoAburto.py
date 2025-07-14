import os
os.system("cls")

productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0], 
}

def input_num(pregunta,Rmin,Rmax):
    while True:
        try:
            opcion = int(input(pregunta))
            if opcion>=Rmin and opcion <=Rmax:
                return opcion
            else:
                print("Por favor eliga una opción dentro del rango")
        except:
            print("Por favor solo escriba números enteros.")

def stock_marca(marca):
    if marca in stock:
        print("Hay notebooks disponibles!!")
        datos = stock[marca][1]
        nombre = productos[marca][0]
        print(f"De la marca {nombre} quedan {datos} notebooks.")
    else:
        print(f"No quedan notebooks de la marca {marca}.")

#def búsaqueda precio(p_min, p_max)

def eliminar_producto(modelo):
    if modelo in productos:
        return True
    else:
        return False
        
 

ciclo = True
while ciclo:
    os.system("cls")
    print(''' ***MENU PRINCIPAL***
          1. Stock marca
          2. Búsqueda por precio
          3. Eliminar producto
          4.Salir.
          ''')
    opcion = input_num("Ingrese una opción: ",1,4)
    match opcion:
        case 1:
            print("Stock por marca")
            marca= input("Ingrese la marca que desea buscar: ")
            stock_marca(marca)
        case 2:
            while True:
                try:
                    p_min = int(input("Ingrese el rango mínimo: "))
                    p_max = int(input("Ingrese el rango máximo: "))
                    if p_min > p_max:
                        print(F"El precio mínimo no puede ser mayor al máximo {p_max}.")
                    else:
                        break
                except:
                    print("Debe ingresar valores enteros!!")
            for modelos in stock:
                precio = int(modelos[0])
                marca = productos[modelos][0]
                cantidad = stock[modelos][1]
                modelo = stock
                if p_min>= precio >= p_max:
                    print("Hay notebooks en tu rango de precio!!")
                    print(f" y son los siguientes {marca} -- {modelo}.")
            else:
                print("No hay noteboocks con ese rango de precios")
            
            
        case 3:
            model = input("Ingrese el modelo a eliminar: ")
            eliminar_producto
        case 4:
            print("Programa finalizado.")
            ciclo = False
        case _:
            print("Opción invalida.")
    os.system("pause")
    