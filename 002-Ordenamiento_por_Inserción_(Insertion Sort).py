#Alma Paola Garcia Landeros
#21110038
#6E1
#Inteligencia Artificial
#Centro de Enseñanza Tecnica Industrial

def insertion_sort(arr):
    """
    Función para ordenar un arreglo utilizando el algoritmo de Insertion Sort.
    
    Args:
    - arr: Lista o arreglo que se desea ordenar.
    
    Returns:
    - El arreglo ordenado en orden ascendente.
    """
    n = len(arr)  # Obtener la longitud del arreglo
    
    # Iterar sobre todos los elementos del arreglo, comenzando desde el segundo elemento
    for i in range(1, n):
        key = arr[i]  # Elemento actual que será insertado en la parte ordenada
        
        # Mover los elementos del arreglo que son mayores que 'key' a una posición hacia adelante
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insertar 'key' en su posición correcta en la parte ordenada
        arr[j + 1] = key
        
        # Imprimir el estado del arreglo después de cada pasada (opcional)
        print(f'Paso {i}: {arr}')
    
    return arr

# Ejemplo de uso:
array = [12, 11, 13, 5, 6]
print("Array original:", array)
sorted_array = insertion_sort(array.copy())  # Llamar a la función con una copia del arreglo original
print("Array ordenado:", sorted_array)
