class Empleado:
    def __init__(self, nombre, edad, salario_base):
        self.nombre = nombre
        self.edad = edad
        self.salario_base = salario_base

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, nueva_edad):
        self._edad = nueva_edad

    @property
    def salario_base(self):
        return self._salario_base
    
    @salario_base.setter
    def salario_base(self, nuevo_salario_base):
        self._salario_base = nuevo_salario_base


    def calcular_salario(self):
        return self._salario_base