class Calculadora:
    def multiplicacion(self, numero1, numero2):
        return numero1 * numero2
    def division(self, numero1, numero2):
        if numero2 == 0:
            raise ValueError("No se puede dividir por cero.")
        return numero1 / numero2
    def proceso(self, numero1, numero2):
        """Decide qué operación realizar basándose en el valor de `numero2`."""
        if numero2 == 0:
            if numero1 == 0:
                raise ValueError("La operación 0/0 no está definida.")
            else:
                return self.division(numero1, numero2)
        else:
            return self.multiplicacion(numero1, numero2)
if __name__ == "__main__":
    try:
        numero1 = float(input("Ingrese numero1: "))
        numero2 = float(input("Ingrese numero2: "))
        calc = Calculadora()
        resultado = calc.proceso(numero1, numero2)
        print(f"Resultado: {resultado}")
    except ValueError as e:
        print(f"Error: {e}")