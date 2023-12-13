def compress(cad):
    '''Comprime una cadena que no contenga números. Si la cadena está vacía, retorna una cadena vacía y si es null retorna null.

    Parámetros:
    cad -- cadena a ser comprimida

    Ejemplo:
    Dada la cadena 'aaaabbdxay' retornaría 'a4b2dxy'
    '''

    if not cad:
        return None
    else:
        res = ''
        for car in cad:
            if car not in res:
                res += car + str(cad.count(car))  # Concatena el caracter con el nro total de veces que está en la cadena cad
        return res.replace('1', '')  # Quitamos los 1's que se generaron cuan hay una sola conicidencia.

print(compress(input('Cadena a comprimir: ')))