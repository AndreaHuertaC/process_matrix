from functools import reduce

def process_matrix(matrix):
    '''
    Recibe una matriz, chequea si es válida y si lo es devuelve una de iguales dimensiones en el que
    cada valor es la media del elemento original y sus vecinos en la matriz original. Si no es válida
    devuelve un ValueError indicándolo.
    '''
    if matrix == []:
        return []
    elif is_numerical_matrix(matrix):
        return _process_matrix(matrix)
    else:
        raise ValueError('Only works on numerical matrices')

def _process_matrix(matrix): 
    '''
    Recibe una matriz, y devuelve una matriz de mismas dimensiones en la que cada valor
     de la original es sustituido con las medias de cada elemento y sus vecinos.
    '''
    avg_matrix = []  
    for i, column in enumerate(matrix):
        new_col = []
        if one_column(matrix): # si es matriz de una columna
            new_col = process_element(0, i, matrix)
        else: # resto de casos (matrices de varias columnas)
            for j in range(len(column)):
                new_element = process_element(i, j, matrix)
                new_col.append(new_element)
        avg_matrix.append(new_col)
    return avg_matrix

def process_element(column, index, elements):
    """
    Recibe el número de columna o lista, el índice de un elemento y la matriz en la que está,
    calcula su promedio con sus vecinos y devuelve dicho promedio
    """
    # obtengo la lista de vecinos
    indices = get_neighbour_indices(column, index, elements)
    # y sus valores
    values = get_neighbour_values(indices, elements)
    # calculo su promedio
    average = get_average(values)
    # devuelvo el valor final
    return average

def get_neighbour_indices(column, index, matrix):
    """
    Recibe el número de columna o lista, el índice de un elemento y la matriz en la que está.
    Devuelve lista con listas, cada una con la columna e índice de los vecinos y el propio elemento. 
    """
    indices = []

    indices.append([column, index + 1])
    indices.append([column, index - 1])
    indices.append([column + 1, index])
    indices.append([column - 1, index])
    indices.append([column, index])

    if one_column(matrix): # si es matriz de 1 columna
        return filter(lambda x: x[0] == 0 and 0 <= x[1] < len(matrix), indices)
    else: #resto de casos (matrices de varias columnas)
        return filter(lambda x: 0 <= x[0] < len(matrix) and 0 <= x[1] < len(matrix[0]), indices)


def get_neighbour_values(indices, elements):
    '''
    Recibe la lista de listas con número de columna e indice de los vecinos y el propio elemento, 
    y devuelve una lista con los valores de cada vecino y el elemento
    '''
    if one_column(elements): # si es matriz de 1 columna
        return list(map(lambda x: elements[x[1]], indices))
    else: # resto de casos (matrices de varias columnas)
        return list(map(lambda x: elements[x[0]][x[1]], indices))
    # Añado list porque en la función process_element, get_average utiliza el output de esta función
    # y obtiene el len() de ello. En python 3 un objeto map no tienen len y da error.

def get_average(numbers): 
    """"
    Recibe una lista de números y devuelve su promedio
    """
    return round(reduce(lambda accum, b: accum + b, numbers, 0) / len(numbers), 2)

def is_numerical_matrix(matrix):
    '''
    Devuelve True si es la matriz que recibe es númerica de una columna o varias columnas de igual tamaño
    '''
    if one_column(matrix):
        return True
    else:
        return is_list_of_lists(matrix) and equal_sublist_size(matrix) and int_all_elements(matrix)

def one_column(matrix):
    '''
    Devuelve True si la matriz que recibe tiene solo una columna o lista
    '''
    indicator = False
    for col in matrix:
        if type(matrix) == list and type(col) == int:
            indicator = True
        else:
            indicator = False
            break
    return indicator 

def is_list_of_lists(matrix):
    '''
    Recibe una matriz y devuelve True si es una lista de listas
    '''
    indicator = False
    for col in matrix:
        if type(matrix) == list and type(col) == list:
            indicator = True
        else:
            indicator = False
            break
    return indicator

def equal_sublist_size(matrix):
    '''
    Recibe una matriz y devuelve True si las listas o columnas son del mismo tamaño'''
    indicator = False
    i = 0
    while i < len(matrix) - 1:
        len_sublist = len(matrix[i])
        if len_sublist == len(matrix[i + 1]):
            indicator = True
        else:
            indicator = False
        i += 1
    return indicator

def int_all_elements(matrix):
    '''
    Devuelve True si todos los elementos dentro de la matriz recibida (lista de listas)
    son de tipo números enteros (int).
    '''
    indicator = False
    for lista in matrix:
        for element in lista:
            if type(element) == int:
                indicator = True
            else:
                indicator = False
                break
    return indicator