#
# Display activity for commits from last six months.
#

import pickle
import datetime

today = datetime.date.today()
past = today - datetime.timedelta(6 * 30)

def load_data():
    global commits

    with open('commits.pickle', 'rb') as file:
        commits = pickle.load(file)

def people_commits():
    for sha in commits:
        commit = commits[sha]
        login = commit.author._login.value
        if login in counts:
            counts[login] = counts[login] + 1
        else:
            counts[login] = 1
        if login not in people:
            people.append(login)


comments_issues = {}
counts = {}
people = []

load_data()
people_commits()

for person in people:
    print(f'{person},{counts[person]}')