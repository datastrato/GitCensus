#
# Display all of the organisations for a repository who belog to the ASF orginations.
# Note this is not quite the same as committers on an project, as they could be committers on any ASF project.
#

import pickle

with open('organisations.pickle', 'rb') as file:
    organisations = pickle.load(file)

orgs = {}
no = 0
for person in organisations:
    ASF = False
    for org in organisations[person]:
        if org == 'apache':
            ASF = True
    if ASF:
        for org in organisations[person]:
            if org not in orgs:
                orgs[org] = 1
            else:
                orgs[org] = orgs[org] + 1
    no = no + 1

for org in orgs:
    print(f"{org},{orgs[org]}")

print(f'{no} people')