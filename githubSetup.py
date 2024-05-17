#
# Utility functions to log into GitHub.
#
from github import Auth

import os
import sys

def read_environment():
    global repo_name
    global token
    global branch
    global login
    global password

    repo_name = ""
    token = ""
    branch = ""
    login = ""
    password = ""

    if 'GC_REPO_NAME' in os.environ:
        repo_name = os.environ['GC_REPO_NAME']
    else:
        sys.exit("Environment variable GC_REPO_NAME missing")
    
    if 'GC_REPO_TOKEN' in os.environ:
        token = os.environ['GC_REPO_TOKEN']
    elif 'GC_LOGIN' in os.environ and 'GC_PASSWORD' in os.environ:
        login = os.environ['GC_LOGIN']
        password = os.environ['GC_PASSWORD']
    else:
        sys.exit("Environment variable GC_REPO_TOKEN or GC_LOGIN and GC_PASSWORD missing")

    if 'GC_REPO_BRANCH' in os.environ:
        branch = os.environ['GC_REPO_BRANCH']
    else:
        sys.exit("Environment variable GC_REPO_BRANCH missing")

def auth():
    read_environment()
    if token:
        return Auth.Token(token)
    else:
        return Auth.Login(login, password)