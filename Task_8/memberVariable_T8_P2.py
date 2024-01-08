class myClass:
    num = 33;
    def __privMeth(self):
        print("I’m inside class myClass")
    def hello(self):
        print("Private Variable value: ",myClass.num)
foo = myClass()
foo.hello()
foo.num