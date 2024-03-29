#ultimo en entrar es el primero en salir
class node:
    def __init__(self, score = None, next = None): #constructor de clase
        self.data = score #save the value of the node
        self.next = next #apuntador a otro objeto de tipo nodo

#last in, first out
class pila:
    def __init__(self):
        self.head = None #Creamos un nodo para almacenar el primer nodo de lista

#metodo para agregar un nodo al final de la lista
    def push(self, data):
        self.head = node(score=data, next=self.head)

#metodo para eliminar un nodo al final de la lista
    def pop(self):
        self.head = self.head.next

    def clear_list(self):
        self.head = None

#metodo imprimir
    def print_list(self):
        if self.head is None:
            print('Lista Vacia')
        else:
            temp=self.head
            while temp.next is not None:
                print(temp.data, end = " ")
                print(" ")
                temp=temp.next
            print (temp.data, end = ' ')

    def count_list(self):
        size = 1
        if self.head is None:
            print('Lista Vacia')
        else:
            temp=self.head
        while temp.next is not None:
            size = size + 1
            temp=temp.next
        print("EL tamanio de la lista es", end = " ")
        print(size)

s = pila()
s.push(1)
s.push(2)
s.push(3)
s.print_list()
print(" ")
s.pop()
print(" ")
s.print_list()
print(" ")
s.count_list()
s.clear_list()
s.print_list()
