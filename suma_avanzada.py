def suma_avanzada(numeros):
    """
    Función para sumar una cantidad N de números
    
    Args:
        numeros (list): Lista de números a sumar
    
    Returns:
        float: Resultado de la suma de todos los números
    
    Raises:
        TypeError: Si el argumento no es una lista o contiene elementos que no son números
        ValueError: Si la lista está vacía
    """
    try:
        # Validar que el argumento sea una lista
        if not isinstance(numeros, list):
            raise TypeError("El argumento debe ser una lista de números")
        
        # Validar que la lista no esté vacía
        if len(numeros) == 0:
            raise ValueError("La lista no puede estar vacía")
        
        # Validar que todos los elementos sean números
        for i, num in enumerate(numeros):
            if not isinstance(num, (int, float)):
                raise TypeError(f"El elemento en la posición {i} no es un número: {num}")
        
        # Realizar la suma
        resultado = sum(numeros)
        return resultado
    
    except Exception as e:
        print(f"Error en la operación de suma avanzada: {e}")
        raise

def suma_avanzada_con_promedio(numeros):
    """
    Función auxiliar que calcula la suma y el promedio
    
    Args:
        numeros (list): Lista de números
    
    Returns:
        dict: Diccionario con 'suma', 'promedio' y 'cantidad'
    """
    try:
        suma = suma_avanzada(numeros)
        cantidad = len(numeros)
        promedio = suma / cantidad
        
        return {
            'suma': suma,
            'promedio': promedio,
            'cantidad': cantidad
        }
    
    except Exception as e:
        print(f"Error en el cálculo de suma y promedio: {e}")
        raise

# Función de prueba
if __name__ == "__main__":
    # Pruebas unitarias básicas
    print("=== PRUEBAS DEL MÓDULO SUMA AVANZADA ===")
    
    # Prueba 1: Lista de números positivos
    numeros1 = [1, 2, 3, 4, 5]
    resultado1 = suma_avanzada(numeros1)
    print(f"Suma de {numeros1} = {resultado1}")
    
    # Prueba 2: Lista con números negativos
    numeros2 = [-5, -3, -1, 4, 8]
    resultado2 = suma_avanzada(numeros2)
    print(f"Suma de {numeros2} = {resultado2}")
    
    # Prueba 3: Lista con números decimales
    numeros3 = [1.5, 2.3, 3.7, 4.1]
    resultado3 = suma_avanzada(numeros3)
    print(f"Suma de {numeros3} = {resultado3}")
    
    # Prueba 4: Lista con un solo número
    numeros4 = [42]
    resultado4 = suma_avanzada(numeros4)
    print(f"Suma de {numeros4} = {resultado4}")
    
    # Prueba 5: Lista con muchos números
    numeros5 = list(range(1, 11))  # [1, 2, 3, ..., 10]
    resultado5 = suma_avanzada(numeros5)
    print(f"Suma de números del 1 al 10 = {resultado5}")
    
    # Prueba 6: Función con promedio
    numeros6 = [10, 20, 30, 40, 50]
    resultado6 = suma_avanzada_con_promedio(numeros6)
    print(f"Números: {numeros6}")
    print(f"Suma: {resultado6['suma']}, Promedio: {resultado6['promedio']}, Cantidad: {resultado6['cantidad']}")
    
    # Prueba 7: Manejo de errores - lista vacía
    try:
        resultado7 = suma_avanzada([])
        print(f"Suma de lista vacía = {resultado7}")
    except ValueError as e:
        print(f"Error controlado: {e}")
    
    # Prueba 8: Manejo de errores - argumento no válido
    try:
        resultado8 = suma_avanzada("no es una lista")
        print(f"Suma de string = {resultado8}")
    except TypeError as e:
        print(f"Error controlado: {e}")
    
    print("=== PRUEBAS COMPLETADAS ===")