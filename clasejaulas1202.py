# CLASE
class Jaulas1202:
    # ATRIBUTOS
    def __init__(self, id1202,tipo1202,capacidad1202,tamaño1202,cont_agua1202,cont_com1202,candado1202):
        self.id1202 = id1202
        self.tipo1202 = tipo1202
        self.capacidad1202 = capacidad1202
        self.tamaño1202 = tamaño1202
        self.cont_agua1202 = cont_agua1202
        self.cont_agua1202 =  cont_agua1202
        self.cont_com1202 =  cont_com1202
        self.candado1202 = candado1202
    
    
    # MOSTRAR
    def mostrar(self):
        print(f"ID: {self.id1202}")
        print(f"Tipo: {self.tipo1202}")
        print(f"Capacidad: {self.capacidad1202}")
        print(f"Tamaño: {self.tamaño1202}")
        print(f"Contenido de agua: {self.cont_agua1202}")
        print(f"Contenido de comida: {self.cont_com1202}")
        print(f"Candado: {self.candado1202}")


    # LISTA
    def Adoptantes1202(self):
        MisAdoptantes=["Nicolas","Sebastian","Janna","Ariel","Dulce","Mario","Arath"]
        print(MisAdoptantes)
        for adoptantes in MisAdoptantes:
            print(adoptantes)


    # TUPLA    
    def perros1202(self):
        MisPerros=("Chihuahua","Bulldog","Pug","French Poodle","Pastor Aleman","Rothwiller","Gran Danés")
        print(MisPerros)
        for perros in MisPerros:
            print(perros)
    
    # CONJUNTO
    def empleados1202(self):
        MisEmpleados={"Juan","Pedro","Maria","Luis","Ana","Carlos","Sebastian"}
        print(MisEmpleados)
        for empleados in MisEmpleados:
            print(empleados)
    
    # DICCIONARIO
    def refugios1202(self):
        MisRefugios={"REFUGIO 1":60,
                    "REFUGIO 2": 55,
                    "REFUGIO 3": 63, 
                    "REFUGIO 4": 70,
                    "REFUGIO 5": 54, 
                    "REFUGIO 6": 44,
                    "REFUGIO 7": 46,}
        print(MisRefugios)
        for ref,per in MisRefugios.items():
            print(f"{ref} --- Cantidad de perros:{per}")
    
    # ADOPCION EXITOSA
    def adopcion1202(self):
        print("LA ADOPCION SE REALIZO CON EXITO")
        print("GRACIAS POR LA ADOPCION")
    
    # ADOPCION CANCELADA
    def adopcioncancel1202(self):
        print("LA ADOPCION SE CANCELÓ")
        print("NO SE REALIZO LA ADOPCION")

    

# OBJETO
print("JAULAS")
objeto1202=Jaulas1202(1202,"Normal",30,"Grande", 100, 85, "Normal")
objeto1202.mostrar()
print(" ")
print("INFORMACION DE LOS ADOPTANTES ")
objeto1202.Adoptantes1202()
print(" ")
print("INFORMACION DE LOS PERROS ")
objeto1202.perros1202()
print(" ")
print("INFORMACION DE LOS EMPLEADOS ")
objeto1202.empleados1202()
print(" ")
print("INFORMACION DE LOS REFUGIOS ")
objeto1202.refugios1202()
print(" ")
print("ADOPCION EXITOSA")
objeto1202.adopcion1202()
print(" ")
print("ADOPCION CANCELADA")
objeto1202.adopcioncancel1202()


