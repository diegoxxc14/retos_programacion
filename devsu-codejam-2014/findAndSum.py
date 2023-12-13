def findAndSum(text='When I was 18, I was in 1st year, and had 25 classmates'):
    '''Identifica los números dentro de una cadena de texto y los suma.

    Parámetros:
    text -- Cadena a analizar

    Ejemplo:
    Dado el texto 'When I was 18, I was in 1st year, and had 25 classmates', retornaría 44
    '''
    
    num = '0'
    suma = 0
    for i in text:
        if i.isdigit():  # Si el caracter es un número
            num += i  # Respaldo el número como str en una variable y se concatena
        else:
            suma += int(num)  # Convierto a int el valor de la variable y se suma
            num = '0'
    return suma

print(findAndSum(input('Texto: ')))