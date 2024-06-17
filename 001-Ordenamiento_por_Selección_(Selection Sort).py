#Alma Paola Garcia Landeros
#21110038
#6E1
#Inteligencia Artificial
#Centro de Enseñanza Tecnica Industrial

def selection_sort(arr):
    """
    Función para ordenar un arreglo utilizando el algoritmo de Selection Sort.
    
    Args:
    - arr: Lista o arreglo que se desea ordenar.
    
    Returns:
    - El arreglo ordenado en orden ascendente.
    """
    n = len(arr)  # Obtener la longitud del arreglo
    
    # Iterar a través de todos los elementos del arreglo
    for i in range(n):
        # Encontrar el índice del elemento mínimo en el subarreglo no ordenado
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Intercambiar el elemento mínimo encontrado con el primer elemento no ordenado
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        # Imprimir el estado del arreglo después de cada pasada (opcional)
        print(f'Paso {i + 1}: {arr}')
    
    return arr

# Ejemplo de uso:
array = [64, 25, 12, 22, 11]
print("Array original:", array)
sorted_array = selection_sort(array.copy())  # Llamar a la función con una copia del arreglo original
print("Array ordenado:", sorted_array)
