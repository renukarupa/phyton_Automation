class Circle:
# constructor
    def __init__(self):
    # initializing instance variable
        self.num=[10,501,22,37,100,999,87,351]

    # a method
    def read_number(self):
        print(self.num)

# creating object of the class. This invokes constructor
obj = Circle()

# calling the instance method using the object obj
obj.read_number()

