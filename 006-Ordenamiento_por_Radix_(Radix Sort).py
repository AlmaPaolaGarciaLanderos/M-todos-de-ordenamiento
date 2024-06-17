#Alma Paola Garcia Landeros
#21110038
#6E1
#Inteligencia Artificial
#Centro de Enseñanza Tecnica Industrial

def radix_sort(arr):
    """
    Función para ordenar un arreglo utilizando el algoritmo de Radix Sort.
    
    Args:
    - arr: Lista de enteros que se desea ordenar.
    
    Returns:
    - El arreglo ordenado en orden ascendente.
    """
    # Encontrar el máximo número para determinar el número de dígitos
    max_num = max(arr)
    
    # Llamar a la función auxiliar para realizar el ordenamiento por dígitos
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    
    return arr

def counting_sort(arr, exp):
    """
    Función auxiliar para ordenar el arreglo por el valor del dígito en la posición específica (exp).
    Utiliza el algoritmo Counting Sort adaptado para Radix Sort.
    
    Args:
    - arr: Lista de enteros que se desea ordenar.
    - exp: Valor de la posición del dígito (1, 10, 100, ...).
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # Count array para almacenar el conteo de cada dígito (0-9)
    
    # Llenar el count array con las ocurrencias de cada dígito en la posición exp
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    
    # Ajustar el count array para reflejar las posiciones actuales de cada dígito
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Construir el arreglo de salida ordenado según el dígito en la posición exp
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    
    # Copiar el arreglo de salida ordenado al arreglo original
    for i in range(n):
        arr[i] = output[i]

# Ejemplo de uso:
array = [170, 45, 75, 90, 802, 24, 2, 66]
print("Array original:", array)
sorted_array = radix_sort(array.copy())  # Llamar a la función con una copia del arreglo original
print("Array ordenado:", sorted_array)
