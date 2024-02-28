import os
import gitcommon

#Get git repo name prefix from environment variable
repo_prefix = os.getenv('REPO_PREFIX')

#Get github token from environment variable
token = os.getenv('GITHUB_TOKEN')

#Get github org from environment variable
org = os.getenv('GITHUB_ORG')

#Create GitCommon object
gc = gitcommon.GitCommon(org=org, token=token)

#Get all repos with the given prefix
repos = gc.get_repos_by_name_prefix(repo_prefix)

#Iterate over all repos
for repo in repos:
    print(f"Processing repo: {repo.name}")
    #Get all PRs not approved
    prs = gc.get_prs_not_approved(repo)
    #Iterate over all PRs
    for pr in prs:
        print(f"Approving PR: {pr.title}")
        #Approve PR
        gc.approve_pr(pr)
