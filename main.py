# Artem Tagintsev, CS317, 10/15/2024, Project: RE to NFA
# This is the main file of the program, responsible for the flow and logic outline
import sys
from errorCheck import IsValidFile
from dataStructures import concatenationOperation, unionOperation, kleeneStarOperation, charOperation

# Make sure there are 3 arguments, exit if not
if len(sys.argv) != 2:
    print("ERROR: Proper format is 'python3 main.py <filename.txt>'")
    sys.exit(1)

fileName = sys.argv[1]
IsValidFile(fileName)  # Perform error checks on the file

# Read the file and process each line
with open(fileName, 'r') as file:
    for line in file:
        line = line.strip()
        if not line: # 
            continue

        numOfStates = 0 # Reset the number of states for each line
        nfaStack = []  # Init the stack to hold NFAs
        alphabet = 'abcdeE' # Var to hold the alphabet

        # Process each character in the line and then perform the necessary operations
        for c in line:
            # Concatenate
            if c == '&':
                numOfStates = concatenationOperation(nfaStack, numOfStates)
            # Union
            elif c == '|':
                numOfStates = unionOperation(nfaStack, numOfStates)
            # Kleene Star
            elif c == '*':
                numOfStates = kleeneStarOperation(nfaStack, numOfStates)
            # Add char from alphabet
            else:
                numOfStates = charOperation(c, nfaStack, numOfStates, alphabet)

        # Make sure the stack has only one NFA in it
        if len(nfaStack) != 1:
            print("ERROR: Invalid Regular Expression, NFA can't be made")
            continue

        # Output the NFA details
        outputNFA = nfaStack[0]
        print(f"RE: {line}")
        print(f"Start: q{outputNFA.startState}")
        print(f"Accept: q{outputNFA.acceptState}")

        for transition in sorted(outputNFA.transitions, key=lambda t: (t.state1, t.symbol, t.state2)):
            print(f"(q{transition.state1}, {transition.symbol}) -> q{transition.state2}")

        print() 

