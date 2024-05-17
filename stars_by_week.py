#
# Display the number of stars for each week of the year
# Note: this doesn't use cached information
#
from github import Github
from github import Auth

import githubSetup

auth = githubSetup.auth()
github = Github(auth=auth)
repo = github.get_repo(githubSetup.repo_name)
print(f"Name: {repo.name}")
print(f"Stars: {repo.stargazers_count}")
stargazers = repo.get_stargazers_with_dates()

weeks = [0] * 54
for stargazer in stargazers:
    week = int(stargazer.starred_at.strftime("%W"))
    weeks[week] = weeks[week] + 1

for i in range(53):
    print(f"{i+1},{weeks[i]}")

