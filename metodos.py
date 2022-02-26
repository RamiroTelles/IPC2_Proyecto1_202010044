
from lista import lista

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