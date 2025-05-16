from flask import Flask, render_template, request
from empleado import Empleado
from gerente import Gerente

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('formulario.html')

# Ruta para procesar los datos del formulario
@app.route('/calcular', methods=['POST'])
def calcular():
    nombre = request.form['nombre']
    edad = int(request.form['edad'])
    salario_base = float(request.form['salario_base'])
    tipo_empleado = request.form['tipo_empleado']

    if tipo_empleado == 'gerente':
        bono = float(request.form['bono'])
        empleado = Gerente(nombre, edad, salario_base, bono)
    else:
        empleado = Empleado(nombre, edad, salario_base)

    salario_mensual = empleado.calcular_salario()
    return render_template('resultado.html', nombre=nombre, salario=salario_mensual)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



""" 
empleado1 = Empleado("Juan", 30, 50000)
gerente1 = Gerente("Ana", 35, 60000, 10000)

print(f"{empleado1.nombre}, Salario Base: {empleado1.calcular_salario()}")
print(f"{gerente1.nombre}, Salario Total: {gerente1.calcular_salario()}")

# Polimorfismo
def mostrar_salario(empleado):
    print(f"El sueldo de {empleado.nombre} es de: {empleado.calcular_salario()}")

empleado1 = Empleado("Juan", 30, 50000)
gerente1 = Gerente("Ana", 35, 60000, 10000)

mostrar_salario(empleado1)
mostrar_salario(gerente1)
""" 