def leer_3_dig(num_list):
    '''Separa e identifica cada dígito de un número entero con su equivalente en letras.
    
    '''
    unidad = ['','un','dos','tres','cuatro','cinco','seis','siete','ocho','nueve']
    decenas = ['','diez','veinte','treinta','cuarenta','cincuenta','sesenta','setenta','ochenta','noventa']
    dec10 = ['','once','doce','trece','catorce','quince','dieciséis','diecisiete','dieciocho','diecinueve']
    centenas = ['','ciento','doscientos','trescientos','cuatrocientos','quinientos','seiscientos','setecientos','ochocientos','novecientos']
    
    res = ''
    avance = 1
    num_aux = 0
    ceros = 0
    
    for num1 in reversed(num_list):
        if avance == 1: #Unidad
            num_aux = int(num1)
            res = unidad[num_aux]
            ceros += int((lambda x: x == '0')(num1))
        elif avance == 2: #Decena
            if ceros == 1 or num1 == '0':
                res = decenas[int(num1)] + res
            elif num1 == '1':
                res = dec10[int(num_aux)]
            elif num1 == '2':
                res = 'veinti' + res
            else:
                res = decenas[int(num1)] + ' y ' + res
            ceros += int((lambda x: x == '0')(num1))
        elif avance == 3:   #Centena
            if ceros == 2 and num1 == '1':
                res = 'cien'
            elif ceros == 2 or num1 == '0':
                res = centenas[int(num1)] + res
            else:
                res = centenas[int(num1)] + ' ' + res
        avance+=1
    return res


def numeros_letras(num):
    '''Convierte un número entero a su equivalente en letras.

    El número debe estar entre 1 y 999 999.

    Parámetros:
    num -- número a convertir (debe ser mayor a 0)

    '''
    num_list = list(str(num))
    lon = len(num_list)
    if lon <= 3:
        return leer_3_dig(num_list)
    elif lon <= 6:
        centena = leer_3_dig(num_list[lon-3:])
        mil = leer_3_dig(num_list[:lon-3])+' '
        if mil == 'un ':
            mil = ''
        return (mil + 'mil ' + centena).upper()
    else:
        return 'Número demasiado grande. Rango entre 1 - 999999.'    

print(numeros_letras(input()))