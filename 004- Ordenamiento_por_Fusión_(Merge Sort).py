#Alma Paola Garcia Landeros
#21110038
#6E1
#Inteligencia Artificial
#Centro de Enseñanza Tecnica Industrial

def merge_sort(arr):
    """
    Función para ordenar un arreglo utilizando el algoritmo de Merge Sort.
    
    Args:
    - arr: Lista o arreglo que se desea ordenar.
    
    Returns:
    - El arreglo ordenado en orden ascendente.
    """
    # Caso base: si la longitud del arreglo es 1 o menos, está ordenado por definición
    if len(arr) <= 1:
        return arr
    
    # Dividir el arreglo en mitades izquierda y derecha
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Llamadas recursivas para ordenar las mitades izquierda y derecha
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Combinar las mitades ordenadas
    sorted_arr = merge(left_half, right_half)
    
    return sorted_arr

def merge(left, right):
    """
    Función auxiliar para combinar dos arreglos ordenados (merge step).
    
    Args:
    - left: Arreglo ordenado izquierdo.
    - right: Arreglo ordenado derecho.
    
    Returns:
    - Arreglo combinado y ordenado de left y right.
    """
    merged = []
    i = j = 0
    
    # Comparar elementos de left y right y agregar el más pequeño a merged
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # Agregar los elementos restantes de left (si hay alguno)
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    # Agregar los elementos restantes de right (si hay alguno)
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged

# Ejemplo de uso:
array = [38, 27, 43, 3, 9, 82, 10]
print("Array original:", array)
sorted_array = merge_sort(array.copy())  # Llamar a la función con una copia del arreglo original
print("Array ordenado:", sorted_array)
