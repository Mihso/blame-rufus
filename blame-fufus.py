from git import Repo
from pathlib import Path

# rorepo is a Repo instance pointing to the git-python repository.
# For all you know, the first argument to Repo is a path to the repository
# # you want to work with
# tester = Path().resolve()

def getInformation(directory):
    repo = Repo(directory)
    name = repo.active_branch
    user = repo.iter_commits()
    print(repo.is_dirty())  # check the dirty state)
    print(user)
    for t in user:
        print(t.committed_date)
    print(name)

direct = "/Users/moshi/projects/project-gamma"
getInformation(direct)