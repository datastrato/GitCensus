#
# Cache GitHub PR, issues and comments from a GitHub repository.
#
from github import Github

import datetime
import pickle

import githubSetup

save_every = 20 # Save to disk every X commits cached
skip_cached = True

# Don't go back further than this (default six months)
past = datetime.date.today()
past -= datetime.timedelta(6 * 30)

def write_commits(commmits):
    print("Writing commit file")
    with open('commits.pickle', 'wb') as file:
        pickle.dump(commmits, file)

def cache_commits(newcommits, oldcommits):
    commits = oldcommits
    i = 0

    print(f'{newcommits.totalCount} new commits')

    for commit in newcommits:
        dt = commit.commit.author.date.date()
        if dt > past:
            name = commit.author._login.value
            sha = commit.sha
            if skip_cached and sha in oldcommits:
                print(f"{sha} by {name} skipped")
            else:
                print(f"{sha} by {name} updated")
                commits[sha] = commit
        else:
            continue
        i = i + 1

    write_commits(commits)

def cache_gitgub():
    auth = githubSetup.auth()
    g = Github(auth=auth)

    repo = g.get_repo(githubSetup.repo_name)
    print(f"Name: {repo.name}")

    newcommits = repo.get_commits() # defaults to sorting by decending created date

    print("Reading commits")
    with open('commits.pickle', 'rb') as pickle_file:
        oldcommits = pickle.load(pickle_file)

    cache_commits(newcommits, oldcommits)

    g.close()
    print("All done")

cache_gitgub()