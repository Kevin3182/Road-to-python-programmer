class Human(object):
    def __init__(self, name, age):
        self.name = name
        self.age= age
    
    def say(self):
        print('Hello my name is {}, {}'.format(self.name, self.age))

A = Human('sh',18)
A.say()

B = Human('gg',19)
B.say()