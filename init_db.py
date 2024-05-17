#
# Create empty GitHub cache files
#
import pickle

print("Creating pickle files")
with open('prs.pickle', 'wb') as file:
    pickle.dump({}, file)
with open('comments_pr.pickle', 'wb') as file:
    pickle.dump({}, file)
with open('merged.pickle', 'wb') as file:
    pickle.dump({}, file)
with open('issues.pickle', 'wb') as file:
    pickle.dump({}, file)
with open('comments_issues.pickle', 'wb') as file:
    pickle.dump({}, file)
with open('locations.pickle', 'wb') as file:
    pickle.dump({}, file)
with open('organisations.pickle', 'wb') as file:
    pickle.dump({}, file)
print("All done")