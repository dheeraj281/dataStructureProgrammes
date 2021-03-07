

class Queue():

    def __init__(self,maxsize):
        self.__maxSize = int(maxsize)
        self.__elements = [None] * int(maxsize)
        self.__rear = -1
        self.__head = 0

    def is_full(self):
        '''Will be used while adding values to the queue. It should not be true for a successfull add operation'''
        return self.__rear == self.__maxSize -1

    def is_empty(self):
        '''Will be used while deleting the value from queue. it should not be empty for succesful pop opertion'''
        if (self.__rear == -1 or self.__head == self.__maxSize):
            return True
        else:
            return False

    def add_to_queue(self, value):
        if self.is_full():
            print ("Queue is full. Element cannot be added further.")
        else:
            self.__rear+=1
            self.__elements[self.__rear] = value
            print("{} is added at {}th posistion in the queue".format(value,self.__rear))

    def pop(self):
        if self.is_empty():
            print("queue is already empty")
        else:
            data = self.__elements[self.__head]
            self.__elements= self.__elements[1:]+[None]
            self.__rear -= 1
            return data

    def viewData(self):
        if self.is_empty():
            print("queue is already empty")
        else:
            ele = []
            for i in range(self.__head, self.__rear + 1):
                ele.append(self.__elements[i])
            print(ele)



size = input("Enter the size of queue.")
new = Queue(size)

while True:
    print("push <value>")
    print("view data")
    print("quit")
    do= input("What would you like to do?").split()

    operation= do[0].strip().lower()
    if operation== "push":
       new.add_to_queue(do[1])
    elif "view" in operation:
        new.viewData()
    elif operation == "pop":
        print ("Item {} is taken out from the queue".format(new.pop()))
    elif operation=="quit":
        break
    else:
        print("Invalid input.")



