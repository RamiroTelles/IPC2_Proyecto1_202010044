from lista import lista
import xml.etree.ElementTree as ET
from pisos import piso
from patron import patron
from metodos import metodos

def menu():
    funciones = metodos()
    while True:
        print("------------------------------------------------------------------------------------------")
        print("1.Cargar Archivo")
        print("2.Lista de pisos")
        print("3.Salir")
        print("------------------------------------------------------------------------------------------")
        print("Seleccione una opcion")
        print("------------------------------------------------------------------------------------------")
        x = input()
        
        if x=='1':
            print("Cargar Archivos")
            tree= ET.parse("pruebas.xml")

            raiz = tree.getroot()

            pisos = lista()
            for obj in raiz:
                nombre = obj.get('nombre')
                r_var = obj[0].text.strip()
                c_var = obj[1].text.strip()
                f_var = obj[2].text.strip()
                s_var = obj[3].text.strip()
                patrones = lista()
                for i in obj[4]:
                    pat= patron(i.get('codigo'),i.text.strip())
                    patrones.agregar_Final(pat)
                patrones =funciones.ordenarPatron(patrones)
                nuevo =piso(nombre,r_var,c_var,f_var,s_var,patrones)
                pisos.agregar_Final(nuevo)
            pisos = funciones.ordenarPiso(pisos)
        elif x=='2':
        
            print("Lista de pisos")
            print("------------------------------------------------")
            for i in range(pisos.cant):
                print("Piso ", (i+1))
                print("R: " + str(pisos.getPos(i).R))
                print("C: " + str(pisos.getPos(i).C))
                print("F: " + str(pisos.getPos(i).F))
                print("S: " + str(pisos.getPos(i).S))
                for j in range(pisos.getPos(i).patrones.cant):
                    print("patron :", (j+1))
                    print(pisos.getPos(i).patrones.getPos(j).codigo)
                    print(pisos.getPos(i).patrones.getPos(j).cadena)
                print("---------------------------------------------------------")
            listaPisos(pisos)
        elif x=='3':
            print("Saliendo")
            break
        else:
            print("Seleccione una opcion Válida")


def listaPisos(pisos):
    
    while(True):

        print("------------------------------------------------------------------------------------------")
        i=0
        while(i<pisos.cant):
            print(str(i)+ ". "+ str(pisos.getPos(i).nombre))
            i+=1
        print(str(i)+ ". Volver")
       # for i in range(pisos.cant):
          #  print(str(i)+ ". "+ str(pisos.getPos(i).nombre))

        print("------------------------------------------------------------------------------------------")
        print("Seleccione un piso")
        x = input()
        if x.isdigit:
            x = int(x)
            if(x!=i):
                if(x<pisos.cant):
                    #listaPatrones(pisos.getPos(x))
                    opcionPisos(pisos.getPos(x))
                    pass
            else:
                break

            pass
        else:
            print("Seleccione una opcion válida")

def opcionPisos(piso):
     while True:
        print("------------------------------------------------------------------------------------------")
        print("1.Mostrar grafica del patron")
        print("2.Cambiar patron")
        print("3.Salir")
        print("------------------------------------------------------------------------------------------")
        print("Seleccione una opcion")
        print("------------------------------------------------------------------------------------------")
        x = input()
        
        if x=='1':
            print("------------------------------------------------------------------------------------------")
            print("Seleccione el patron a mostrar graficamente")
            print("------------------------------------------------------------------------------------------")
            patron1 = listaPatrones(piso)
            print("Mostrar Graficamente")

            pass
        elif x=='2':
            print("------------------------------------------------------------------------------------------")
            print("Seleccione el patron de inicio")
            print("------------------------------------------------------------------------------------------")
            patron1 = listaPatrones(piso)

            print("------------------------------------------------------------------------------------------")
            print("Seleccione el patron final")
            print("------------------------------------------------------------------------------------------")
            patron2 = listaPatrones(piso)

            print("ordenando")
            pass
           
        elif x=='3':
            print("Saliendo")
            break
        else:
            print("Seleccione una opcion Válida")




def listaPatrones(piso):
    while(True):
        print("------------------------------------------------------------------------------------------")
        i=0
        while(i<piso.patrones.cant):
            print(str(i)+ ". "+ str(piso.patrones.getPos(i).codigo))
            print(str(piso.patrones.getPos(i).cadena))
            i+=1
        print("------------------------------------------------------------------------------------------")
        
        x = input()
        if x.isdigit:
            x = int(x)
            
            if(x<piso.patrones.cant):
                return x
                pass
            else:
                print("Seleccione una opcion válida")
                continue
            

            pass
        else:
            print("Seleccione una opcion válida")
            continue
        
menu()

#elemento = pisos.getPos(3)
#print(str(elemento.nombre))
#print("------------------------------------------------")
#for i in range(pisos.cant):
#    print("Piso ", (i+1))
#    print("R: " + str(pisos.getPos(i).R))
#    print("C: " + str(pisos.getPos(i).C))
#    print("F: " + str(pisos.getPos(i).F))
#    print("S: " + str(pisos.getPos(i).S))
#    for j in range(pisos.getPos(i).patrones.cant):
#        print("patron :", (j+1))
#        print(pisos.getPos(i).patrones.getPos(j).codigo)
#        print(pisos.getPos(i).patrones.getPos(j).cadena)
#    print("---------------------------------------------------------")

