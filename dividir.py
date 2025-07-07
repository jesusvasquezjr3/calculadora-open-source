def dividir(num1, num2):
    """
    Función para dividir dos números
    
    Args:
        num1 (float): Primer número (dividendo)
        num2 (float): Segundo número (divisor)
    
    Returns:
        float: Resultado de la división (num1 / num2)
    
    Raises:
        TypeError: Si los argumentos no son números
        ZeroDivisionError: Si el divisor es cero
    """
    try:
        # Validar que los argumentos sean números
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise TypeError("Los argumentos deben ser números")
        
        # Validar división por cero
        if num2 == 0:
            raise ZeroDivisionError("No se puede dividir entre cero")
        
        resultado = num1 / num2
        return resultado
    
    except Exception as e:
        print(f"Error en la operación de división: {e}")
        raise

# Función de prueba
if __name__ == "__main__":
    # Pruebas unitarias básicas
    print("=== PRUEBAS DEL MÓDULO DIVISIÓN ===")
    
    # Prueba 1: División exacta
    resultado1 = dividir(20, 4)
    print(f"20 / 4 = {resultado1}")
    
    # Prueba 2: División con decimales
    resultado2 = dividir(10, 3)
    print(f"10 / 3 = {resultado2}")
    
    # Prueba 3: División de negativos
    resultado3 = dividir(-15, -3)
    print(f"-15 / -3 = {resultado3}")
    
    # Prueba 4: División positivo entre negativo
    resultado4 = dividir(12, -4)
    print(f"12 / (-4) = {resultado4}")
    
    # Prueba 5: División por uno
    resultado5 = dividir(7, 1)
    print(f"7 / 1 = {resultado5}")
    
    # Prueba 6: División de decimales
    resultado6 = dividir(8.4, 2.1)
    print(f"8.4 / 2.1 = {resultado6}")
    
    # Prueba 7: División por cero (manejo de error)
    try:
        resultado7 = dividir(10, 0)
        print(f"10 / 0 = {resultado7}")
    except ZeroDivisionError as e:
        print(f"Error controlado: {e}")
    
    print("=== PRUEBAS COMPLETADAS ===")