# GitCensus

GitCensus is a set of tool to cache and generate statistics about your project's community. The tools use the excellent [PyGitHub library](https://github.com/PyGithub/PyGithub) to obtain GitHub information.

The object with the code is to be simple and easy to understand that can by updated by people who are not experts in Python. I only dabble in Python, so please forgive anything that's not done in the correct Python way.

Feedback and pull requests are welcome!

# Prerequisites

Python 3.9
PyGithub 2.4.0

# Getting started

Most of the scripts work off a cache of the GitHub information so that they are quick to run, and you don't encounter issues with GitHub's request limits.

First off you need to set up some environment variables to define what repository you will be analysing.
```shell
export GC_REPO_NAME=<your repo>
export GC_REPO_BRANCH=<branch>
```

You can access the repository via a GitHub token like so:
```shell
export GC_REPO_TOKEN=<GitHub token>
```

Or via a user name and password:
```shell
export GC_LOGIN=<your GitHub login>
export GC_PASSWORD=<your GitHub password>
```

You then need to initial the pickle databases:
```shell
python3 init_db.py
```

And read and cache the GitHub information you are interested you.

If you are interested in PR, issues and comments run:
```shell
python3 cache_github.py
```

If you are interested in users organisations and locations run:
```shell
python3 github_orgs_and_locs.py
```

Finally you can run some script to look at the cached data:

To see weekly activity on the project by contributors run:
```shell
python3 activity_by_week.py
```

To see locations of contributors:
```shell
python3 locations.py
```

To see organisations of contributors:
```shell
python3 organisations.py
```

# Contributions

Contributions of any kind are welcome.
