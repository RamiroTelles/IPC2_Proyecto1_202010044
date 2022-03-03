from lista import lista
from patron import patron
from pisos import piso
from metodos import metodos

funciones = metodos()


patron1 = patron("cod24","WBBBB")
patron2 = patron("Cod25","BBBWW")

resultados = funciones.cambiarPatron(5,1,1,patron1,patron2)

print("Costo total "+ "\""+ str(resultados.getPos(0)) + "\"")

print("Pasos")
print("--------------------------------------")
print(resultados.getPos(1))
