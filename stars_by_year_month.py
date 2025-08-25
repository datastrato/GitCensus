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

start = 2020
years = [[0] * 12 for _ in range(12)]

for stargazer in stargazers:
    year = stargazer.starred_at.year
    month = stargazer.starred_at.month - 1
    years[year-start][month] = years[year-start][month] + 1

for year in range(start, 2025):
    for i in range(12):
        month = datetime.date(1900, i+1, 1).strftime('%b')
        print(f'{year},{month},{years[year-start][i]}')
