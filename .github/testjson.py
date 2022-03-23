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
    with open(filename) as json_file:
        data = json.load(json_file)
        #print(data)
        for k in topkeys:
            if data.get(k) is None:
                print("No '"+k+"' key")
                exitval = -1
        projects = data['projects']
        for project in projects:
            for k in projkeys:
                if project.get(k) is None:
                    print("No '"+k+"' project key")
                    exitval = -1 
except json.decoder.JSONDecodeError as e:
    print("Could not decode valid JSON", e)
    exitval = -1

exit(exitval)
