from git import Repo
from pathlib import Path

# rorepo is a Repo instance pointing to the git-python repository.
# For all you know, the first argument to Repo is a path to the repository
# # you want to work with
# tester = Path().resolve()
repo = Repo.init("")
name = repo.active_branch
# print(tester)
print(name)
