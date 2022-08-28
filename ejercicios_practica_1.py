# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con diccionarios

from ast import Try
import csv
from re import T


def ej1():
    print('Ejercicios con diccionarios 1º')
    # Crear un diccionario vacio
    # el diccionario vacio debe llamarse "stock"
    
    # stock = ....

    # Luego de crear el diccionario completelo
    # con el siguiente stock:
    # tornillos = 100
    # tuercas = 150
    # arandelas = 300

    # Los nombres tornillos, tuercas y arandelas
    # son las claves (keys) del diccionario
    # mientras que las cantidades son los valores (values)

    # Una vez armado el diccionario imprimirlo en pantalla con print

    # Comenzar aquí, recuerde el identado dentro de esta funcion

    stock = {} #diccionario vacio
    stock['Tornillos'] = 100
    stock['Tuercas'] = 150
    stock['Arandelas'] = 300

    for k,v in stock.items():

        print('La cantidad de {} es {}'.format(k,v))
        print()

def ej2():
    print('Ejercicio con diccionarios 2º')
    # Basado en el ejercicio anterior ej1, utilizaremos el diccionario
    # como una base de datos. Comenzaremos con un diccionario de stock
    # de nuestros productos en cero:
    
    stock = {'tornillos': 0, 'tuercas': 0, 'arandelas': 0}

    # Paso 1:
    # Crear un bucle utilizando while que se ejecute de forma infinita
    # while True.....
    
    # Paso 2:
    # Dentro de ese bucle consultar al usuario por consola
    # que producto desea agregar al stock
    #   - Si el usuario ingresa "FIN" como producto se debe 
    #   finalizar el bucle
    #   - Si el usuario ingresa un producto no definido en el stock
    #   se debe enviar un mensaje de error. (si desea investigar esto
    #   se resuelve muy bien utilizando el operador "in" con diccionarios)

    # Paso 3:
    # Luego de haber ingresado el producto se debe ingresar por consola
    # cuanto stock de ese producto se desea agregar al stock.
    # Si teniamos 20 tornillos y el usuario desea agregar 10 tornillos más,
    # en nuestro diccionario deben quedar 30 tornillos (debe acumular)

    # Paso 4:
    # Cuando el usuario ingrese "FIN" y se termine el bucle, debe
    # imprimir en pantalla con print el diccionario con el stock final

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    cantidad=0
    print('Este es el stock actual:')
    print()
    while True:
        for k,v in stock.items():
            print('el stock de {} es {}'.format(k,v))
            print()
        print('Si desea salir ingrese: FIN')
        print('Si no, agregue el producto deseado')
        print()
        k=str(input('Ingrese el producto deseado o FIN para salir: '))
       
                              
        if k.upper() == 'FIN':
            for k,v in stock.items():
                print('el stock de {} es {}'.format(k,v))
            break
            

        else:
            try:
                stock [k] in stock
                stock [k]+= int(input('Ingrese la cantidad: '))
                
            except:
                print('EL PRODUCTO NO ESTA DEFINIDO EN EL STOCK!!!')
                print()
        
            
if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    ej2()