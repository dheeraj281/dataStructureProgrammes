
################### Linked List Implementation with python #####################

# The link list is a sequence of nodes having a similar data type, each node contains one data object and pointer to the next node.

# A linked list is a linear data structure with the collection of multiple nodes. Where each element stores its own data and a pointer to the location of the next element.
# The last link in a linked list points to null, indicating the end of the chain.


class Node():

    ''' For creating a Linked List, we create a node class which holds the info of next node attached to the object
            and create another class to use this node object.
            '''

    def __init__(self,data=None,next_node=None):
        self.data = data
        self.next = next_node

    def get_data(self):
        print("current data from get data method is {}".format(self.data))
        return self.data

    def set_next(self,node):
        self.next = node

    def __repr__(self):
        return ("{}".format(self.data))


# Implementation of link list consists of the following functionality in a linked list

# 1. Insert: This method will insert a new node in a linked list.
# 2. Size: This method will return the size of the linked list.
# 3. Search: This method will return a node containing the data, else will raise an error
# 4. Delete: This method will delete a node containing the data, else will raise an error.

class LinkedList():
    ''' This class will be used to create the list and perform operations on the list '''

    def __init__(self):
        '''  Init method is used for the initialization of a
              class variable if the list has no nodes it is set to none.'''
        self.start = None

    def insert(self,new_value):
        ''' inserting values in the linked list. as of now it adds value at the start of the list. '''
        new_node = Node(new_value, self.start) #creating a node object with the new data. giving data and start node as argument.
        self.start = new_node # assigning the new object to the current head which was none by default.
        print("currently playing song {}".format(self.start))

    def see_next(self):
        ''' To check wif the current node is pointing to which node in the next attribute '''
        current_node = self.start
        print("Next song is {}".format(current_node.next))

    def view(self):
        '''To see all the data added in the linked list. In other word, to traverse throguh the list'''
        lv = []
        if self.start == None:
            print("list is empty! No value")
        else:
            temp = self.start
            print(temp)
            while temp != None:
                lv.append(temp)
                temp = temp.next
            print(lv)

    def deletefirst(self,nodeName=None):
        ''' To delete the given node in the list. assign its node pointer to the next node '''
        if self.start == None:
            print("List is empty. Delete is not allowed")
        else:
            temp= self.start
            while temp and temp.next:
                if temp.next.get_data() == nodeName:
                    temp.next = temp.next.next
                    break
                else:
                    temp= temp.next
            else:
                print("The requested is not found in the list")


my_list = LinkedList()


for val in ["Dheeraj","dharmu", "neha", "Amit", "jaysheel", "vimay", "nidhi", "Raj"]:
    print("################################")
    my_list.insert(val)
    my_list.see_next()
    my_list.view()

my_list.deletefirst(nodeName="Amit")
my_list.view()




