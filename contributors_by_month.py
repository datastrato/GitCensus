import pickle
from datetime import datetime
import ignore

with open('prs.pickle', 'rb') as file:
    prs = pickle.load(file)

people = {}

for i in range(12):
    people[i] = []

for id in prs:
    pr = prs[id]
    login = pr.user.login
    if login not in ignore.ignore:
        month = int(pr.created_at.month) - 1
        if pr.created_at.year == 2024:
            if login not in people[month]:
                people[month].append(login)

for i in range(12):
    print(f'{i+1},{len(people[i])}')
