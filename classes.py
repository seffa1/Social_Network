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

        # Generates the names, age, and gender for the users from a text file of names
        with open('names.txt', 'r') as name_file:
            for name in name_file.readlines():
                cls.name_list.append(str(name)[0:-1])  # gets ride of the '\n'

                # Adds age and gender to the list
                cls.age_list.append(random.randint(14, 90))
                cls.gender_list.append(random.choice(['m', 'f']))
                n += 1
                if n >= user_amount:
                    break

        # Generates the email list
        for name in cls.name_list:
            # Builds a random email address for each person and adds it to the list
            email = ''
            email += str(name)[0]
            with open('names.txt', 'r') as name_file:
                random_name = random.choice(list(name_file))
            email += str(random_name)[0:-1]  # gets ride of the '\n'
            email += str(random.randint(0, 99))
            email += '@gmail.com'
            cls.email_list.append(email)
        print('Done')

    @classmethod
    def generate_users(cls):
        print('Generating user accounts with user info....')
        while len(cls.name_list) > 0:
            name = cls.name_list.pop()
            email = cls.email_list.pop()
            age = cls.age_list.pop()
            gender = cls.gender_list.pop()
            user = User(name, email, age, gender)
            cls.user_list[user.user_ID] = user
        print('Done')

    @classmethod
    def show_user(cls):
        print('Printing user list...')
        for user in cls.user_list:
            print(f'User_ID: {user} --- Name: {cls.user_list[user].name} --- Email: {cls.user_list[user].email}')

    @classmethod
    def generate_user_friends(cls):
        for user_ID in cls.user_list:
            user = cls.user_list[user_ID]
            number_of_friends = random.randint(1, len(cls.user_list)/3)  # at most you can be friends with a 1/3 of total users

