from os import system,startfile
from lista import lista
from patron import patron
from pisos import piso
from metodos import metodos


funciones = metodos()


#patron1 = patron("cod24","WBWBWWWB")
#patron2 = patron("Cod25","BBBWW")
patron1 = lista()
p1 = "BBBWW"


for i in p1:
    patron1.agregar_Final(i)

#resultados = funciones.cambiarPatron(5,2,1,patron1,patron2)

#print("Costo total "+ "\""+ str(resultados.getPos(0)) + "\"")

#print("Pasos")
#print("--------------------------------------")
#print(resultados.getPos(1))

funciones.graficarPatron(1,5,patron1)

system("dot -Tpng grafica.dot -o grafica.png")

system('dot -Tpng grafica.dot -o grafica.png')
 
system("cd ./grafica.png")
startfile("grafica.png")