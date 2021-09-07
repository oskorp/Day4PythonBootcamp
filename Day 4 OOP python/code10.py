#multiple inheritance
class alien:

    def ego(self):
        print("he can live in space")


class woman:

    def earth(self):
        print("she is smart")

class starlord(alien,woman):

    def galaxy(self):
        print("he is guardian of galaxy")


hero=starlord()
villian=alien()

villian.ego()


hero.earth()
hero.ego()
hero.galaxy()