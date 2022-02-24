from lista import lista
import xml.etree.ElementTree as ET
from pisos import piso
from patron import patron

def menu():
    
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
                nuevo =piso(nombre,r_var,c_var,f_var,s_var,patrones)
                pisos.agregar_Final(nuevo)

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
                    listaPatrones(pisos.getPos(x))
                pass
            else:
                break

            pass
        else:
            print("Seleccione una opcion válida")

def listaPatrones(piso):
    while(True):
        print("------------------------------------------------------------------------------------------")
        i=0
        while(i<piso.patrones.cant):
            print(str(i)+ ". "+ str(piso.patrones.getPos(i).codigo))
            print(str(piso.patrones.getPos(i).cadena))
            i+=1
        print(str(i)+ ". Volver")
      

        print("------------------------------------------------------------------------------------------")
        print("Seleccione el patron de inicio")
        x = input()
        if x.isdigit:
            x = int(x)
            if(x!=i):
                if(x<piso.patrones.cant):
                    pass
                else:
                    print("Seleccione una opcion válida")
                    continue
            else:
                break

            pass
        else:
            print("Seleccione una opcion válida")
            continue
        print("------------------------------------------------------------------------------------------")
        i=0
        while(i<piso.patrones.cant):
            print(str(i)+ ". "+ str(piso.patrones.getPos(i).codigo))
            print(str(piso.patrones.getPos(i).cadena))
            i+=1
        print(str(i)+ ". Volver")
      

        print("------------------------------------------------------------------------------------------")
        print("Se seleccionó como patron inicio:")
        print(str(piso.patrones.getPos(x).codigo))
        print(str(piso.patrones.getPos(x).cadena))
        print("------------------------------------------------------------------------------------------")
        print("Seleccione el patron Final")
        y = input()
        if y.isdigit:
            y = int(y)
            if(y!=i):
                if(y<piso.patrones.cant):
                    pass
                else:
                    print("Seleccione una opcion válida")
                    continue
            else:
                break

            pass
        else:
            print("Seleccione una opcion válida")
            continue
        print("------------------------------------------------------------------------------------------")
        print("Se seleccionó como patron Final:")
        print(str(piso.patrones.getPos(x).codigo))
        print(str(piso.patrones.getPos(x).cadena))
        print("------------------------------------------------------------------------------------------")
        print("Cambiando el patron ")
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

