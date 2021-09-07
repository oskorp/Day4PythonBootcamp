#parameterized constructor

class engg:

    coll="kelkar"#class variable

    def __init__(self,s1,s2,s3):
        self.s1=s1 #instance variables
        self.s2=s2
        self.s3=s3

    def calculate(self):
        return((self.s1+self.s2+self.s3)/3)

omkar=engg(94,76,94)
sneha=engg(98,93,94)
tejas=engg(91,88,86)

print(omkar.calculate())
print(sneha.calculate())
print(tejas.calculate())

print(omkar.coll)
print(sneha.coll)
print(tejas.coll)


