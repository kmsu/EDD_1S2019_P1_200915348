#creamos clase nodo

class node:
    def __init__(self, name = None, next = None, previous = None): #constructor de clase
        self.data = name #atributo que almacena el dato del nodo
        self.next = next #apuntador a otro objeto de tipo nodo
        self.previous = previous

#creamos clase lista
class circular:
    def __init__(self):
        self.head = None #Creamos un nodo para almacenar el primer nodo de lista
        self.last = None

    def empty(self):
        if self.head == None:
            return True
        else:
            return False
#metodo para agregar un nodo al final de la lista
    def add(self, data):
        if self.head is None:
            self.head = node(data)
            self.last= node(data)
        else:
            aux = node(data)
            aux.next = self.head
            self.head.previous = aux
            self.head = aux
        self.head.previous = self.last
        self.last.next = self.head

    def addNode(self, node):
        if self.head is None:
            self.head = node
            self.head.next = node
            node.previous = self.head
        else:
            temp = self.head
            while temp.next is not self.head:
                temp = temp.next
            temp.next = node
            node.next = self.head
            self.head.previous = node
            node.previous = temp


#metodo para eliminar un nodo al final de la lista
    def delete(self):
        aux = self.head
        previous = None
        while aux.next is not None:
            previous = aux
            aux = aux.next
        if previous is None:
            self.head = None
        else:
            previous.next = None

#metodo imprimir
    def print_list(self):
        if self.head is None:
            print('Lista Vacia')
        else:
            temp = self.head
            while temp.next is not self.head:
                print(temp.data, end = " ")
                print(" ")
                temp=temp.next
            print (temp.data, end = ' ')


s = circular()
#s.add(1)
s.addNode(node(2))
s.addNode(node(3))
s.addNode(node(4))
s.addNode(node(5))
s.print_list()
#print(" ")
#s.print_list()
