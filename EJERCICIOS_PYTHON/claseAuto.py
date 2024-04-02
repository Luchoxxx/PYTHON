
# clase auto:

class auto:
    
    def __init__(self,marca,modelo,motor,tipo_combustible=["gasolina","biotenasol","diesel","gas natural"],tipo_auto=["subcompacto","compacto","familiar","ejecutivo","suvenir"],num_asientos=0,velocidad_max=0,color = ["blanco","Negro","rojo","naranja","amarillo","verde","azul","violeta"],velocidad_actual=0,num_puertas = 0):

        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.color=color
        self.tipo_combustible = tipo_combustible
        self.tipo_auto = tipo_auto
        self.num_asientos = num_asientos
        self.num_puertas = num_puertas
        self.velocidad_max = velocidad_max
        self.velocidad_actual = velocidad_actual
        
 
    # Metodos get y set de la clase auto .
    
    def get_marca(self):
        return self.marca
    def get_modelo(self):
        return self.modelo
    def get_motor(self):
        return self.motor
    def get_color(self):
        return self.color
    def get_tipo_combustible(self):
        return self.tipo_combustible
    def get_tipoAuto(self):
        return self.tipo_auto
    def get_munAsientos(self):
        return self.num_asientos
    def get_puertas(self):
        return self.num_puertas
    def get_velocidad_max(self):
        return self.velocidad_max
    def get_velocidad_actual(self):
        return self.velocidad_actual
    
    #Metodos set 

    def set_marca(self, nueva_marca):
        return self.marca == nueva_marca
    def set_modelo(self, nueva_modelo):
        return self.modelo == nueva_modelo
    def set_motor(self, nueva_motor):
        return self.modelo == nueva_motor
    def set_color(self, nueva_color):
        return self.color ==nueva_color
    def set_tipo_combustible(self, nuevoCombustible):
        return self.tipo_combustible== nuevoCombustible
    def set_tipo_auto(self, nuevoAuto):
        return self.tipo_auto == nuevoAuto
    def set_velocidad(self, nueva_velocidad):
        return self.velocidad_actual == nueva_velocidad
    def set_velocidad_max(self, nueva_maxima):
          return self.velocidad_max == nueva_maxima
    
    # Metodos especiales del auto.
    def acelera_auto(self):

        if self.velocidad_actual > self.velocidad_max:
            return "Limite de velocidad exedido"
        if self.velocidad_actual < 0:
            print("Auto en reposo ")
    def tiempo_llegada(self):
        distancia_llegar = 1524 # Esta en kilometros
        return self.velocidad_actual / distancia_llegar
    
    def IMPRIME_DATOS(self):
        print("""
                marca :{marca}
                modelo:{modelo}
                motor :{motor}
                numero Puertas:{mun_p}
                tipo_combustible :{tipo_combustible}
                tipo_auto:{tipo_auto}

""")

print("Hola mensaje ")
# Pequeño mensaje de comprobacion 
print("------------------------------------------------1")

 
        