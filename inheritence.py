'''class parent():
    def print_last_name(self):
        print('chandel')

class child(parent):

    def print_first_name(self):
        print('Abhishek')

    def print_last_name(self):
        print('Chandu')
       


abhi = child()
abhi.print_first_name()
abhi.print_last_name()'''

#child inherites the attributes inside parent class

#multiple inheritense

class Mario():
    def move(self):
        print(' I am growing')

class Shroom():
    def eat_shroom(self):
        print(' Now I am BIG!')

class BigMario(Mario, Shroom):
    pass

bm = BigMario()
bm.move()
bm.eat_shroom()
