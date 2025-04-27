def _and(a, b):
    return (bool(a))*(bool(b))      #A*B: Igual a matematicas (solo el 1*1 da 1)

def _or(a, b):
    result = (bool(a))+(bool(b))    #1+0 y 0+1 dan 1, 0+0 da 0 pero 1+1 da 2, por eso ↓
    if result > 1:                  #si da un resultado mayor a 1
        result = result//2          #dividimos por 2 y nos quedamos con la parte entera, así 1+1=1
    return result

def _xor(a, b):
    return int(bool(a) != bool(b))      #A xor B: devuelve 1(verdadero) si  a≠b

def _nand(a, b):
    #Multiplicación hace lo mismo que la operación AND
    #Luego 1 - (a * b) invierte el resultado: si el resultado es 1, será 0. Si es 0, será 1
    return 1 - (a * b)

def _nor(a, b):
    suma = int(bool(a)) + int(bool(b))
    if suma > 1:
        suma = 1  # Porque 1+1 tiene que seguir siendo 1
    return 1 - suma

def _not(a):
    return 1 - int(bool(a))         #NOT A = 1 - A: inversion matematica (si A = 1 -> 0, si A = 0 -> 1)

def generador_de_tabla_de_verdad(operacion):
    if operacion == 6:                  #6=NOT Tabla especial
        print("A | Resultado")
        print("--|----------")
        for A in [0, 1]:
            resultado = _not(A)
            print(f"{A} |    {resultado}")
    else:
        print("A | B | Resultado")
        print("--|---|----------")
        for A in [0, 1]:
            for B in [0, 1]:
                operaciones = {
                    1: _and(A, B),      #1=AND
                    2: _or(A, B),       #2=OR
                    3: _xor(A, B),      #3=XOR
                    4: _nand(A, B),     #4=NAND
                    5: _nor(A, B)          #5=NOR
                }
                resultado = operaciones[operacion]
                print(f"{A} | {B} |    {resultado}")
    return


#Programa principal:
MENU_OPCIONES = """
Ingresa la opción deseada:
1: AND
2: OR
3: XOR
4: NAND
5: NOR
6: NOT
0: EXIT
"""

# Validaciones del input
entrada = input(MENU_OPCIONES)                                              #Mostramos al usuario el menu definido en MENU_OPCIONES
while len(entrada) != 1 or entrada < '0' or entrada > '6':                  #Utilizamos una comparacion entre strings para definir la opcion y conservar el formato del menu
    print("Ingresaste una opcion invalida. Ingresa un numero del 1 al 6.")  
    entrada = input(MENU_OPCIONES)                                          
opcion = int(entrada)                                                       #Convertimos la entrada a entero

if opcion == 0:                                                             # Si la opcion es 0 Salimos del programa
    print("Saliendo del programa...")
    exit(0)

generador_de_tabla_de_verdad(opcion)