#
# Work out all users activity month by month
# The calculations assume 10 points for a PR, 3 points for an issue and 1 point for a comment
#
import pickle

import ignore

def load_data():
    global prs
    global comments_prs
    global issues
    global comments_issues

    with open('prs.pickle', 'rb') as file:
        prs = pickle.load(file)
    with open('comments_pr.pickle', 'rb') as file:
        comments_prs = pickle.load(file)
    with open('issues.pickle', 'rb') as file:
        issues = pickle.load(file)
    with open('comments_issues.pickle', 'rb') as file:
        comments_issues = pickle.load(file)

months = [{},{},{},{},{},{},{},{},{},{},{},{}]

def pr_points():
    for id in prs:
        pr = prs[id]
        login = pr.user.login
        if login not in ignore.ignore:
            dt = pr.created_at
            month = pr.created_at.month - 1
            if login not in months[month]:
                months[month][login] = 10
            else:
                months[month][login] = months[month][login] + 10

def pr_comment_points():
    for id in prs:
        pr = prs[id]
        for comment in comments_prs[pr.number]:
            login = comment.user.login
            if login not in ignore.ignore:
                dt = pr.created_at
                month = pr.created_at.month - 1
            if login not in months[month]:
                months[month][login] = 1
            else:
                months[month][login] = months[month][login] + 1

def issue_points():
    for id in issues:
        issue = issues[id]
        login = issue.user.login
        if login not in ignore.ignore:
            dt = issue.created_at
            month = issue.created_at.month - 1
            if login not in months[month]:
                months[month][login] = 5
            else:
                months[month][login] = months[month][login] + 5

def issue_comment_points():
    for id in issues:
        for comment in comments_issues[id]:
            login = comment.user.login
            if login not in ignore.ignore:
                dt = comment.created_at
                month = comment.created_at.month - 1
                if login not in months[month]:
                    months[month][login] = 1
                else:
                    months[month][login] = months[month][login] + 1

load_data()
pr_points()
pr_comment_points()
issue_points()
issue_comment_points()

for month in months:
    print(f"Month: {month}")
