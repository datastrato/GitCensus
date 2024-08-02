#
# Cache the locatiopn and organisation information from GitHub for a repository.
#
from github import Github
from github import Auth

import pickle

import githubSetup

save_every = 20 # Save to disk every X record cached
max = 1000 # Max people to read in one go

def write_files(locations, organisations):
    print("Writing files")
    with open('locations.pickle', 'wb') as file:
        pickle.dump(locations, file)
    with open('organisations.pickle', 'wb') as file:
        pickle.dump(organisations, file)

def cache_github():
    i = 0
    print("Reading contribitors")

    auth = githubSetup.auth()
    g = Github(auth=auth)

    repo = g.get_repo(githubSetup.repo_name)
    print(f"Name: {repo.name}")

    people = repo.get_contributors()
    print(f'{people.totalCount} people')

    everyone = []
    for person in people:
        login = person.login
        everyone.append(person)

    # assumes commits.pickle exist and upto date
    with open('commits.pickle', 'rb') as pickle_file:
        commits = pickle.load(pickle_file)

    for commit in commits:
        login = commits[commit].author._login.value
        if login not in everyone:
            everyone.append(commits[commit].author)

    locations = {}
    with open('locations.pickle', 'rb') as pickle_file:
        locations = pickle.load(pickle_file)

    organisations = {}
    with open('organisations.pickle', 'rb') as pickle_file:
        organisations = pickle.load(pickle_file)

    for person in everyone:
        login = person.login
        if login not in locations:
            locations[login] = person.location
            belongs_to = person.get_orgs()
            organisations[login] = []
            company = person.company
            print(f'{login} {locations[login]} {company}')
            if company:
                organisations[login].append(company)
            for org in belongs_to:
                organisations[login].append(org.login)
            # Save as we go in case something goes wrong
            if i % save_every == 0:
                write_files(locations, organisations)
            if i == max:
                print(f'Done {max} people stopping')
                break
            i = i + 1

    write_files(locations, organisations)

    g.close()

    print(f"All done")

cache_github()
