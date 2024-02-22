from github import Github, Repository

class GitCommon:

    def __init__(self, org: str, token: str) -> None:
        self.client = Github(token)
        self.org = self.client.get_organization(org)
        self.org.login

    def get_repos_by_name_prefix(self, prefix: str) -> list[Repository.Repository]:
        return [repo for repo in self.org.get_repos() if repo.name.startswith(prefix)]
    
    def get_prs_not_approved(self, repo: Repository.Repository) -> list[Repository.PullRequest.PullRequest]:
        return [pr for pr in repo.get_pulls(state='open') if pr.requested_reviewers]
    
    def approve_pr(self, pr: Repository.PullRequest.PullRequest):
        pr.create_review(event="APPROVE")

