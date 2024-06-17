#Alma Paola Garcia Landeros
#21110038
#6E1
#Inteligencia Artificial
#Centro de Enseñanza Tecnica Industrial

def counting_sort(arr):
    """
    Función para ordenar un arreglo utilizando el algoritmo de Counting Sort.
    
    Args:
    - arr: Lista o arreglo que se desea ordenar. Debe contener enteros no negativos.
    
    Returns:
    - El arreglo ordenado en orden ascendente.
    """
    # Encontrar el valor máximo en el arreglo para determinar el rango
    max_val = max(arr)
    
    # Inicializar un arreglo de conteo con tamaño suficiente para cubrir el rango de valores
    count = [0] * (max_val + 1)
    
    # Llenar el arreglo de conteo con las frecuencias de cada elemento en arr
    for num in arr:
        count[num] += 1
    
    # Reconstruir el arreglo ordenado utilizando el arreglo de conteo
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    
    return sorted_arr

# Ejemplo de uso:
array = [4, 2, 2, 8, 3, 3, 1]
print("Array original:", array)
sorted_array = counting_sort(array.copy())  # Llamar a la función con una copia del arreglo original
print("Array ordenado:", sorted_array)
