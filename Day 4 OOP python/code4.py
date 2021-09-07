class codeos:#clas

    def __init__(self):#constructor
        self.event="python"
        self.duration=6

    def update(self):#method
        self.duration=7

bootcamp=codeos()#object

print(bootcamp.event)
print(bootcamp.duration)

bootcamp.update()
print(bootcamp.duration)


print(bootcamp.duration)