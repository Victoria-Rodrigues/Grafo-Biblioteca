class Node:
    def __init__(self, data):
        self.data = data
        self.prox = None

    def __str__(self):
        return str(self.data)

class __fila:
    def __init__(self, data=None, node=None):
        if node:
            self.init = node

        elif data:
            self.init = Node(data)

        else:
            self.init = None

    def printOut(self):
        aux = self.init
        while aux:
            print(aux)
            aux = aux.prox

class Fila(__fila):
    def __init__(self):
        super().__init__()
        self.tam = 0

    def insert(self,data):
        if self.init is None:
            self.init = Node(data)
        else:
            aux = self.init
            parent = None
            while aux:
                parent = aux
                aux = aux.prox

            parent.prox = Node(data)

        self.tam += 1
        return True

    def remove(self):
        aux = self.init
        value = aux.data
        self.init = aux.prox
        self.tam -= 1
        del(aux)
        return value