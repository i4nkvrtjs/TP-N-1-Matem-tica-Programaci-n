def _and(a, b):
    return (bool(a))*(bool(b))      #A*B: Igual a matematicas (solo el 1*1 da 1)

def _or(a, b):
    result = (bool(a))+(bool(b))    #1+0 y 0+1 dan 1, 0+0 da 0 pero 1+1 da 2, por eso ↓
    if result > 1:                  #si da un resultado mayor a 1
        result = result//2          #dividimos por 2 y nos quedamos con la parte entera, así 1+1=1
    return result

def generador_de_tabla_de_verdad(operacion):
    print("A | B | Resultado")
    print("--|---|----------")
    for A in [0, 1]:
        for B in [0, 1]:
            operaciones = {
            1: _and(A, B),      #1=AND
            2: _or(A, B),       #2=OR
            3: (A, B),      #3=XOR
            4: not(A and B),    #4=NAND
            5: not(A or B)      #5=NOR
            }
            resultado = operaciones[operacion]
            print(f"{A} | {B} |    {resultado}")
    return

generador_de_tabla_de_verdad(2)   #Acá iría la opcion elegida por el usuario