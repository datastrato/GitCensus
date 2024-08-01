#
# Display activity for PRs from last six months.
#

import pickle
import datetime

today = datetime.date.today()
past = today - datetime.timedelta(6 * 30)

display_closed = True # display open or closed PRs

def load_data():
    global prs

    with open('prs.pickle', 'rb') as file:
        prs = pickle.load(file)

def people_prs():
    for id in prs:
        pr = prs[id]
        login = pr.user.login
        start = pr.created_at.date()
        if pr.closed_at:
            closed = pr.closed_at.date()
            stats = closed_prs
            counts = closed_no
            people = people_closed
        else:
            closed = today
            stats = open_prs
            counts = open_no
            people = people_open
        diff = closed - start
        if login in stats:
            stats[login] = stats[login] + diff.days
            counts[login] = counts[login] + 1
        else:
            stats[login] = diff.days
            counts[login] = 1
        if login not in people:
            people[login] = []
        if login not in people[login]:
            people[login].append(login)

open_prs = {}
closed_prs = {}
stats = {}
open_no = {}
closed_no = {}
counts = {}
people_open = {}
people_closed = {}
people = {}

load_data()
people_prs()

if display_closed:
    for person in closed_prs:
        print(f'{person},{closed_no[person]},{closed_prs[person]/closed_no[person]}')
else:
    for person in open_prs:
        print(f'{person},{open_no[person]},{open_prs[person]/open_no[person]}')