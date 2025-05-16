from empleado import Empleado

class Gerente(Empleado):
    def __init__(self, nombre, edad, salario_base, bono):
        super().__init__(nombre, edad, salario_base)
        self.bono = bono

    @property
    def bono(self):
        return self._bono
    
    @bono.setter
    def bono(self, nuevo_bono):
        self._bono = nuevo_bono


    def calcular_salario(self):
        return super().calcular_salario() + self._bono