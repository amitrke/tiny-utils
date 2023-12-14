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

project = jira.project('JRA')
#Find the active sprints for a project
# sprints = jira.sprints(project.key, state='active')
# for sprint in sprints:
#     print('{}: {}'.format(sprint.id, sprint.name))

#Jira Agile board id 123
board = jira.board(123)
#Find the active sprints for a board
sprints = jira.sprints(board.id, state='active')
for sprint in sprints:
    print('{}: {}'.format(sprint.id, sprint.name))



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
