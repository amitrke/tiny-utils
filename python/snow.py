#Service Now Utilities
import pysnow

# Create client object
c = pysnow.Client(instance='myinstance', user='myusername', password='mypassword')

# Define a resource, here we'll use the incident table API
incident = c.resource(api_path='/table/incident')

# Query for incidents with state 3
response = incident.get(query={'state': 3})

# Print out the first match
print(response.first())