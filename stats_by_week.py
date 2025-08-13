#
# Work out all users activity week by week
# The calculations assume 10 points for a PR, 3 points for an issue and 1 point for a comment
#
import pickle

import datetime

import ignore

now = datetime.date.today().year

def load_data():
    global prs
    global issues
    global commits

    with open('prs.pickle', 'rb') as file:
        prs = pickle.load(file)
    with open('issues.pickle', 'rb') as file:
        issues = pickle.load(file)
    with open('commits.pickle', 'rb') as pickle_file:
        commits = pickle.load(pickle_file)

def count_prs():
    count = 0
    for id in prs:
        pr = prs[id]
        login = pr.user.login
        if login not in ignore.ignore:
            dt = pr.created_at
            week = dt.isocalendar()[1] - 1
            year = dt.year
            if year == now:
                print(login)
                pr_count[week] = pr_count[week] + 1
                count = count + 1
    print(count)


def count_issues():
    for id in issues:
        issue = issues[id]
        login = issue.user.login
        if login not in ignore.ignore:
            dt = issue.created_at
            week = dt.isocalendar()[1] - 1
            year = dt.year
            if year == now:
                issue_count[week] = issue_count[week] + 1

def count_commits():
    for commit in commits:
        login = commits[commit].author._login.value
        if login not in ignore.ignore:
            dt = commits[commit].commit.author.date.date()
            week = dt.isocalendar()[1] - 1
            year = dt.year
            if year == now:
                commit_count[week] = commit_count[week] + 1

pr_count = [0]*52
issue_count = [0]*52
commit_count = [0]*52

load_data()
count_prs()
count_issues()
count_commits()

for no in range(52):
    print(f"{pr_count[no]},{issue_count[no]},{commit_count[no]}")