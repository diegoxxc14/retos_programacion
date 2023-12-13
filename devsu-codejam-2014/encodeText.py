def encode(cad):
    '''Método que invierta una cadena, con todos los primeros caracteres de cada palabra en mayúscula y todos los demás
    letras en minúsculas. Las palabras siempre deben dividirse en un espacio. 
    
    Regla: 
    No se puede utilizar ningún método 'reverse' o 'split' dado por el lenguaje

    Parámetros:
    cad -- cadena a codificar

    Ejemplo:
    Dada la cadena 'Hello my friend', retornaría 'Dneirf Ym Olleh'
    '''

    if not cad:
        return None
    else:
        res=''
        for i in range(-1, -len(cad)-1, -1):  # Recorrer la cadena de atrás hacia adelante
            res+=cad[i]
        return res.title()

print(encode(input('Cadena: ')))