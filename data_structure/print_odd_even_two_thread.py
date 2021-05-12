import threading

class OddEven:
    eventEven = threading.Event()
    eventOdd = threading.Event()

    def __init__(self, limit):
        self.limit = limit
        self.n = 0
    def showEven(self):
        while self.n < self.limit:
            self.eventEven.wait()
            print(f'E: {self.n}')
            self.n+=1
            self.eventEven.clear()
            self.eventOdd.set()

    def showOdd(self):
        while self.n < self.limit:
            self.eventOdd.wait()
            print(f'O: {self.n}')
            self.n+=1
            self.eventOdd.clear()
            self.eventEven.set()


if __name__ == "__main__":
    limit = 20
    obj = OddEven(limit)
    even = threading.Thread(target= obj.showEven)
    odd = threading.Thread(target= obj.showOdd)
    even.start()
    odd.start()
    OddEven.eventEven.set()
    even.join()
    odd.join()
    print(" execution completed")
