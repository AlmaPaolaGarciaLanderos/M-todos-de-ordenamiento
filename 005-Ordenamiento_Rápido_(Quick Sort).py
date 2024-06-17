#Alma Paola Garcia Landeros
#21110038
#6E1
#Inteligencia Artificial
#Centro de Enseñanza Tecnica Industrial

def quick_sort(arr):
    """
    Función para ordenar un arreglo utilizando el algoritmo de Quick Sort.
    
    Args:
    - arr: Lista o arreglo que se desea ordenar.
    
    Returns:
    - El arreglo ordenado en orden ascendente.
    """
    # Llamar a la función auxiliar para realizar el ordenamiento
    quick_sort_helper(arr, 0, len(arr) - 1)
    
    return arr

def quick_sort_helper(arr, low, high):
    """
    Función auxiliar recursiva para ordenar un subarreglo utilizando el algoritmo de Quick Sort.
    
    Args:
    - arr: Lista o arreglo que se desea ordenar.
    - low: Índice inicial del subarreglo.
    - high: Índice final del subarreglo.
    """
    if low < high:
        # Obtener el índice del pivote después de particionar el arreglo
        pivot_index = partition(arr, low, high)
        
        # Llamar recursivamente a quick_sort_helper para los subarreglos izquierdo y derecho del pivote
        quick_sort_helper(arr, low, pivot_index - 1)
        quick_sort_helper(arr, pivot_index + 1, high)

def partition(arr, low, high):
    """
    Función para particionar el arreglo y devolver el índice del pivote.
    
    Args:
    - arr: Lista o arreglo que se desea particionar.
    - low: Índice inicial del subarreglo.
    - high: Índice final del subarreglo.
    
    Returns:
    - Índice del pivote.
    """
    # Elegir el último elemento como pivote
    pivot = arr[high]
    
    # Índice del elemento más pequeño
    i = low - 1
    
    for j in range(low, high):
        # Si el elemento actual es más pequeño que o igual al pivote, lo intercambiamos con el elemento en i
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Colocar el pivote en su posición correcta intercambiándolo con el elemento en i+1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    # Devolver el índice del pivote
    return i + 1

# Ejemplo de uso:
array = [10, 7, 8, 9, 1, 5]
print("Array original:", array)
sorted_array = quick_sort(array.copy())  # Llamar a la función con una copia del arreglo original
print("Array ordenado:", sorted_array)
