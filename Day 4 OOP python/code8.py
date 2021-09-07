#single level inheritance

class father:

    def skills(self):
        print("he can play piano")
    

class child(father):

    def skillsupgrade(self):
        print("he can play guitar")

dad=father()
son=child()

dad.skills()
son.skillsupgrade()
son.skills()
dad.skillupgrade()
    
