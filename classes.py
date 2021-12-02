import os
import random
from collections import deque
# import networkx as nx
# import matplotlib.pyplot as plt

def clear():
    os.system('cls')


class User:
    user_ID = 0

    def __init__(self, name: str, email: str, age: int, gender: str):
        self.email = email
        self.age = age
        self.name = name
        self.gender = gender

        # This should be a sorted dictionary, by weight
        self.friends = {}  # email: weight

        User.user_ID += 1
        self.user_ID = User.user_ID

    # Friend adding is something that should be happening at a graph level, not vertex level
    # This method will be moved to the network generator
    # def add_friend(self, friend, weight):  # weight represents how much you interact with that friend
    #     self.friends[friend.email] = weight

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
        return f'User ID: {self.user_ID}  Email: {self.email}'


class Network_Generator:
    user_dict = {}  # user.email : user object
    connections_dict = {}
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
    def add_user(cls, user):
        cls.user_dict[user.email] = user

    @classmethod
    def generate_users(cls):
        # Its unlikely but technically possible to have two users with the same email generated
        # In that case the second one would overwrite the first
        print('\nGenerating user accounts with user info....')
        while len(cls.name_list) > 0:
            name = cls.name_list.pop()
            email = cls.email_list.pop()
            age = cls.age_list.pop()
            gender = cls.gender_list.pop()
            user = User(name, email, age, gender)
            cls.add_user(user)
        print('Done')

    @classmethod
    def show_user(cls):
        print('\nPrinting user list...')
        for user in cls.user_dict:
            print(f'ID: {cls.user_dict[user].user_ID}   Email: {user}')
        print('----------------------\n')

    connections = 0

    @classmethod
    def make_friends(cls, user1: User, user2: User, weight):
        if user1.email == user2.email:
            print(f"{user1.email} cannot be friends with themselves")
        else:
            # friends = {email: weight}
            user1.friends[user2.email] = weight
            user2.friends[user1.email] = weight
            # print(f'{user1.email} and {user2.email} are now friends: {weight}')
            cls.connections += 1

    @classmethod
    def generate_connections(cls, max_friends: int):
        print('\nGenerating connections...')

        # each user will be assigned some friends
        for user in cls.user_dict.values():

            # each user gets a random number of friend between 1 and total_users/connectedness
            number_of_friends = random.randint(1, max_friends)

            # add a number of friends equal to the number_of_friends
            for i in range(0, number_of_friends):

                # Choose a random user from the list, but try again if you pick yourself
                friend = random.choice(list(cls.user_dict.values()))
                while friend.email == user.email:
                    friend = random.choice(list(cls.user_dict.values()))

                # Give them a random likeness, or how much they interact with one another
                likeness = random.randint(0, 9)

                # Make them friends!
                cls.make_friends(user, friend, likeness)
        print(f'Total connections: {cls.connections}')
        print(f'Average Friends: {cls.connections // len(cls.user_dict)}')
        print('Done')


    @classmethod
    def print_connections(cls):
        for user in cls.user_dict.values():
            print(f'Friends of User ID:{user.user_ID} - {user.email}')
            for friend in user.friends:
                print(f'---> Weight: {user.friends[friend]} - ID: {cls.user_dict[friend].user_ID} - {friend}')
            print('')

        print('----------------------')

    @classmethod
    def create_user(cls, name, email, age, gender):
        user = User(name, email, age, gender)
        cls.add_user(user)

    @classmethod
    def search_for_user(cls, name):
        pass

    @classmethod
    def find_user_bredth(cls, user1: User, user2: User):
        # This algorithm starts at user 1, and traverses the network until it finds user2
        visit_count = 0
        visited = []
        path_queue = deque()
        current_user = user1

        # The search ends if this condition is met
        if current_user.email == user2.email:
            print('User Found!')
            print(f'Visited {visit_count} user')
            print(f'Visited the following users:')
            for user in visited:
                print(f'{user.name}')
            return

        # If the user is not the one we are looking for

        # Get all friends of the current user
        current_user_friends_list = []
        for friend_email in current_user.friends:
            friend = cls.user_dict[friend_email]
            current_user_friends_list.append(friend)

        # We add their connections to the path_queue, then chose one at random
        for friend in current_user_friends_list:
            path_queue.appendleft(friend)



        # Make the chosen children the current child, check it, add its children to the queue
        # The next child is the next in the queue, this is a bredth-first approach
        # For a depth first search, we will use a stack instead of a queue

















# https://www.geeksforgeeks.org/visualize-graphs-in-python/
class Network_Visualizer:
    def __init__(self):
        self.connections

