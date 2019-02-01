class nldc:

    def __init__(self):
        print("this is to make loop for storing data found by csv file")

    def demand(self):
        print('this is for demand')

    def supply(self):
        print('this is for supply')

class Enemy:
    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)

jason = Enemy(13)
Sandy = Enemy(18)

jason.get_energy()
Sandy.get_energy()
