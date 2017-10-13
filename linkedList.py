class Node:
    def __init__(self,data=None,next_node=None):
        self.data = data
        self.next_node = next_node

   '''
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self,next_node):
        self.next_node = next_node
    '''

class LinkedList:
    def __init__(self,head=None,last=None):
        self.head = None
        self.last = None

    def insert(self,data):
        if self.head == None :
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next_node = Node(data)
            self.last = self.last.next_node

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next_node
        return count

    def printList(self):
        current = self.head
        while current != None:
            print(current.data, end = ' ')
            current = current.next_node

    def search(self,num):
        current = self.head
        found = False
        while current and found is False:
            if current.data == num :
                found = True
                print('Found the number:',num)
            else:
                current = current.next_node
        if found is False:
            raise ValueError('The given number is not present in the list')
        return current

    def delete(self,num):
        current = self.head
        previous = None
        if current and current.data == num:
            self.head = current.next_node
            print(num,'has been deleted successfully')
            print('Modified List: ',end = ' ')
            self.printList()
        else:
            while current:
                previous = current
                current = current.next_node
                if current and current.data == num:
                    previous.next_node = current.next_node
                    print(num,'has been deleted successfully')
                    print('Modified List: ',end = ' ')
                    self.printList()
                    break
            if current == None:
                raise ValueError('The given number is not present in the list')
    
                    
        
    
            
        
        
