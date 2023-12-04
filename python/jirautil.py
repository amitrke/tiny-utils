# BEGIN: 5j8d9f3b4c5e
import os
from jira import JIRA

options = {
    'server': os.environ.get('JIRA_SERVER_URL')
}

email = os.environ.get('JIRA_EMAIL_ADDRESS')
api_token = os.environ.get('JIRA_API_TOKEN')
jira = JIRA(options, basic_auth=(email, api_token))

issue = jira.issue('JRA-9')
print(issue.fields.project.key)            # 'JRA'
print(issue.fields.issuetype.name)         # 'New Feature'
print(issue.fields.reporter.displayName)   # 'Mike Cannon-Brookes [Atlassian]'

# Find all the issues that I am currently working on
issues = jira.search_issues('assignee = currentUser() and status not in (Closed, Resolved)', maxResults=100)
for issue in issues:
    print('{}: {}'.format(issue.key, issue.fields.summary))
    # Print the last worklog entry
    worklogs = jira.worklogs(issue)
    if worklogs:
        worklog = worklogs[-1]
        print('  Last worklog: {} - {}'.format(worklog.author, worklog.comment))
    else:
        print('  No worklog entries')

    #Print if the issue does not have a target end date
    if not issue.fields.duedate:
        print('  No target end date')
    
    
# Function to add a worklog entry to an issue
def add_worklog(issue, timeSpentSeconds, comment):
    jira.add_worklog(issue, timeSpentSeconds=timeSpentSeconds, comment=comment)
    

# END: 5j8d9f3b4c5e
