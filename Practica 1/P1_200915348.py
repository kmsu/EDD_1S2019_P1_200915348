#creamos clase nodo
#ultimo que entra es el primero en salir
class node:
    def __init__(self, name = None, score = None, next = None): #constructor de clase
        self.data = name #atributo que almacena el dato del nodo
        self.data2 = score
        self.next = next #apuntador a otro objeto de tipo nodo

#creamos clase lista
class pila:
    def __init__(self):
        self.head = None #Creamos un nodo para almacenar el primer nodo de lista

#metodo para agregar un nodo al final de la lista
    def push(self, data, data2):
        if self.head is None:
            self.head = node(name=data, score= data2)
            return
        aux = self.head
        while aux.next:
            aux = aux.next
        aux.next = node(name=data, score = data2)

#metodo para eliminar un nodo al final de la lista
    def pop(self):
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
            temp=self.head
        while temp.next is not None:
            print(temp.data, end = " ")
            print(temp.data2, end = " ")
            print(" ")
            temp=temp.next
        print (temp.data, end = ' ')
        print(temp.data2, end = " ")


s = pila()
s.push("usuario 1", 45)
s.push("usuario 2", 31)
s.print_list()
s.pop()
print(" ")
s.print_list()
