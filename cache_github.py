#
# Cache GitHub PR, issues and comments from a GitHub repository.
#
from github import Github

import datetime
import pickle

import githubSetup

save_every = 20 # Save to disk evey X PR or issues cached
skip_cached = False # Skip re-reding any issues and PRs
skip_closed = True # Skip re-reding closed issues and PRs

# Don't go back further than this (default six months)
past = datetime.date.today()
past -= datetime.timedelta(6 * 30)

def write_prs(prs, comments_pr, merged):
    print("Writing PR files")
    with open('prs.pickle', 'wb') as file:
        pickle.dump(prs, file)
    with open('comments_pr.pickle', 'wb') as file:
        pickle.dump(comments_pr, file)
    with open('merged.pickle', 'wb') as file:
        pickle.dump(merged, file)

def write_issues(issues, comments_issues):
    print("Writing issue files")
    with open('issues.pickle', 'wb') as file:
        pickle.dump(issues, file)
    with open('comments_issues.pickle', 'wb') as file:
        pickle.dump(comments_issues, file)

def cache_prs(newprs, oldprs, oldcomments, oldmerged):
    prs = oldprs
    comments_pr = oldcomments
    merged = oldmerged
    i = 0

    for pr in newprs:
        dt = pr.created_at.date()
        if dt > past:
            login = pr.user.login
            no = pr.number
            if skip_cached and no in oldprs or skip_closed and no in oldprs and oldprs[no].closed_at and pr.closed_at:
                print(f"{no} by {login} skipped")
                prs[no] = oldprs[no]
                comments_pr[no] = oldcomments[no]
                if no in oldmerged:
                    merged[no] = oldmerged[no]
                else:
                    merged[no] = pr.is_merged()
            else:
                print(f"{no} by {login} updated")
                merged[no] = pr.is_merged()
                prs[no] = pr
                all_comments = pr.get_comments()
                array = []
                for commment in all_comments:
                    array.append(commment)
                comments_pr[no] = array
                if i % save_every == 0:
                    write_prs(prs, comments_pr, merged)
        else:
            break
        i = i + 1

    write_prs(prs, comments_pr, merged)

def cache_issues(newissues, oldissues, oldcomments):
    issues = oldissues
    comments_issues = oldcomments
    i = 0

    for issue in newissues:
        dt = issue.created_at.date()
        if dt > past:
            login = issue.user.login
            no = issue.number
            if skip_cached and no in oldissues or skip_closed and no in oldissues and oldissues[no].closed_at and issue.closed_at:
                print(f"{no} by {login} skipped")
                issues[no] = oldissues[no]
                comments_issues[no] = oldcomments[no]
            else:
                print(f"{no} by {login} updated")
                issues[no] = issue
                all_comments = issue.get_comments()
                array = []
                for commment in all_comments:
                    array.append(commment)
                comments_issues[no] = array
                # Save as we go in case something goes wrong
                if i % save_every == 0:
                    write_issues(issues, comments_issues)
        else:
            break
        i = i + 1

    write_issues(issues, comments_issues)

def cache_gitgub():
    auth = githubSetup.auth()
    g = Github(auth=auth)

    repo = g.get_repo(githubSetup.repo_name)
    print(f"Name: {repo.name}")
    print(f"Open issues: {repo.open_issues_count}")
    print(f"Stars: {repo.stargazers_count}")

    newprs = repo.get_pulls(state='all', base=githubSetup.branch) # defaults to sorting by decending created date
    newissues = repo.get_issues(state='all')

    print("Reading PRs")
    with open('prs.pickle', 'rb') as pickle_file:
        oldprs = pickle.load(pickle_file)
    with open('comments_pr.pickle', 'rb') as pickle_file:
        oldcomments = pickle.load(pickle_file)
    with open('merged.pickle', 'rb') as pickle_file:
        oldmerged = pickle.load(pickle_file)

    cache_prs(newprs, oldprs, oldcomments, oldmerged)

    print("Reading Issues")
    with open('issues.pickle', 'rb') as pickle_file:
        oldissues = pickle.load(pickle_file)
    with open('comments_issues.pickle', 'rb') as comments_issues:
        oldcomments = pickle.load(comments_issues)

    cache_issues(newissues, oldissues, oldcomments)

    g.close()
    print("All done")

cache_gitgub()