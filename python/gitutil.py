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
    print(" - changedFiles: " + str(changedFiles))

# Check if the command is status
# If it is, print the status of all repos

if command == "status":
    for repo in repolist["repos"]:
        git_status(os.path.join(*repolist["basePath"], repo))

