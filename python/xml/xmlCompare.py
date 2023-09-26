import xml.etree.ElementTree as ET

#Sample student xml
xmlDataLeft = """<?xml version="1.0" encoding="UTF-8"?>
<students>
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
</students>"""

xmlDataRight = """<?xml version="1.0" encoding="UTF-8"?>
<students>
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
</students>"""

# Parse left xml you want to compare
left = ET.fromstring(xmlDataLeft)

# Parse right xml
right = ET.fromstring(xmlDataRight)

# Function to convert xml to dict recursively
def xmlToDict(xmlElement: ET.Element):
    # If xml element has no children, return the text
    if len(xmlElement) == 0:
        return xmlElement.text
    # If xml element has children, create a dict
    xmlDict = {}
    # Loop through each child
    for child in xmlElement:
        # If child is a list, append it to the dict
        if child.tag in xmlDict:
            if type(xmlDict[child.tag]) is list:
                xmlDict[child.tag].append(xmlToDict(child))
            else:
                xmlDict[child.tag] = [xmlDict[child.tag]]
                xmlDict[child.tag].append(xmlToDict(child))
        # If child is not a list, add it to the dict
        else:
            xmlDict[child.tag] = xmlToDict(child)
    return xmlDict