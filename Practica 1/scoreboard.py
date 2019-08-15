
#primero que entra es el primero en salir
class node:
    def __init__(self, name = None, score = None, next = None): #constructor de clase
        self.data = name #atributo que almacena el dato del nodo
        self.data2 = score
        self.next = next #apuntador a otro objeto de tipo nodo

#creamos clase lista
class queue:
    def __init__(self):
        self.head = None #Creamos un nodo para almacenar el primer nodo de lista

#metodo para agregar un nodo al final de la lista
    def enqueue(self, data, data2):
        if self.head is None:
            self.head = node(name=data, score= data2)
            return
        aux = self.head
        while aux.next:
            aux = aux.next
        aux.next = node(name=data, score = data2)

#metodo para eliminar un nodo al inicio de la lista
    def dequeue(self):
        self.head = self.head.next

    def queue_count(self):
        size = 1
        if self.head is None:
            size = 0
        else:
            temp=self.head
            while temp.next is not None:
                size = size + 1
                temp=temp.next
        return size

    def count_list(self):
        size = 1
        if self.head is None:
            #print('Lista Vacia')
            size = 0
        else:
            temp=self.head
            while temp.next is not None:
                size = size + 1
                temp=temp.next
        #print("EL tamanio de la lista es", end = " ")
        #print(size)
        return size

    def getHead(self):
        return self.head

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

#s = queue()
#s.enqueue("juan", 1)
#s.enqueue("Pedro", 2)
#s.enqueue("Esteban", 3)
#s.print_list()
#print(" ")
#s.dequeue()
#s.print_list()
#print("Tamanio: ", end = ' ')
#count = s.queue_count()
#print(str(count))
#s.queue_count()
