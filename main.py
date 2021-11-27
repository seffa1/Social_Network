import os
from classes import Person

class Person:
    user_ID = 0

    def __init__(self, name: str, email: str, age: int):
        self.email = email
        self.age = age
        self.name = name
        self.friends = []

        Person.user_ID += 1
        self.user_ID = Person.user_ID

    def add_friend(self, friend):
        self.friends.append(friend)

    def info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Email: {self.email}')

    def show_friends(self):
        clear()
        print(f'Friends of {self.name}')
        for friend in self.friends:
            print(friend.name)

    def show_recommended_friends(self):
        pass

def clear():
    os.system('cls')

def build_network():
    user_1 = Person('Sam', 'sameffa@gmail.com', 25)
    user_2 = Person('Zach', 'zacheffa@gmail.com', 31)
    user_3 = Person('Summer', 'sumsegar@gmail.com', 24)
    user_4 = Person('Joe', 'jieeffa@gmail.com', 60)
    user_5 = Person('Kathy', 'kathyeffa@gmail.com', 58)
    user_6 = Person('Casey', 'caseym@gmail.com', 32)
    user_7 = Person('John', 'jdoe@gmail.com', 17)
    user_8 = Person('Jane', 'jdoe1@gmail.com', 16)
    user_9 = Person('Hannah', 'hjeffers@gmail.com', 23)
    user_10 = Person('Zumington', 'hamcube1@gmail.com', 14)





def main():
    pass




if __name__ == '__main__':
    main()
