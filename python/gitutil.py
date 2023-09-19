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
with open("python/repolist.json", "r") as f:
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


# Check if the command is status
# If it is, print the status of all repos

if command == "status":
    for repo in repolist["repos"]:
        git_status(os.path.join(*repolist["basePath"], repo))

