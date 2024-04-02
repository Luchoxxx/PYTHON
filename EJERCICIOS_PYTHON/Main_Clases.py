
## Creacuion de la istancia de dos personas ## 
#from ClasePersona import Persona
from ClasePersona import planeta 

#persona1 = Persona("Luis","Fernandez",74384348,"09/02/2002","Peru")
#persona2 = Persona("Liz","Fernandez",74382448,"31/08/2008","Peru")

#persona1.imprime_datos()
#persona2.imprime_datos()


# instancia de la clase planeta 

Oplaneta1 = planeta("pluton",3,46455.7,535445,5677748447464,46464664646,"Gaseoso",True)
Oplaneta2 = planeta("Tierra",1,46455.7,531145,5677748232724,46656764342,"Terrestre",True)

Oplaneta1.imprime_atributos()
Oplaneta2.imprime_atributos()
print(Oplaneta1.Evaluar_planeta())
print(Oplaneta2.Evaluar_planeta())
print(Oplaneta1.densidad_planeta())
print(Oplaneta2.densidad_planeta())