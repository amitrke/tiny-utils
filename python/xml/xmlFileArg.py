# Read two command-line arguments: xml file names

import sys
import xml.etree.ElementTree as ET

# Read two command-line arguments: xml file names
if len(sys.argv) != 3:
    print("Usage: python xmlFileArg.py file1.xml file2.xml")
    sys.exit(1)

# Parse left xml you want to compare
left = ET.parse(sys.argv[1]).getroot()

# Parse right xml
right = ET.parse(sys.argv[2]).getroot()
