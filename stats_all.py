#
# Work out all users stats
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

load_data()
pr_count = len(prs)
issue_count = len(issues)
commit_count = len(commits)

print("Month,PRs,Issues,Commits")
print(f"{pr_count},{issue_count},{commit_count}")