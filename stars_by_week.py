#
# Display the number of stars for each week of the year
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

now = datetime.date.today().year
weeks = [0] * 54

for stargazer in stargazers:
    year = stargazer.starred_at.year
    if year == now:
        week = int(stargazer.starred_at.strftime("%W"))
        weeks[week] = weeks[week] + 1

for i in range(54):
    print(f"{i+1},{weeks[i]}")

