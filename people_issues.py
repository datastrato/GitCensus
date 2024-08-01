#
# Display activity for issues from last six months.
#

import pickle
import datetime

today = datetime.date.today()
past = today - datetime.timedelta(6 * 30)

display_closed = True # display open or closed issues

def load_data():
    global issues

    with open('issues.pickle', 'rb') as file:
        issues = pickle.load(file)

def people_prs():
    for id in issues:
        issue = issues[id]
        login = issue.user.login
        start = issue.created_at.date()
        if issue.closed_at:
            closed = issue.closed_at.date()
            stats = closed_issue
            counts = closed_no
            people = people_closed
        else:
            closed = today
            stats = open_issue
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

open_issue = {}
closed_issue = {}
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
    for person in closed_issue:
        print(f'{person},{closed_no[person]},{closed_issue[person]/closed_no[person]}')
else:
    for person in open_issue:
        print(f'{person},{open_no[person]},{open_issue[person]/open_no[person]}')