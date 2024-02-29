import json
import gitcommon
import commonutils

# Read config.json file
with open('python/config.json') as json_file:
    config = json.load(json_file)

repo_prefix = config.get('Github')['repo-prefix']

#Get github token from environment variable
token = commonutils.get_env_var('GITHUB_TOKEN')

org = config.get('Github')['organization']
prApprovedUsers = config.get('Github')['prApproveUsers']
autoMerge = config.get('Github')['autoMerge']

#Create GitCommon object
gc = gitcommon.GitCommon(org=org, token=token)

#Get all repos with the given prefix
repos = gc.get_repos_by_name_prefix(repo_prefix)

#Iterate over all repos
for repo in repos:
    print(f"Processing repo: {repo.name}")
    #Get all PRs not approved
    prs = gc.get_prs_not_approved(repo=repo, prApprovedUsers=prApprovedUsers)
    #Iterate over all PRs
    for pr in prs:
        print(f"Approving PR: {pr.title}")
        #Approve PR
        gc.approve_pr(pr)
        if autoMerge:
            print(f"Merging PR: {pr.title}")
            #Merge PR
            #gc.merge_pr(pr)
