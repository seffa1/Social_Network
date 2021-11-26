import os


def clear():
    os.system('cls')


class Person:
    def __init__(self, name: str, email: str, age: int):
        self.email = email
        self.age = age
        self.name = name
        self.friends = []

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