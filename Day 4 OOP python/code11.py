#polymorphism
class india:

    def currency(self):
        print("indian currency is INR")

    def capital(self):
        print("capital of india is New Delhi")
    
class usa:

    def currency(self):
        print("currency of usa is USD")

    def capital(self):
        print("captial of usa is WDC")


country1=india()
country2=usa()

country1.currency()
country2.currency()

country1.capital()
country2.capital()