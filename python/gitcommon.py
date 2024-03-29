from github import Github, Repository, PullRequest

class GitCommon:

    def __init__(self, org: str, token: str) -> None:
        self.client = Github(token)
        self.org = self.client.get_organization(org)
        self.org.login

    def get_repos_by_name_prefix(self, prefix: str) -> list[Repository.Repository]:
        return [repo for repo in self.org.get_repos() if repo.name.startswith(prefix)]
    
    def get_prs_not_approved(self, repo: Repository.Repository, prApprovedUsers: list[str]) -> list[PullRequest.PullRequest]:
        unapproved_prs = []
        for pr in repo.get_pulls(state='open'):
            if pr.mergeable == True and pr.mergeable_state == "blocked" and \
                pr.user.login in prApprovedUsers and pr.requested_reviewers:
                unapproved_prs.append(pr)
        return unapproved_prs
    
    def approve_pr(self, pr: PullRequest.PullRequest):
        pr.create_review(event="APPROVE")

    def merge_pr(self, pr: PullRequest.PullRequest):
        pr.merge()
