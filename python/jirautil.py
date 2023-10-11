# BEGIN: 5j8d9f3b4c5e
import os

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
# END: 5j8d9f3b4c5e
