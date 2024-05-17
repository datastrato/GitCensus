#
# Display the number of stars for each month
# Note: this doesn't use cached information
#
from github import Github
from github import Auth

import datetime

import githubSetup

auth = githubSetup.auth()
github = Github(auth=auth)
repo = github.get_repo(githubSetup.repo_name)
print(f"Name: {repo.name}")
print(f"Stars: {repo.stargazers_count}")

stargazers = repo.get_stargazers_with_dates()

months = [0] * 12

for stargazer in stargazers:
    month = stargazer.starred_at.month - 1
    months[month] = months[month] + 1

for i in range(11):
    month = datetime.date(1900, i+1, 1).strftime('%b')
    print(f'{month},{months[i]}')
