
# Clases en python ejercicios ###
## clase persona #### 

from numpy import double

"""""
class Persona:

    #Metodo costructor ## 

    def __init__(self, nombre, apellidos,dni,año_nacimiento,pais_nacimiento):

        self.nombre = nombre
        self.apellidos = apellidos
        self.año_nacimiento = año_nacimiento
        self.dni = dni
        self.pais_nacimiento = pais_nacimiento
        self.genero = chr(35)

    def imprime_datos(self):

        print(
              Datos de mi usuario:
              nombre: {nombre}
              apellidos: {apellidos}
              DNI: {dni}
              Año_nacimiento: {año_nacimiento}
              Pais de nacimiento:{pais_nacimiento}
              Genero:{genero}
              .format(nombre=self.nombre,apellidos=self.apellidos,dni=self.dni,año_nacimiento=self.año_nacimiento,pais_nacimiento=self.pais_nacimiento,genero=self.genero))

"""

    ### La clase planeta ### 

class planeta:
    
    def __init__(self,nombre=str(None),n_satelites=0,masa_planeta=float(0),volumen=float(0),diametro= 0,distance_sol=0,tipo_planeta=["gaseoso","terrestre","Enano"],observable=False):
        
        self.nombre =nombre
        self.n_satelites= n_satelites
        self.masa_planeta = masa_planeta
        self.volumen = volumen
        self.diametro = diametro
        self.distance_sol = distance_sol
        self.tipo_planeta = tipo_planeta
        self.observable = observable

    #Este metodo imprime todos los carateristicas del planeta ##
    def imprime_atributos(self):
        print("""
              Carateristicas del planeta. 
              Nombre:{nombre}
              Numeros de satelites:{n_satelites}
              Masa: {masa_planeta}
              Volumen: {volumen}
              Diametro: {diametro}
              Distance al sol: {distance_sol}
              Tipo de planeta: {tipo_planeta}
              Observable: {observable}  
              """.format(nombre=self.nombre,n_satelites = self.n_satelites,masa_planeta = self.masa_planeta,volumen=self.volumen,diametro=self.diametro,distance_sol=self.distance_sol,tipo_planeta=self.tipo_planeta,observable=self.observable))

    #Method the class planeta

    def densidad_planeta(self):
        return self.masa_planeta/self.volumen
    def Evaluar_planeta(self):
        unidad_astronomica =149597870 # estos estan  en KM
        if self.distance_sol >= (2.1*unidad_astronomica) or self.distance_sol < (3.4*unidad_astronomica):
            return f"PLANETA¨{self.nombre} FUERA DEL SISTEMA SOLAR"
        else:
            print("Planeta dentro del sistema solar")   
    
    "Agregando un pequeño codigo de testeo "
    print("Agregando comentario ")
 