from Calculadora import Calculadora
if __name__ == "__main__":
    try:
        numero1 = float(input("Ingrese numero1: "))
        numero2 = float(input("Ingrese numero2: "))
        calc = Calculadora()
        resultado = calc.proceso(numero1, numero2)
        print(f"Resultado: {resultado}")
    except ValueError as e:
        print(f"Error: {e}")