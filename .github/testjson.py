import sys
import os
import json

topkeys = ["formatVersion", "fileVersion", "projects"]
projkeys = [ "projectName",
             "projectImage",
             "description",
             "bundleLink",
             "learnGuideLink",
             "compatibility"
             ]

try:
    filename = sys.argv[1]
except IndexError:
    print("Must provide filenamename as argument")
    exit(-1)

exitval = 0

if not filename.endswith(".json"):
    print("File doesn't end with .json");
    exit(-1)
    
try:
    with open(pathname) as json_file:
        data = json.load(json_file)
        for k in topkeys:
            if not data.get(k):
                print("No '"+k+"' key")
                exitval = -1
        projects = data['projects']
        for k in projkeys:
            if not projects.get(k):
                print("No '"+k+"' project key")
                exitval = -1 
except json.decoder.JSONDecodeError as e:
    print("Could not decode valid JSON", e)
    exitval = -1

exit(exitval)
