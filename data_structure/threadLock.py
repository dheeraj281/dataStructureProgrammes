import threading, concurrent.futures
import time


class Database:

    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update(self, name):
        print("executing thread {}".format(name))
        print("before acquiring lock")
        with self._lock:
            print(" Thread {} acquired the lock".format(name))
            local_copy = self.value
            local_copy = local_copy + 1
            time.sleep(3)
            self.value = local_copy
            print("Thread {} is going to release the lock".format(name))
        print("Thread {} has released the lock".format(name))


database = Database()
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    for i in range(1,3):
        executor.submit(database.update, i)
print("Testing update. Ending value is %d.", database.value)
