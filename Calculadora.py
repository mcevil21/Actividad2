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