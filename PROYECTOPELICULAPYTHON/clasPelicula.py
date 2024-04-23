class Pelicula:
    #Metodo costructor
    def __init__(self,name,fechaLanzamiento,duracionMinutos,calificacion,calificacionEstrellas,numeroCalificaciones):
        self.name = name
        self.fechaLanzamiento = fechaLanzamiento
        self.duracionMinutos = duracionMinutos
        self.calificacionEstrellas = calificacionEstrellas
        self.numeroCalificaciones = numeroCalificaciones
        self.calificacion = calificacion
        self.calificacionEstrellas = calificacionEstrellas
        self.numeroCalificaciones = numeroCalificaciones

    #Metodos accesore
    def getname(self):
        return self.name
    def getfechaLanamiento(self):
        return self.fechaLanzamiento
    def getduracionMinutos(self):
        return self.duracionMinutos
    def getcalificacionEstrellas(self):
        return self.calificacionEstrellas
    
