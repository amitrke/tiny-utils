# Read command line arguments
# Usage: python gitutil.py <command> <args>
# Commands:
#   - clone <repo> <dir>

import sys
import json
import os
from git import Repo

# Get command line arguments
args = sys.argv

# Check if there are enough arguments
if len(args) < 2:
    print("Usage: python gitutil.py <command> <args>")
    exit()

# Get command
command = args[1]

# Read the repolist json file
with open("repolist.json", "r") as f:
    repolist = json.load(f)

def git_status(repoPath):
    # Initialize existing repo
    print("Repo: " + repoPath)
    repo = Repo(repoPath)
    changedFiles = [item.a_path for item in repo.index.diff(None)]
    branch = repo.active_branch
    print(" - branch: " + branch.name)

    # If changed files is not empty, print the changed files
    if len(changedFiles) > 0:
        print(" - changedFiles: " + str(changedFiles))
    
    # If there are untracked files, print them
    untrackedFiles = repo.untracked_files
    if len(untrackedFiles) > 0:
        print(" - untrackedFiles: " + str(untrackedFiles))
    
    # If there are uncommited changes, print them
    if repo.is_dirty():
        print(" - uncommited changes")

    # Check if the branch is ahead of the remote
    if len(list(repo.iter_commits('origin/' + branch.name + '..' + branch.name))) > 0:
        print(" - branch is ahead of remote")

    # Check if the branch is behind the remote
    if len(list(repo.iter_commits(branch.name + '..' + 'origin/' + branch.name))) > 0:
        print(" - branch is behind remote")
    
    # Check if the branch is diverged from the remote
    if len(list(repo.iter_commits('origin/' + branch.name + '..' + branch.name))) > 0 and len(list(repo.iter_commits(branch.name + '..' + 'origin/' + branch.name))) > 0:
        print(" - branch is diverged from remote")

    # Check if the branch has been merged into the remote develop branch
    if branch.name != "develop" and len(list(repo.iter_commits('origin/develop..' + branch.name))) != 0:
        print(" - branch has not been merged into remote develop branch")

# Check if the command is status
# If it is, print the status of all repos

if command == "status":
    for repo in repolist["repos"]:
        git_status(os.path.join(*repolist["basePath"], repo))

# Check if the command is checkout
# If it is, checkout the specified branch in all repos

if command == "checkout":
    # Check if there are enough arguments
    if len(args) < 3:
        print("Usage: python gitutil.py checkout <branch>")
        exit()
    
    # Get branch name
    branch = args[2]

    for repo in repolist["repos"]:
        # Initialize existing repo
        print("Repo: " + repo)
        repo = Repo(os.path.join(*repolist["basePath"], repo))
        print(" - branch: " + branch)

        # Checkout the specified branch
        repo.git.checkout(branch)

# Check if the command is fetch

if command == "fetch":
    for repo in repolist["repos"]:
        # Initialize existing repo
        print("Repo: " + repo)
        repo = Repo(os.path.join(*repolist["basePath"], repo))

        # Fetch from remote
        repo.git.fetch()

# Check if the command is pull

if command == "pull":
    for repo in repolist["repos"]:
        # Initialize existing repo
        print("Repo: " + repo)
        repo = Repo(os.path.join(*repolist["basePath"], repo))

        # Pull from remote
        repo.git.pull()