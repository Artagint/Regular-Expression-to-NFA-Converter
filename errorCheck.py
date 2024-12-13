# This file holds code related to error checking
import sys
import os

def IsValidFile(fileName):
    # Check if the file ends in '.txt', exit if not
    if not fileName.endswith('.txt'):
        print("ERROR: Make sure file ends with '.txt'")
        sys.exit(1)

    # Check if the file is valid and exists, exit if not
    if not os.path.isfile(fileName):
        print(f"ERROR: File '{fileName}' is invalid")
        sys.exit(1)

    # Check if the file is empty, exit if it is
    if (os.path.getsize(fileName) == 0):
        print(f"ERROR: '{fileName}' is empty")
        sys.exit(1)

