from lista import lista
from patron import patron
from pisos import piso
from metodos import metodos

funciones = metodos()


patron1 = patron("cod25","WBWBWWWB")
patron2 = patron("Cod24","WBWBWWWB")
patron3 = patron("cod13","WBWBWWWB")
patron4 = patron("cod14","WBWBWWWB")

patron5 = patron("cod15","WBWBWWWB")
patron6 = patron("cod16","WBWBWWWB")
patron7 = patron("cod17","WBWBWWWB")
patron8 = patron("cod18","WBWBWWWB")

patrones1 = lista()
patrones1.agregar_Final(patron1)
patrones1.agregar_Final(patron2)
patrones1.agregar_Final(patron3)
patrones1.agregar_Final(patron4)

patrones2 = lista()
patrones2.agregar_Final(patron5)
patrones2.agregar_Final(patron6)
patrones2.agregar_Final(patron7)
patrones2.agregar_Final(patron8)


piso1 = piso("abc",1,1,1,1,patrones1)
piso2 = piso("dfg",1,1,1,1,patrones2)
piso3 = piso("hif",1,1,1,1,patrones1)
piso4 = piso("ABC",1,1,1,1,patrones2)

pisos = lista()
pisos.agregar_Final(piso1)
pisos.agregar_Final(piso2)
pisos.agregar_Final(piso3)
pisos.agregar_Final(piso4)


pisos.getPos(0).patrones = funciones.ordenarPatron(pisos.getPos(0).patrones)


pisos = funciones.ordenarPiso(pisos)

print("------------------------------------------------")
for i in range(pisos.cant):

    print("Piso ", (i+1))
    print(pisos.getPos(i).nombre)
    #print("R: " + str(pisos.getPos(i).R))
    #print("C: " + str(pisos.getPos(i).C))
    #print("F: " + str(pisos.getPos(i).F))
    #print("S: " + str(pisos.getPos(i).S))
    for j in range(pisos.getPos(i).patrones.cant):
        print("patron :", (j+1))
        print(pisos.getPos(i).patrones.getPos(j).codigo)
        print(pisos.getPos(i).patrones.getPos(j).cadena)
    print("---------------------------------------------------------")