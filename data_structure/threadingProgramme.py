import threading
import time,concurrent.futures

names = ["dheeraj", "amit", "jaya", "dharmu", "neha", "nidhi", "raju", "kaju", "amju"]
fruits = ["orange", "banana", "apple", "grapes", "mango", "pineapple", "guava", "strawberry", "beetroot", "watermelon"]
animals = ["lion", "tiger", "rabbit", "dog", "horse", "cow", "ox", "bear", "camel", "pig", "donkey", "fox", "kangaroo"]


def showName(arr):
    for i in arr:
        print(i)


one = threading.Thread(target=showName, args=(names,))
two = threading.Thread(target=showName,args=(fruits,))
three = threading.Thread(target=showName,args=(animals,))

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(showName, (names,fruits, animals))

