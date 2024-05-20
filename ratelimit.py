#
# How long are you rate limited for?
#
from github import Github
from github import Auth

import pickle

import githubSetup

auth = githubSetup.auth()
g = Github(auth=auth)
print(g.get_rate_limit())
g.close()