class grandfather():

    def property1(self):
        print("charchter1")

class father(grandfather):

    def property2(self):
        print("charchter2")

class grandchild(father):
    
    def property3(self):
        print("charchter3")

nana=grandfather()
papa=father()
baccha=grandchild()

nana.property1()

papa.property1()
papa.property2()

baccha.property2()
baccha.property1()
baccha.property3()

