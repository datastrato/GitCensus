#
# List all contribitors, no of PRs and orgs they are in
#

import pickle
from datetime import datetime
import ignore

with open('prs.pickle', 'rb') as file:
    prs = pickle.load(file)
with open('organisations.pickle', 'rb') as file:
    orgs = pickle.load(file)

people = {}
for id in prs:
    pr = prs[id]
    login = pr.user.login
    if login not in ignore.ignore:
        if login not in people:
            people[login] = 1
        else:
            people[login] = people[login] + 1

print("Name,PRs,Orgs")
for person in people:
    org = ''
    if person in orgs:
        org = orgs[person]
    print(f"{person},{people[person]},{org}")
