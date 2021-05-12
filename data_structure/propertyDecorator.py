class Details:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, newname):
        self.__name = newname
    @name.deleter
    def name(self):
        del self.__name

obj = Details("Dheeraj")

print(obj.name)

obj.name = "Jaya"

print(obj.name)

del obj.name
print(obj.name)
