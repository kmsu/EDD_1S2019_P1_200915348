#ultimo en entrar es el primero en salir
class node:
    def __init__(self, score_x = None, score_y = None, next = None): #constructor de clase
        self.data_x = score_x #save the value of the node
        self.data_y = score_y
        self.next = next #apuntador a otro objeto de tipo nodo

#last in, first out
class pila:
    def __init__(self):
        self.head = None #Creamos un nodo para almacenar el primer nodo de lista

#metodo para agregar un nodo al final de la lista
    def push(self, data_X, data_y):
        self.head = node(score_x = data_X, score_y = data_y, next=self.head)

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
                print(temp.data_x, end = " ")
                print(temp.data_y, end = " ")
                print(" ")
                temp=temp.next
            print (temp.data_x, end = ' ')
            print (temp.data_y, end = ' ')

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

#s = pila()
#s.push(1,1)
#s.push(2,1)
#s.push(3,1)
#s.print_list()
#print(" ")
#s.pop()
#s.pop()
#s.pop()
#print(" ")
#s.print_list()
#print(" ")
#s.count_list()
#s.clear_list()
#s.print_list()
