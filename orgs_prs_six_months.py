#
# Display organisational activity for PRs from last six months.
#

import pickle
import datetime

from org import fix_org

today = datetime.date.today()
past = today - datetime.timedelta(6 * 30)

display_closed = True # display open or closed PRs

def load_data():
    global prs
    global organisations

    with open('prs.pickle', 'rb') as file:
        prs = pickle.load(file)
    with open('organisations.pickle', 'rb') as file:
        organisations = pickle.load(file)

def orgs_prs():
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
        if login in organisations:
            for org in organisations[login]:
                org = fix_org(org)
                if org in stats:
                    stats[org] = stats[org] + diff.days
                    counts[org] = counts[org] + 1
                else:
                    stats[org] = diff.days
                    counts[org] = 1
                if org not in people:
                    people[org] = []
                if login not in people[org]:
                    people[org].append(login)

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
orgs_prs()

if display_closed:
    for org in closed_prs:
        orgs = '"' + str(people_closed[org]) + '"'
        print(f'{org},{len(people_closed[org])},{closed_no[org]},{closed_prs[org]/closed_no[org]},{orgs}')
else:
    for org in open_prs:
        orgs = '"' + str(people_open[org]) + '"'
        print(f'{org},{len(people_open[org])},{open_no[org]},{open_prs[org]/open_no[org]},{orgs}')