def restar(num1, num2):
    """
    Función para restar dos números
    
    Args:
        num1 (float): Primer número (minuendo)
        num2 (float): Segundo número (sustraendo)
    
    Returns:
        float: Resultado de la resta (num1 - num2)
    
    Raises:
        TypeError: Si los argumentos no son números
    """
    try:
        # Validar que los argumentos sean números
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise TypeError("Los argumentos deben ser números")
        
        resultado = num1 - num2
        return resultado
    
    except Exception as e:
        print(f"Error en la operación de resta: {e}")
        raise

# Función de prueba
if __name__ == "__main__":
    # Pruebas unitarias básicas
    print("=== PRUEBAS DEL MÓDULO RESTA ===")
    
    # Prueba 1: Números positivos
    resultado1 = restar(10, 3)
    print(f"10 - 3 = {resultado1}")
    
    # Prueba 2: Números negativos
    resultado2 = restar(-10, -5)
    print(f"-10 - (-5) = {resultado2}")
    
    # Prueba 3: Número positivo menos negativo
    resultado3 = restar(10, -3)
    print(f"10 - (-3) = {resultado3}")
    
    # Prueba 4: Números decimales
    resultado4 = restar(8.5, 2.3)
    print(f"8.5 - 2.3 = {resultado4}")
    
    # Prueba 5: Resta con cero
    resultado5 = restar(7, 0)
    print(f"7 - 0 = {resultado5}")
    
    # Prueba 6: Resta que da negativo
    resultado6 = restar(3, 10)
    print(f"3 - 10 = {resultado6}")
    
    print("=== PRUEBAS COMPLETADAS ===")