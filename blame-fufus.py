from git import Repo
from pathlib import Path
import time

# rorepo is a Repo instance pointing to the git-python repository.
# For all you know, the first argument to Repo is a path to the repository
# # you want to work with
# tester = Path().resolve()

def getInformation(directory):
    repo = Repo(directory)
    name = repo.active_branch
    user = repo.iter_commits()
    recentChange = False
    rufus_fault = False
    checked = False
    for t in user:
        count += 1
        current = time.gmtime()
        dateCommit = time.gmtime(t.committed_date)
        if checked == False:
            if current.tm_mday - dateCommit.tm_mday <= 7: # checks if most recent change happened within a week(7 days)
                recentChange = True # returns true if so
                if str(t.author).lower() == "rufus": # then checks if that change was made by rufus
                    rufus_fault = True # returns true if so
            checked = True

    print("Active Branch: ", name)
    print("Local Changes:" , repo.is_dirty())
    print("Recent Commits: ",recentChange)
    print("Blame Rufus: ",rufus_fault)

direct = "/Users/moshi/projects/project-gamma"
getInformation(direct)