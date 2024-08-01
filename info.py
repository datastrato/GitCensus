#
# Cache info
#
import pickle

with open('prs.pickle', 'rb') as pickle_file:
    prs = pickle.load(pickle_file)

print(f'{len(prs)} PRs')

with open('issues.pickle', 'rb') as pickle_file:
    issues = pickle.load(pickle_file)

print(f'{len(issues)} issues')

with open('locations.pickle', 'rb') as pickle_file:
    locations = pickle.load(pickle_file)

print(f'{len(locations)} locations')

with open('organisations.pickle', 'rb') as pickle_file:
    organisations = pickle.load(pickle_file)

print(f'{len(organisations)} organisations')

with open('commits.pickle', 'rb') as pickle_file:
    commits = pickle.load(pickle_file)

print(f'{len(commits)} commits')
