#
# Work out all users activity week by week
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

def pr_points():
    for id in prs:
        pr = prs[id]
        login = pr.user.login
        if login not in ignore.ignore:
            dt = pr.created_at
            week = pr.created_at.isocalendar()[1] - 1
            if login not in users:
                users[login] = [0]*52
                users[login][week] = 10
            else:
                users[login][week] = users[login][week] + 10

def pr_comment_points():
    for id in prs:
        pr = prs[id]
        for comment in comments_prs[pr.number]:
            login = comment.user.login
            if login not in ignore.ignore:
                dt = comment.created_at
                week = comment.created_at.isocalendar()[1] - 1
                if login not in users:
                    users[login] = [0]*52
                    users[login][week] = 1
                else:
                    users[login][week] = users[login][week] + 1

def issue_points():
    for id in issues:
        issue = issues[id]
        login = issue.user.login
        if login not in ignore.ignore:
            dt = issue.created_at
            week = issue.created_at.isocalendar()[1] - 1
            if login not in users:
                users[login] = [0]*52
                users[login][week] = 3
            else:
                users[login][week] = users[login][week] + 3

def issue_comment_points():
    for id in issues:
        for comment in comments_issues[id]:
            login = comment.user.login
            if login not in ignore.ignore:
                dt = comment.created_at
                week = comment.created_at.isocalendar()[1] - 1
                if login not in users:
                    users[login] = [0]*52
                    users[login][week] = 1
                else:
                    users[login][week] = users[login][week] + 1

users = {}

load_data()
pr_points()
pr_comment_points()
issue_points()
issue_comment_points()

for user in users:
    print(f"{user}", end="")
    for no in range(52):
        print(f",{users[user][no]}", end="")
    print("")