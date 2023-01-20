from git import Repo # comes from the GitPython package
import time

def getInformation(directory):
    repo = Repo(directory)
    name = repo.active_branch # gets name of the current branch
    commit = repo.iter_commits(max_count = 1) # only gets the the most recent commit
    recentChange = False
    rufus_fault = False
    for c in commit:
        current = time.gmtime() # get current time and date
        dateCommit = time.gmtime(c.committed_date)
        if current.tm_mday - dateCommit.tm_mday <= 7: # checks if most recent change happened within a week(7 days)
            recentChange = True # returns true if so
            if str(c.author).lower() == "rufus": # then checks if that change was made by rufus
                rufus_fault = True # returns true if so

    print("Active Branch: ", name)
    print("Local Changes:" , repo.is_dirty()) # checks if there are any changes made that aren't committed
    print("Recent Commits: ",recentChange)
    print("Blame Rufus: ",rufus_fault)

git_dir = "/Users/moshi/projects/blame-rufus"
getInformation(git_dir)