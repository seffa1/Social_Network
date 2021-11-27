import os
import random
from collections import deque

def clear():
    os.system('cls')


class User:
    user_ID = 0

    def __init__(self, name: str, email: str, age: int, gender: str):
        self.email = email
        self.age = age
        self.name = name
        self.gender = gender
        self.friends = {}

        User.user_ID += 1
        self.user_ID = User.user_ID

    def add_friend(self, friend, weight):  # weight represents how much you interact with that friend
        self.friends[friend] = weight

    def info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Email: {self.email}')
        print(f'Gender: {self.gender}')

    def show_friends(self):
        clear()
        print(f'Friends of {self.name}:')
        for friend in self.friends:
            print(friend.name)

    def show_recommended_friends(self):
        pass

    def __repr__(self):
        print(f'User ID: {self.user_ID}')
        print(f'User Email: {self.email}')


class Network_Generator:
    user_list = {}  # User_ID : User Object
    name_list = deque()
    email_list = deque()
    age_list = deque()
    gender_list = deque()

    @classmethod
    def generate_user_info(cls, user_amount):
        print(f'Generating info for {user_amount} users...')
        n = 0
        while n <= user_amount:
            with open('names.txt', 'r') as name_file:
                for name in name_file.readlines():
                    # Adds user's name to the name list
                    cls.name_list.append(str(name))

                    # Builds a random email address for each person and adds it to the list
                    email = ''
                    email += str(name)[0]
                    random_name = random.choice(list(name_file))
                    email += str(random_name)
                    random_num = random.randint(0, 99)
                    email += str(random_num)
                    email += '@gmail.com'
                    cls.email_list.append(email)

                    # Adds age and gender to the list
                    cls.age_list.append(random.randint(14, 90))
                    cls.gender_list.append(random.choice(['m', 'f']))
                    n += 1

    @classmethod
    def generate_users(cls):
        while len(cls.name_list) > 0:
            name = cls.name_list.pop()
            email = cls.email_list.pop()
            age = cls.age_list.pop()
            gender = cls.gender_list.pop()
            user = User(name, email, age, gender)
            cls.user_list[user.user_ID] = user

    @classmethod
    def generate_edges(cls):
        pass




