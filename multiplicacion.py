def multiplicar(num1, num2):
    """
    Función para multiplicar dos números
    
    Args:
        num1 (float): Primer número (multiplicando)
        num2 (float): Segundo número (multiplicador)
    
    Returns:
        float: Resultado de la multiplicación (num1 * num2)
    
    Raises:
        TypeError: Si los argumentos no son números
    """
    try:
        # Validar que los argumentos sean números
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise TypeError("Los argumentos deben ser números")
        
        resultado = num1 * num2
        return resultado
    
    except Exception as e:
        print(f"Error en la operación de multiplicación: {e}")
        raise

# Función de prueba
if __name__ == "__main__":
    # Pruebas unitarias básicas
    print("=== PRUEBAS DEL MÓDULO MULTIPLICACIÓN ===")
    
    # Prueba 1: Números positivos
    resultado1 = multiplicar(6, 4)
    print(f"6 * 4 = {resultado1}")
    
    # Prueba 2: Números negativos
    resultado2 = multiplicar(-5, -3)
    print(f"-5 * -3 = {resultado2}")
    
    # Prueba 3: Número positivo por negativo
    resultado3 = multiplicar(8, -2)
    print(f"8 * (-2) = {resultado3}")
    
    # Prueba 4: Números decimales
    resultado4 = multiplicar(2.5, 4.2)
    print(f"2.5 * 4.2 = {resultado4}")
    
    # Prueba 5: Multiplicación por cero
    resultado5 = multiplicar(15, 0)
    print(f"15 * 0 = {resultado5}")
    
    # Prueba 6: Multiplicación por uno
    resultado6 = multiplicar(7, 1)
    print(f"7 * 1 = {resultado6}")
    
    # Prueba 7: Números grandes
    resultado7 = multiplicar(1000, 2000)
    print(f"1000 * 2000 = {resultado7}")
    
    print("=== PRUEBAS COMPLETADAS ===")