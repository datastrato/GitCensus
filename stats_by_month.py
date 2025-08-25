#
# Work out stats month by month
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
            month = dt.month - 1
            year = dt.year
            if year == now:
                pr_count[month] = pr_count[month] + 1
                count = count + 1
    print(f"Total PRs this year: {count}")

def count_issues():
    count = 0
    for id in issues:
        issue = issues[id]
        login = issue.user.login
        if login not in ignore.ignore:
            dt = issue.created_at
            month = dt.month - 1
            year = dt.year
            if year == now:
                issue_count[month] = issue_count[month] + 1
                count = count + 1
    print(f"Total Issues this year: {count}")

def count_commits():
    count = 0
    for commit in commits:
        login = commits[commit].author._login.value
        if login not in ignore.ignore:
            dt = commits[commit].commit.author.date.date()
            month = dt.month - 1
            year = dt.year
            if year == now:
                commit_count[month] = commit_count[month] + 1
                count = count + 1
    print(f"Total Commits this year: {count}")

# Arrays for each month (Jan–Dec = 12 slots)
pr_count = [0]*12
issue_count = [0]*12
commit_count = [0]*12

load_data()
count_prs()
count_issues()
count_commits()

print("Month,PRs,Issues,Commits")
for no in range(12):
    print(f"{no+1},{pr_count[no]},{issue_count[no]},{commit_count[no]}")
