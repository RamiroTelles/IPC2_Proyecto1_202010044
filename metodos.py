
from lista import lista
from patron import patron
from os import system,startfile

class metodos():

    def __init__(self) -> None:
        pass



    def ordenarPiso(self,lista):
        
        for i in range(lista.cant):
            for j in range(lista.cant-1):
                if lista.getPos(j).nombre> lista.getPos(j+1).nombre:
                    aux = lista.getPos(j)
                    lista.remplazar(lista.getPos(j+1),j)
                    lista.remplazar(aux,j+1)
        return lista

    def ordenarPatron(self,lista):
        for i in range(lista.cant):
            for j in range(lista.cant-1):
                if lista.getPos(j).codigo> lista.getPos(j+1).codigo:
                    aux = lista.getPos(j)
                    lista.remplazar(lista.getPos(j+1),j)
                    lista.remplazar(aux,j+1)
        return lista

    def cambiarPatron(self,c,f,s,p1,p2):
        #r = filas
        #c = columnas
        #f = costo voltear
        #s = costo intercambiar
        costoTotal =0
        pasos=''
        aux=""
        patronInicio = lista()
        for i in p1.cadena:
            patronInicio.agregar_Final(i)

        patronFinal = lista()
        for i in p2.cadena:
            patronFinal.agregar_Final(i)

        i=0 
        
        while(i<patronInicio.cant):

            if patronInicio.getPos(i) == patronFinal.getPos(i):
                i+=1
                continue
            else:
                if (i+1)==patronInicio.cant :
                    #voltear.
                    if patronInicio.getPos(i).upper() == 'W':
                        patronInicio.remplazar('B',i)
                    else:
                        patronInicio.remplazar('W',i)
                    pasos += "voltear la posicion " + str(i) +"\n"
                    costoTotal+=f
                    i+=1
                    continue
                elif ((i+1)%c) ==0:
                    if (4*f)>(s*2):
                        if patronInicio.getPos(i+c)== patronFinal.getPos(i) and (i+c)<patronInicio.cant:
                            if patronInicio.getPos(i) == patronFinal.getPos(i+c) and (i+c)<patronInicio.cant:
                                #intercambiar i+c

                                aux = patronInicio.getPos(i)
                                patronInicio.remplazar(patronInicio.getPos(i+c),i)
                                patronInicio.remplazar(aux,i+c)
                                pasos += "Intercambiar celda "+ str(i) + " con celda " + str(i+c)+ "\n"
                                costoTotal+=s

                                i+=1
                                continue
                            elif f>s:
                                #intercambiar i+c

                                aux = patronInicio.getPos(i)
                                patronInicio.remplazar(patronInicio.getPos(i+c),i)
                                patronInicio.remplazar(aux,i+c)
                                pasos += "Intercambiar celda "+ str(i) + " con celda " + str(i+c)+ "\n"
                                costoTotal+=s   

                                i+=1
                                continue
                            else:
                                #voltear.
                                if patronInicio.getPos(i).upper() == 'W':
                                    patronInicio.remplazar('B',i)
                                else:
                                    patronInicio.remplazar('W',i)
                                pasos += "voltear la posicion " + str(i) +"\n"
                                costoTotal+=f
                                i+=1
                                continue
                        else:
                            #voltear.
                            if patronInicio.getPos(i).upper() == 'W':
                                patronInicio.remplazar('B',i)
                            else:
                                patronInicio.remplazar('W',i)
                            pasos += "voltear la posicion " + str(i) +"\n"
                            costoTotal+=f
                            i+=1
                            continue
                    else:
                        #voltear.
                        if patronInicio.getPos(i).upper() == 'W':
                            patronInicio.remplazar('B',i)
                        else:
                            patronInicio.remplazar('W',i)
                        pasos += "voltear la posicion " + str(i) +"\n"
                        costoTotal+=f
                        i+=1
                        continue
                elif (4*f)>(2*s):
                    
                    if (patronInicio.getPos(i+1)==patronFinal.getPos(i)):
                        if(patronInicio.getPos(i)==patronFinal.getPos(i+1)):
                            #intercambiar i+1

                            aux = patronInicio.getPos(i)
                            patronInicio.remplazar(patronInicio.getPos(i+1),i)
                            patronInicio.remplazar(aux,i+1)
                            pasos += "Intercambiar celda "+ str(i) + " con celda " + str(i+1)+ "\n"
                            costoTotal+=s

                            i+=1
                            continue
                        else:
                            if(patronInicio.getPos(i+c)==patronFinal.getPos(i) and (i+c)<patronInicio.cant):
                                if(patronInicio.getPos(i)==patronFinal.getPos(i+c) and (i+c)<patronInicio.cant):
                                        #intercambiar i+c

                                        aux = patronInicio.getPos(i)
                                        patronInicio.remplazar(patronInicio.getPos(i+c),i)
                                        patronInicio.remplazar(aux,i+c)
                                        pasos += "Intercambiar celda "+ str(i) + " con celda " + str(i+c)+ "\n"
                                        costoTotal+=s

                                        i+=1
                                        continue
                                elif (f>s):
                                    #intercambiar i+c

                                    aux = patronInicio.getPos(i)
                                    patronInicio.remplazar(patronInicio.getPos(i+c),i)
                                    patronInicio.remplazar(aux,i+c)
                                    pasos += "Intercambiar celda "+ str(i) + " con celda " + str(i+c)+ "\n"
                                    costoTotal+=s

                                    i+=1
                                    continue
                                else:
                                    #voltear.
                                    if patronInicio.getPos(i).upper() == 'W':
                                        patronInicio.remplazar('B',i)
                                    else:
                                        patronInicio.remplazar('W',i)
                                    pasos += "voltear la posicion " + str(i) +"\n"
                                    costoTotal+=f
                                    i+=1
                                    continue
                            elif (f>s):
                                #intercambiar i+1

                                aux = patronInicio.getPos(i)
                                patronInicio.remplazar(patronInicio.getPos(i+1),i)
                                patronInicio.remplazar(aux,i+1)
                                pasos += "Intercambiar celda "+ str(i) + " con celda " + str(i+1)+ "\n"
                                costoTotal+=s

                                i+=1
                                continue
                            else:
                                #voltear.
                                if patronInicio.getPos(i).upper() == 'W':
                                    patronInicio.remplazar('B',i)
                                else:
                                    patronInicio.remplazar('W',i)
                                pasos += "voltear la posicion " + str(i) +"\n"
                                costoTotal+=f
                                i+=1
                                continue
                    elif(patronInicio.getPos(i+c)==patronFinal.getPos(i) and (i+c)<patronInicio.cant):
                        if(patronInicio.getPos(i)==patronFinal.getPos(i+c) and (i+c)<patronInicio.cant):
                            #intercambiar i+c

                            aux = patronInicio.getPos(i)
                            patronInicio.remplazar(patronInicio.getPos(i+c),i)
                            patronInicio.remplazar(aux,i+c)
                            pasos += "Intercambiar celda "+ str(i) + " con celda " + str(i+c)+ "\n"
                            costoTotal+=s

                            i+=1
                            continue
                        elif(f>s):
                            #intercambiar i+c

                            aux = patronInicio.getPos(i)
                            patronInicio.remplazar(patronInicio.getPos(i+c),i)
                            patronInicio.remplazar(aux,i+c)
                            pasos += "Intercambiar celda "+ str(i) + " con celda " + str(i+c)+ "\n"
                            costoTotal+=s

                            i+=1
                            continue
                        else:
                            #voltear.

                            if patronInicio.getPos(i).upper() == 'W':
                                patronInicio.remplazar('B',i)
                            else:
                                patronInicio.remplazar('W',i)
                            pasos += "voltear la posicion " + str(i) +"\n"
                            costoTotal+=f

                            i+=1
                            continue
                    else:
                        #voltear.

                        if patronInicio.getPos(i).upper() == 'W':
                            patronInicio.remplazar('B',i)
                        else:
                            patronInicio.remplazar('W',i)
                        pasos += "voltear la posicion " + str(i) +"\n"
                        costoTotal+=f

                        i+=1
                        continue

                                


                else:
                    #voltear.

                    if patronInicio.getPos(i).upper() == 'W':
                        patronInicio.remplazar('B',i)
                    else:
                        patronInicio.remplazar('W',i)
                    pasos += "voltear la posicion " + str(i) +"\n"
                    costoTotal+=f

                    i+=1
                    continue

        #
        resultados = lista()
        resultados.agregar_Final(costoTotal)
        resultados.agregar_Final(pasos)
        resultados.agregar_Final(patronInicio)
        return resultados

    def graficarPatron(self,r,c,patron):

        encabezado = '''
digraph L{
    node[shape=box style=filled]
    subgraph cuadro{  
        '''
        cuerpo =""
        #crear nodos
        for i in range(r):
            for j in range(c):
                cuerpo+= "nod"+str(i)+str(j)+"["
                if patron.getPos((i*c)+(j)).upper()=='W':
                    cuerpo+="fillcolor=white,"
                else:
                    cuerpo+="fillcolor=black,"
                cuerpo+="group=" + str(j)+ " label=\"\""
                cuerpo+="]\n"
        cuerpo+="edge[fillcolor=white,color=white]\n"

        for j in range(c):
            for i in range(r-1):
                cuerpo+="nod"+str(i)+str(j)+"->"+ " nod" +str(i+1)+str(j) +"\n"

        pie='''
        }
}'''    
        documento = encabezado + cuerpo + pie
        ruta = "grafica.dot"
        try:
            myfile = open("grafica.dot","w")
            myfile.write(documento)
            myfile.close
        #"dot -Tpng grafica.dot -o grafica.png"
        

        #dot -Tpng C:\Users\ramir\Desktop\grafica.dot -o grafica.png
       
        except:
            print("error")