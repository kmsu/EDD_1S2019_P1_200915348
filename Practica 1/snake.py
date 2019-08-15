import os.path
import sys

class node:
    def __init__(self, name_x = 0, name_y = 0, next = None, previous = None): #constructor de clase
        self.data_x = name_x #atributo que almacena el dato del nodo
        self.data_y = name_y
        self.next = next #apuntador a otro objeto de tipo nodo
        self.previous = previous

#creamos clase lista
class doubleLinkedList:
    def __init__(self):
        self.head = None #Creamos un nodo para almacenar el primer nodo de lista
        self.last = None

    def empty(self):
        if self.head == None:
            return True
        else:
            return False
#metodo para agregar un nodo al inicio de la lista
    def add(self, data):
        if self.head is None:
            self.head = node(data)
            self.last= node(data)
        else:
            aux = node(data)
            aux.next = self.head
            self.head.previous = None
            self.head = aux
        self.head.previous = None
        self.last.next = None

#Agregar al inicio con nodo
    def addNodeAtStart(self, node):
        if self.head is None:
            self.head = node
            self.last = node
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node

#Agregar al final con nodo
    def addNodeAtEnd(self, node):
        if self.head is None:
            self.head = node
            self.last = node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node
            node.previous = temp
            self.last = node

    def getHead(self):
        return self.head

    def getLast(self):
        return self.last

#metodo para eliminar un nodo al final de la lista
    def deleteBad(self):
        aux = self.head
        previous = None
        while aux.next is not None:
            previous = aux
            aux = aux.next
        if previous is None:
            self.head = None
        else:
            previous.next = None

    def delete(self):
        self.last = self.last.previous
        self.last.next = None


#metodo imprimir
    def print_list(self):
        if self.head is None:
            print('Lista Vacia')
        else:
            temp = self.head
            while temp.next is not None:
                print(temp.data_x, end = " ")
                print(temp.data_y, end = " ")
                print(" ")
                temp=temp.next
            print (temp.data_x, end = ' ')
            print (temp.data_y, end = ' ')

    def printHead(self):
        print(str(self.head.data_x), end = " ")
        print(str(self.head.data_y), end = " ")


    def startSnake(self):
        self.addNodeAtStart(node(1,1)) #head of the list
        self.addNodeAtStart(node(2,1))
        self.addNodeAtStart(node(3,1))
        #self.addNodeAtEnd(node(6,1))
        #self.addNodeAtEnd(node(5,1))
        #self.addNodeAtEnd(node(4,1))
        #self.addNodeAtEnd(node(3,1))
        #self.addNodeAtEnd(node(2,1))
        #self.addNodeAtEnd(node(1,1))

    def addList(self, x, y):
        self.addNodeAtEnd(node(x,y))

#metodo imprimir
    def print_snake(self):
        self.addNode(node(1,3))
        self.addNode(node(1,2))
        self.addNode(node(1,1))
        val = ""
        if self.head is None:
            print('Lista Vacia')
        else:
            temp = self.head
            while temp.next is not None:
                #print(temp.data, end = " ")
                val = val + temp.data
                #print(" ")
                temp=temp.next
            val = val + temp.data
            #print (temp.data, end = '')
        return val

    def print_list_revers(self):
        if self.head is None:
            print('Lista Vacia')
        else:
            temp = self.last
            #while temp.next is not None:
            #    temp=temp.next
            #self.head = temp
            while temp.previous is not None:
                print(temp.data_x, end = " ")
                print(temp.data_y, end = " ")
                print(" ")
                temp=temp.previous
            print(temp.data_x, end = " ")
            print(temp.data_y, end = " ")

    def print_list_graphiz(self):
        if self.head is None:
            print('Lista Vacia')
        else:
            temp = self.head
            while temp.next is not self.head:
                print(temp.data, end = " ")
                print(" ")
                temp=temp.next
            print (temp.data, end = ' ')

    def archivo(self, nameFile):
        with open(nameFile) as file:
            reader = csv.reader(file)
            next(file)
            for row in reader:
                self.addNode(node(row[0]))

    def insertarNodo(self):
        self.addNode(node("#"))

    def sizeSnake(self):
        size = 0
        if self.head is None:
            #print('Lista Vacia')
            size = 0
        else:
            temp = self.head
            while temp is not None:
                size += 1
                temp=temp.next
        return size

    def clear_list(self):
        self.head = None
        #self.startSnake()

    def snakeReport(self):
        node = self.head
        if node is None:
            print_center(s, "list empty")
        else:
            #Create report by graphiz
            f = open('snakeList.dot', 'w')
            f.write('digraph snake{\n')
            f.write('node [shape=record];\n')
            f.write('rankdir=LR;\n')
            f.write('node0 -> nodei;')
            f.write('nodei [label = "null"];')
            #temp=node
            count = 0
            #print(str(node.data_x))
            #print(str(node.data_y))
            while node.next is not None:
                f.write('node{} [label=\"{}\"];\n'.format(count, "(" + str(node.data_x) + "," + str(node.data_y) + ")"))
                count += 1
                f.write('node{} -> node{};\n'.format(count-1, count))
                f.write('node{} -> node{};\n'.format(count, count-1))
                node = node.next
            f.write('node{} [label = \"{}\"];\n'.format(count, "(" + str(node.data_x) + "," + str(node.data_y) + ")"))
            f.write('nodef [label = "null"];')
            f.write('node'+ str(count) + ' -> nodef;\n')
            f.write('}')
            f.close()
            os.system('dot snakeList.dot -Tpng -o snakeList.png')
            os.system('snakeList.png')

#PROBAR OBTENER EL ULTIMO ANTES DE TRABAJAR EN LA CLASE PRINCIPAL

#s = doubleLinkedList()
#s.startSnake()
#print(str(s.sizeSnake()))
#s.addList(5,4)
#s.archivo()
#s.insertarNodo("juan")
#s.insertarNodo("pedro")
#s.insertarNodo("neto")
#s.addNodeAtStart(node(0,0))
#s.addNodeAtStart(node(0,1))
#s.addNodeAtStart(node(1,1))

#s.print_list()
#s.printHead()
#print(" ")
#print(" ")
#s.clear_list()
#s.print_list_revers()
#s.delete()
#s.print_list()
