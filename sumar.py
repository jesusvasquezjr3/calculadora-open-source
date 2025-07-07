def sumar(num1, num2):
    """
    Función para sumar dos números
    
    Args:
        num1 (float): Primer número
        num2 (float): Segundo número
    
    Returns:
        float: Resultado de la suma
    
    Raises:
        TypeError: Si los argumentos no son números
    """
    try:
        # Validar que los argumentos sean números
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise TypeError("Los argumentos deben ser números")
        
        resultado = num1 + num2
        return resultado
    
    except Exception as e:
        print(f"Error en la operación de suma: {e}")
        raise

# Función de prueba
if __name__ == "__main__":
    # Pruebas unitarias básicas
    print("=== PRUEBAS DEL MÓDULO SUMA ===")
    
    # Prueba 1: Números positivos
    resultado1 = sumar(5, 3)
    print(f"5 + 3 = {resultado1}")
    
    # Prueba 2: Números negativos
    resultado2 = sumar(-10, -5)
    print(f"-10 + (-5) = {resultado2}")
    
    # Prueba 3: Número positivo y negativo
    resultado3 = sumar(10, -3)
    print(f"10 + (-3) = {resultado3}")
    
    # Prueba 4: Números decimales
    resultado4 = sumar(3.5, 2.7)
    print(f"3.5 + 2.7 = {resultado4}")
    
    # Prueba 5: Suma con cero
    resultado5 = sumar(7, 0)
    print(f"7 + 0 = {resultado5}")
    
    print("=== PRUEBAS COMPLETADAS ===")