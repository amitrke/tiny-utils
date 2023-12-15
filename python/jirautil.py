import os
from jira import JIRA
from datetime import datetime, timedelta
from typing import Optional
from datetime import datetime, timedelta
import pytz
import pytz
from datetime import datetime

options = {
    'server': os.environ.get('JIRA_SERVER_URL')
}

email = os.environ.get('JIRA_EMAIL_ADDRESS')
api_token = os.environ.get('JIRA_API_TOKEN')
jira = JIRA(options, basic_auth=(email, api_token))

def add_worklog(issue: 'JIRA.Issue', time_spent_hours: float, started: str, comment: str = '') -> None:
    """
    Adds a worklog entry to an issue in JIRA if no worklog was present for the issue for the date of started.

    Parameters:
    - issue: The JIRA issue object to add the worklog to.
    - time_spent_hours: The time spent on the issue in hours.
    - started: The start time of the worklog entry in JIRA's time format.
    - comment: The comment for the worklog entry. (optional)

    Returns:
    - None
    """
    time_spent_seconds = int(time_spent_hours * 3600)  # Convert hours to seconds
    worklogs = jira.worklogs(issue)
    for worklog in worklogs:
        if worklog.started[:10] == started[:10]:
            return  # Worklog already exists for the date of started

    jira.add_worklog(issue, timeSpentSeconds=time_spent_seconds, comment=comment, started=started)

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
#Jira Agile boards for a project
boards = jira.boards(project.key)
boardId = 123

#Filter the boards to find the one we want
board = next(board for board in boards if board.id == boardId)

#Find the active sprints for a board
sprints = jira.sprints(board.id, state='active')
# Find all the issues that I am currently working on
issues = jira.search_issues('assignee = currentUser() and status not in (Closed, Resolved)', maxResults=100)

hoursLoggedToday = 0
hoursLoggedYesterday = 0
inProgressIssues = []
prefferedIssuesForWorklog = []

for issue in issues:
    print('{}: {}'.format(issue.key, issue.fields.summary))
    # Print the last worklog entry
    worklogs = jira.worklogs(issue)

    print('{}: {}'.format(issue.key, issue.fields.summary))
    worklogs = jira.worklogs(issue)

    if issue.fields.status.name == 'In Progress':
        inProgressIssues.append(issue)

    if worklogs:
        worklog = worklogs[-1]
        print('  Last worklog: {} - {}'.format(worklog.author, worklog.comment))
        
        # Calculate the hours logged today
        today = datetime.now().date()
        for worklog in worklogs:
            if worklog.started[:10] == str(today):
                hoursLoggedToday += worklog.timeSpentSeconds / 3600
        
        # Calculate the hours logged yesterday
        yesterday = today - timedelta(days=1)
        for worklog in worklogs:
            if worklog.started[:10] == str(yesterday):
                hoursLoggedYesterday += worklog.timeSpentSeconds / 3600
    else:
        print('  No worklog entries')
        
    #Print if the issue does not have a target end date
    if not issue.fields.duedate:
        print('  No target end date')
    
print('  Hours logged today: {}'.format(hoursLoggedToday))
print('  Hours logged yesterday: {}'.format(hoursLoggedYesterday))

if hoursLoggedToday < 8:
    # Sort the issues by the number of worklog entries
    inProgressIssues.sort(key=lambda issue: len(jira.worklogs(issue)), reverse=True)
    for issue in inProgressIssues:
        if hoursLoggedToday >= 8:
            break
        
        # Calculate the time remaining for the issue
        timeRemaining = issue.fields.timeoriginalestimate - issue.fields.timespent
        if timeRemaining > 0:
            # Calculate the time to log for the issue
            timeToLog = min(8 - hoursLoggedToday, timeRemaining)
            
            #Log the time for the issue starting 8 am today
            pacific_tz = pytz.timezone('US/Pacific')
            started = datetime.now(pacific_tz).replace(hour=8, minute=0, second=0, microsecond=0).isoformat()
            add_worklog(issue, timeToLog, started)
            
            # Update the hours logged today
            hoursLoggedToday += timeToLog

if hoursLoggedYesterday < 8:
    # Sort the issues by the number of worklog entries
    inProgressIssues.sort(key=lambda issue: len(jira.worklogs(issue)), reverse=True)
    for issue in inProgressIssues:
        if hoursLoggedYesterday >= 8:
            break
        
        # Calculate the time remaining for the issue
        timeRemaining = issue.fields.timeoriginalestimate - issue.fields.timespent
        if timeRemaining > 0:
            # Calculate the time to log for the issue
            timeToLog = min(8 - hoursLoggedYesterday, timeRemaining)
            
            #Log the time for the issue starting 8 am yesterday
            started = datetime.now().replace(hour=8, minute=0, second=0, microsecond=0).isoformat()
            started = (datetime.now() - timedelta(days=1)).replace(hour=8, minute=0, second=0, microsecond=0).isoformat()
            add_worklog(issue, timeToLog, started)
            
            # Update the hours logged yesterday
            hoursLoggedYesterday += timeToLog

