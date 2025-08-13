#
# Work out contribitors by week
#
import pickle
from datetime import datetime
import ignore

with open('prs.pickle', 'rb') as file:
    prs = pickle.load(file)

people = {}

for i in range(52):
    people[i] = []

for id in prs:
    pr = prs[id]
    login = pr.user.login
    if login not in ignore.ignore:
        week = pr.created_at.isocalendar()[1]
        if pr.created_at.year == 2024:
            if login not in people[week]:
                people[week].append(login)

for i in range(52):
    print(f'{i+1},{len(people[i])}')
