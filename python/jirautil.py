# BEGIN: 5j8d9f3b4c5e
import os
from jira import JIRA
from datetime import datetime, timedelta
from typing import Optional

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

#Jira Agile boards for a project
boards = jira.boards(project.key)
boardId = 123

#Filter the boards to find the one we want
board = next(board for board in boards if board.id == boardId)

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
# Calculate the start time (yesterday at 8 am)
start_time = datetime.now() - timedelta(days=1)
start_time = start_time.replace(hour=8, minute=0, second=0, microsecond=0)

# Convert the start time to JIRA's time format
start_time_str = start_time.strftime('%Y-%m-%dT%H:%M:%S.000%z')

# Log work for the issue
add_worklog(issue, timeSpentSeconds, comment, started=start_time_str)

def add_worklog(issue: 'JIRA.Issue', time_spent_seconds: int, comment: str, started: str) -> None:
    """
    Adds a worklog entry to an issue in JIRA if no worklog was present for the issue for the date of started.

    Parameters:
    - issue: The JIRA issue object to add the worklog to.
    - time_spent_seconds: The time spent on the issue in seconds.
    - comment: The comment for the worklog entry.
    - started: The start time of the worklog entry in JIRA's time format.

    Returns:
    - None
    """
    worklogs = jira.worklogs(issue)
    for worklog in worklogs:
        if worklog.started[:10] == started[:10]:
            return  # Worklog already exists for the date of started

    jira.add_worklog(issue, timeSpentSeconds=time_spent_seconds, comment=comment, started=started)
    

# END: 5j8d9f3b4c5e
