def fillText(list_words, width):
    '''Rellena la cadena con espacios en blanco.

    Parámetros:
    list_words -- Lista de palabras en una línea
    width -- Ancho del párrafo
    '''

    index = 0  # 1ra posición de la lista de palabras
    while len(' '.join(list_words)) < width:  # Mientra el tamaño siga siendo menor al ancho establecido
        list_words[index] += ' '  # Agrego un espacio al fina de cada palabra
        index += 1  # Siguiente posición de una palabra
        index = (lambda x, y: 0 if (x == y) else x) (index, len(list_words) - 1)  # Si la posición es de la última palabra
    return ' '.join(list_words)  # Retorna la nueva cadena con tamaño igual al del ancho establecido

def justifyText(text, width):
    '''Justifica un texto según el ancho dado.

    Parámetros:
    text -- Texto a justicar
    width -- Ancho del párrafo
    '''

    texto = ''
    words = text.split(' ')
    line = ''  # Palabras que conforman la línea
    len_line = 0  # Tamaño de la línea
    space = ''  # Caracter separador (Una sola palabra no necesita espacios)
    for word in words:
        len_line += len(word) + len(space)
        if len_line <= width:  # Si el tamaño de la línea es menor al ancho establecido
            line += space + word
            space = ' '
        else:  # Si se sobrepasa el ancho establecido
            if len(line) != width:  # Si el tamaño no es igual al ancho establecido
                line = fillText(line.split(space), width)  # Rellenar la línea hasta el ancho establecido
            texto += line + '\n'
            line = word  # Reniciar la línea siguiente con la palabra
            len_line = len(word)  # Reiniciar el tamaño de la línea
    return texto + line  # Concatena la última línea sin justificar y retorna

text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet odio ligula. Curabitur sagittis maximus ligula, et tristique dolor molestie vel. Cras ultrices sagittis ligula, nec consequat tellus elementum a. Pellentesque in lacus et felis hendrerit pellentesque. Donec pharetra consectetur erat, ut aliquet ligula. Duis fringilla ornare orci, sed rutrum ex sagittis sit amet. Fusce consectetur venenatis purus a vehicula. Phasellus egestas orci sed sem laoreet laoreet. Curabitur ex nibh, interdum a odio sit amet, porttitor vulputate sapien. Nulla facilisis sapien id leo egestas dictum.'
width = 125
print(justifyText(text, width))