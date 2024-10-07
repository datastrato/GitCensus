#
# Display organisational activity for commits from last six months.
#

import pickle
import datetime

from org import fix_org

today = datetime.date.today()
past = today - datetime.timedelta(6 * 30)

display_closed = True # display open or closed PRs

def load_data():
    global commits
    global organisations

    with open('commits.pickle', 'rb') as pickle_file:
        commits = pickle.load(pickle_file)
    with open('organisations.pickle', 'rb') as file:
        organisations = pickle.load(file)

def orgs_commits():
    for commit in commits:
        login = commits[commit].author._login.value
        dt = commits[commit].commit.author.date.date()
        if login in organisations:
            for org in organisations[login]:
                org = fix_org(org)
                if org in stats:
                    counts[org] = counts[org] + 1
                else:
                    counts[org] = 1
                if org not in people:
                    people[org] = []
                if login not in people[org]:
                    people[org].append(login)

counts = {}
people = {}

load_data()
orgs_commits()

for org in counts:
    orgs = '"' + str(people[org]) + '"'
    print(f'{org},{len(people[org])},{counts[org]},{orgs}')