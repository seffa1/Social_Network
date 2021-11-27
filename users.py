from collections import deque


name_list = deque()
email_list = deque()

names_to_read = 1000
n = 0
while n <= names_to_read:
    with open('names.txt', 'r') as name_file:
        for name in name_file.readlines():
            name_list.append(name)
            n += 1


