import xml.etree.ElementTree as ET

#Sample student xml
xmlDataLeft = """<?xml version="1.0" encoding="UTF-8"?>
<class>
    <standard>1</standard>
    <student>
        <name>John</name>
        <age>20</age>
        <address>
            <number>123</number>
            <street>Main St</street>
            <zip>12345</zip>
        </address>
    </student>
    <student>
        <name>Jane</name>
        <age>22</age>
        <address>
            <number>456</number>
            <street>Elm St</street>
            <zip>67890</zip>
        </address>
    </student>
</class>"""

xmlDataRight = """<?xml version="1.0" encoding="UTF-8"?>
<class>
    <standard>1</standard>
    <student>
        <name>Ron</name>
        <age>20</age>
        <address>
            <number>456</number>
            <street>Elm St</street>
            <zip>67890</zip>
        </address>
    </student>
    <student>
        <name>Samantha</name>
        <age>21</age>
        <address>
            <number>789</number>
            <street>Maple Ave</street>
            <zip>54321</zip>
        </address>
    </student>
</class>"""

# Parse left xml you want to compare
left = ET.fromstring(xmlDataLeft)

# Parse right xml
right = ET.fromstring(xmlDataRight)

recordTagXPath = './/class/student'

# Function to convert xml to list based on recordTagXPath
def xmlToList(xml, recordTagXPath):
    # Create empty list
    list = []
    # Find all records
    records = xml.findall(recordTagXPath)
    # Loop through records
    for record in records:
        # Create empty dictionary
        dict = {}
        # Find all fields
        fields = record.findall('*')
        # Loop through fields
        for field in fields:
            # Add field name and value to dictionary
            dict[field.tag] = field.text
        # Add dictionary to list
        list.append(dict)
    # Return list
    return list