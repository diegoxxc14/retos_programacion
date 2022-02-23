def drawNumbers(num):
    '''Simular una pantalla digital utilizando asteriscos en una matriz, como en la imagen (resources\drawNumbers.jpg).

    La matriz debe ser siempre de 5x7. Si el número recibido es menor que 10, el primer espacio debe ser reemplazdo por 0. Si el número es menor que 0 o mayor que 99, retorna una matriz con “ER” dibujado.

    Parámetros:
    num -- número entero (0 - 99)

    Retorna:
    Matriz de valores de caracteres con los números dibujados en ellos
    '''

    mat = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    ini, fin = 0, 3

    if 0 <= num < 100:
        if num < 10:
            num = '0' + str(num)
        else:
            num = str(num)

        for pos in range(2):  # Recorrer dos veces
            if num[pos] == '0':
                for i in range(5):  # Filas
                    for j in range(ini, fin):
                        if 0 < i < 4 and j == ini+1:  # Controlo los espacios en blanco
                            continue
                        mat[i][j] = '*'
                        
            elif num[pos] == '1':
                for i in range(5):  # Filas
                    for j in range(ini, fin):
                        if j == fin-1:
                            mat[i][j] = '*'

            elif num[pos] == '2':
                for i in range(5):  # Filas
                    for j in range(ini, fin):
                        if (i == 1 and j < fin-1) or (i == 3 and j > ini):  # Controlo los espacios en blanco
                            continue
                        mat[i][j] = '*'
            
            elif num[pos] == '3':
                for i in range(5):  # Filas
                    for j in range(ini, fin):
                        if (i == 1 or i == 3) and j < fin-1:  # Controlo los espacios en blanco
                            continue
                        mat[i][j] = '*'

            elif num[pos] == '4':
                for i in range(5):  # Filas
                    for j in range(ini, fin):
                        if (j == ini and i > 2) or (j == ini+1 and i != 2):  # Controlo los espacios en blanco
                            continue
                        mat[i][j] = '*'
            
            elif num[pos] == '5':
                for i in range(5):  # Filas
                    for j in range(ini, fin):
                        if (i == 1 and j > ini) or (i == 3 and j < fin-1):  # Controlo los espacios en blanco
                            continue
                        mat[i][j] = '*'
            
            elif num[pos] == '6':
                for i in range(5):  # Filas
                    for j in range(ini, fin):
                        if (j == ini+1 and (i == 1 or i == 3)) or (j == fin-1 and i == 1):  # Controlo los espacios en blanco
                            continue
                        mat[i][j] = '*'
            
            elif num[pos] == '7':
                for i in range(5):  # Filas
                    for j in range(ini, fin):
                        if i == 0 or j == fin-1:
                            mat[i][j] = '*'

            elif num[pos] == '8':
                for i in range(5):  # Filas
                    for j in range(ini, fin):
                        if (i == 1 or i == 3) and j == ini+1:  # Controlo los espacios en blanco
                            continue
                        mat[i][j] = '*'

            elif num[pos] == '9':
                for i in range(5): #Filas
                    for j in range(ini, fin):
                        if (i == 3 and j == ini) or ((i == 1 or i == 3) and j == ini+1):  # Controlo los espacios en blanco
                            continue
                        mat[i][j] = '*'
            
            ini, fin = 4, 7
    else:
        for i in range(5):  # Letra 'E'
            for j in range(3):
                if (i == 1 or i == 3) and j > 0:  # Controlo los espacios en blanco
                    continue
                mat[i][j] = '*'

        for i in range(5):  # Letra 'R'
            for j in range(4, 7):
                if ((i == 1 or i == 4) and j == 5) or (i == 3 and j == 6):  # Controlo los espacios en blanco
                    continue
                mat[i][j] = '*'

    return mat

m = drawNumbers(100)

for i in m:
    for j in i:
        print(j, end='')
    print()