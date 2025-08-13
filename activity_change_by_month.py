#
# Work out all users activity changes month by month
# The calculations assume 10 points for a PR, 3 points for an issue and 1 point for a comment
#
import pickle

import ignore

def load_data():
    global prs
    global comments_prs
    global issues
    global comments_issues
    global commits

    with open('prs.pickle', 'rb') as file:
        prs = pickle.load(file)
    with open('comments_pr.pickle', 'rb') as file:
        comments_prs = pickle.load(file)
    with open('issues.pickle', 'rb') as file:
        issues = pickle.load(file)
    with open('comments_issues.pickle', 'rb') as file:
        comments_issues = pickle.load(file)
    with open('commits.pickle', 'rb') as pickle_file:
        commits = pickle.load(pickle_file)

months = [{},{},{},{},{},{},{},{},{},{},{},{}]

def pr_points():
    for id in prs:
        pr = prs[id]
        login = pr.user.login
        if login not in ignore.ignore:
            if login not in users:
                users[login] = 1
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
                if login not in users:
                    users[login] = 1
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
            if login not in users:
                users[login] = 1
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

def commit_points():
    for commit in commits:
        login = commits[commit].author._login.value
        if login not in ignore.ignore:
            dt = commits[commit].commit.author.date.date()
            month = issue.created_at.month - 1
            if login not in months[month]:
                months[month][login] = 5
            else:
                months[month][login] = months[month][login] + 5

users = {}
load_data()
pr_points()
pr_comment_points()
issue_points()
issue_comment_points()
commit_points()

no = 0
last = {}
for month in months:
    for user in users:
        if no > 0:
            this_month = 0
            if user in month:
                this_month = month[user]
            last_month = 0
            if user in last:
                last_month = last[user]
            if this_month > 0 and last_month > 0:
                if abs(this_month/last_month-1) > 0.5:
                    print(no,user,this_month/last_month)
            elif this_month == 0 and last_month > 0:
                print(no,user,0)
            elif last_month == 0 and this_month > 0:
                print(no,user,1)
    no = no + 1
    last = month

