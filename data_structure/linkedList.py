import pdb


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return newnode
        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = newnode
        return newnode

    def insert_at_start(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
        return newnode

    def view(self):
        all = []
        temp = self.head
        while temp is not None:
            all.append(temp.get_data())
            temp = temp.next
        return all

    def middleElement(self):

        currentfast = currentslow = self.head
        while currentfast and currentfast.next:
            currentslow = currentslow.next
            currentfast = currentfast.next.next

        return currentslow.get_data()

    def secondlastElement(self):
        current = self.head
        while current.next.next is not None:
            current = current.next
        return current.get_data()

    def reverseList(self):
        prev = None
        current = self.head

        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        self.head = prev


newlist = LinkedList()

dheeraj = newlist.insert_at_end("Dheeraj")
jaya = newlist.insert_at_end("jaya")
raju = newlist.insert_at_end("Raju")
kaju = newlist.insert_at_end("Kaju")
kaju = newlist.insert_at_end("babu")
mom = newlist.insert_at_start("mummy")
dad = newlist.insert_at_start("Daddy")

print("Dheeraj is pointing at {} ".format(dheeraj.next.get_data()))
print("Jaya is pointing at {} ".format(jaya.next.get_data()))
print("raju is pointing at {} ".format(raju.next.get_data()))
print("mummy is pointing at {} ".format(mom.next.get_data()))
print("daddy is pointing at {} ".format(dad.next.get_data()))

print("whole list {}".format(newlist.view()))
print("middle element of the list is {}".format(newlist.middleElement()))
print("second last element of the list is {}".format(newlist.secondlastElement()))

newlist.reverseList()
print("after reversing the list")
print("Reversed list {}".format(newlist.view()))
print("middle element of the list after reversing is {}".format(newlist.middleElement()))
print("second last element of the list after revesring is {}".format(newlist.secondlastElement()))






