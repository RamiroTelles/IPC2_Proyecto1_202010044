from re import I
from numpy import true_divide


from nodo import nodo

class lista:

    def __init__(self) -> None:
        self.inicio = None
        self.cant = 0
        self.vacio = True

    def agregar_inicio(self,dato):
        nuevo = nodo(dato)
        if self.vacio:
            self.inicio = nuevo
            self.cant+=1
            self.vacio = False
        else:
            self.inicio.anterior = nuevo
            nuevo.siguiente = self.inicio
            self.inicio = nuevo
        
    def agregar_Final(self,dato):
        nuevo = nodo(dato)
        if self.vacio:
            self.inicio = nuevo
            self.cant+=1
            self.vacio = False
        else:
            aux = self.inicio

            while(aux.siguiente != None):
                aux = aux.siguiente
            aux.siguiente = nuevo
            nuevo.anterior = aux
            self.cant +=1
        
    
    def remplazar(self,dato,pos):
        nuevo = nodo(dato)
        if not (pos)>(self.cant-1):

            aux = self.inicio
            i=0
            while (i<pos):
                aux = aux.siguiente
            aux.siguiente.anterior = nuevo
            nuevo.siguiente = aux.siguiente
            aux.anterior.siguiente = nuevo
            nuevo.anterior = aux.anterior
            self.vacio = False
        else:
            print("Posicion no existente")

    def buscar(self,dato):
        if self.vacio:
            print("Lista Vacia")
        else:
            aux = self.inicio
            i=0
            if aux.dato == dato:
                return i
            else:
                while(aux.siguiente != None):
                    aux = aux.siguiente
                    i+=1
                    if aux.dato == dato:
                        return i
            return None

    def eliminarPos(self,pos):
        if pos<=(self.cant-1):
            aux = self.inicio
            i=0
            while(i<pos):
                aux = aux.siguiente
            if aux.anterior!= None:
                aux.anterior.siguiente = aux.siguiente
                if aux.siguiente != None:
                    aux.siguiente.anterior = aux.anterior
                else:
                    pass
            else:
                aux.siguiente.anterior = aux.anterior
                self.inicio = aux.siguiente
            
            return True
        else:
            print("posicion no existente")
    
    def eliminarDato(self,dato):
        if self.vacio:
            print("Lista Vacia")
        else:
            aux = self.inicio
            i=0
            if aux.dato == dato:
                aux.siguiente.anterior = None
                self.inicio = aux.siguiente
                return True
            else:
                while(aux.siguiente != None):
                    aux = aux.siguiente
                    i+=1
                    if aux.dato == dato:
                        aux.anterior.siguiente = aux.siguiente
                        if aux.siguiente != None:
                            aux.siguiente.anterior = aux.anterior
                        else:
                            pass
                        return True
            return False
    
    def imprimir(self):
        if self.vacio:
            print("Lista Vacia")
        else:
            aux = self.inicio
            txt = "[ " + str(aux.dato)
            while(aux.siguiente!=None):
                aux = aux.siguiente
                txt+= ", " + str(aux.dato)
            txt+=" ]"
            print(txt)
        
