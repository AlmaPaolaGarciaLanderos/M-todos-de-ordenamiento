#Alma Paola Garcia Landeros
#21110038
#6E1
#Inteligencia Artificial
#Centro de Enseñanza Tecnica Industrial

def heap_sort(arr):
    """
    Función para ordenar un arreglo utilizando el algoritmo de Heap Sort.
    
    Args:
    - arr: Lista o arreglo que se desea ordenar.
    
    Returns:
    - El arreglo ordenado en orden ascendente.
    """
    n = len(arr)
    
    # Construir el montículo (heap) máximo
    # Comenzando desde el último nodo no hoja hasta el primer nodo
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extraer elementos uno por uno del montículo
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Intercambiar el máximo (raíz) con el último elemento
        heapify(arr, i, 0)  # Llamar heapify en el montículo reducido
    
    return arr

def heapify(arr, n, i):
    """
    Función para convertir un subárbol con raíz en el índice i en un montículo (heap) máximo.
    
    Args:
    - arr: Lista o arreglo que contiene el montículo.
    - n: Tamaño del montículo.
    - i: Índice del nodo raíz del subárbol.
    """
    largest = i  # Inicializar el nodo raíz como el más grande
    left = 2 * i + 1  # Índice del hijo izquierdo
    right = 2 * i + 2  # Índice del hijo derecho
    
    # Verificar si el hijo izquierdo existe y es mayor que el nodo raíz
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Verificar si el hijo derecho existe y es mayor que el nodo raíz o el hijo izquierdo
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # Si el nodo raíz no es el más grande, intercambiarlo con el nodo más grande y llamar heapify recursivamente
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Ejemplo de uso:
array = [12, 11, 13, 5, 6, 7]
print("Array original:", array)
sorted_array = heap_sort(array.copy())  # Llamar a la función con una copia del arreglo original
print("Array ordenado:", sorted_array)
