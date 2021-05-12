#### reverse a string using recursion #####


def reverseWithRecursion(data):

    size = len(data)

    if size == 0:
        return

    print(data[size-1], end="")
    reverseWithRecursion(data[0:size-1])


### reverse a string using stack ##########


class Stack:

    def __init__(self):
        self.item = []

    def push(self,data):
        self.item.append(data)

    def pop(self):
        if self.item == []:
            return None
        else:
            return self.item.pop()

    def isEmpty(self):
        return self.item == []


def reverse(mystr):
    stack = Stack()
    newstr = ""
    for i in mystr:
        stack.push(i)

    while not stack.isEmpty():
        newstr += stack.pop()
    return newstr

if __name__ == "__main__":
    print(reverse("dheeraj"))




