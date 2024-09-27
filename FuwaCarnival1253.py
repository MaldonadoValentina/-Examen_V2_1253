# Zona de Clase 
class FuwaCarnival1253: 
    def diccionario_Cliente1253(self):
        diccCliente1243 = {
            "idC:" : 1273,
            "Nombre:" : "Oracio",
            "Apellidos:" : "Flores Herrera",
            "Sexo:" : "H",
            "Edad:" : 57,
            "CURP:" : "FLO196487MCHLDLP3",
            "No.Telefono:" : "656 780 2396"
        }
        print(diccCliente1243)
        for m,a in diccCliente1243.items():
            print("-", m,a)
    def diccionario_Empleado1253(self):
        diccEmpleado1243 = {
            "idE:" : 2300,
            "Nombre:" : "Paula",
            "Apellidos:" : "Jimenez Palacio",
            "Sexo:" : "M",
            "Edad:" : 26,
            "CURP:" : "JPP100820MCHLDLC8",
            "Fecha de Nacimiento:" : "10/08/2000"
        }
        print(diccEmpleado1243)
        for l,d in diccEmpleado1243.items():
            print("-", l,d)
    def diccionario_Sucursal1253(self):
        diccSucursal1243 = {
            "idS:" : 100801,
            "Nombre:" : "Carnivaleros",
            "Dirección:" : "C.Love #5106",
            "Horarios:" : "13:30 - 18:59",
            "Encargado:" : "Valentina Maldonado Rodriguez",
            "CP:" : 32467,
            "Num.Telefono:" : "614 907 6531"
        }
        print(diccSucursal1243)
        for o,n in diccSucursal1243.items():
            print("-", o,n)
    def diccionario_Producto1253(self):
        diccProducto1243 = {
            "idPr:" : 52000,
            "Nombre:" : "Topper_Chocolate",
            "Descripción:" : "Dulce de Chocolate de la mascota Topper",
            "Precio: $" : 89.04,
            "Cantidad:" : 89,
            "CAD:" : "04/26",
            "Lote:" : "09/08/24"
        }
        print(diccProducto1243)
        for r,z in diccProducto1243.items():
            print("-", r,z)

# Creacion de Objeto
verDicc1253 = FuwaCarnival1253()

# Zona de Uso de Objeto
print("ºDiccionario Tabla Clienteº")
verDicc1253.diccionario_Cliente1253()
print("ºDiccionario Tabla Empleadoº")
verDicc1253.diccionario_Empleado1253()
print("ºDiccionario Tabla Sucursalº")
verDicc1253.diccionario_Sucursal1253()
print("ºDiccionario Tabla Productoº")
verDicc1253.diccionario_Producto1253()
