import math


def findTheColor(x, y):
    '''Dado 2 enteros, retorna 'white' o 'black', en base al color del gráfico ('/resoruces/findTheColor (Graphic).jpg'). 

    Parámetros:
    x -- número entero positivo o negativo
    y -- número entero positivo o negativo

    Ejemplo:
    Cuando sea 2 y 1, retornaría 'white'.
    Cuando sea 2 y 1, retornaría 'black'.
    Cuando sea 4 y 3, retornaría 'black'.
    Cuando sea 4 y 3, retornaría 'black'.
    '''
    
    rad=0
    for i in range(1,6):
        if i==5:    #Si el punto no está en los primeros 4 círculos
            return 'black'
        rad=i
        d=math.sqrt((x-0)**2 + (y-0)**2)
        if d < rad: #Está dentro del círculo
            break
    if (x>0 and y>0) or (x<0 and y<0):  #Si está en el cuadrante I o III (+,+)(-,-)
        if rad%2==0:
            return 'white'
        return 'black'
    else:   #Caso contrario está en el cuadrante II o IV (+,-)(-,+)
        if rad%2==0:
            return 'black'
        return 'white'

print(findTheColor(4, -3))