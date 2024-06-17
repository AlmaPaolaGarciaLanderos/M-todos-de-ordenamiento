#Alma Paola Garcia Landeros
#21110038
#6E1
#Inteligencia Artificial
#Centro de Enseñanza Tecnica Industrial

def bubble_sort(arr):
    """
    Función para ordenar un arreglo utilizando el algoritmo de Bubble Sort.
    
    Args:
    - arr: Lista o arreglo que se desea ordenar.
    
    Returns:
    - El arreglo ordenado en orden ascendente.
    """
    n = len(arr)  # Obtener la longitud del arreglo
    
    # Iterar sobre todos los elementos del arreglo
    for i in range(n):
        swapped = False  # Bandera para optimizar el rendimiento: si no se realizan intercambios, el arreglo ya está ordenado
        
        # Últimos i elementos ya están en su lugar correcto
        for j in range(0, n-i-1):
            # Comparar elementos adyacentes y realizar el intercambio si el primer elemento es mayor que el segundo
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True  # Se marca como verdadero si se realizó algún intercambio
        
        # Si no se realizan intercambios en esta pasada, el arreglo está ordenado y se puede detener el proceso
        if not swapped:
            break
        
        # Imprimir el estado del arreglo después de cada pasada (opcional)
        print(f'Paso {i + 1}: {arr}')
    
    return arr

# Ejemplo de uso:
array = [64, 34, 25, 12, 22, 11, 90]
print("Array original:", array)
sorted_array = bubble_sort(array.copy())  # Llamar a la función con una copia del arreglo original
print("Array ordenado:", sorted_array)
