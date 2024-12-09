# Artem Tagintsev, CS317, 10/15/2024, Project: RE to NFA
# This file contains the code responsible for handling operations in the stack
from classes import NFA

# Returns the new number of states after it increments
def newState(numOfStates):
    numOfStates += 1
    return numOfStates, numOfStates

# Concatenates two NFAs that we have on the stack
def concatenationOperation(nfaStack, numOfStates):
    nfa2 = nfaStack.pop()
    nfa1 = nfaStack.pop()
    
    nfa1.addTransition(nfa1.acceptState, 'E', nfa2.startState)
    
    concatenateNFA = NFA(nfa1.startState, nfa2.acceptState)
    concatenateNFA.transitions = nfa1.transitions + nfa2.transitions
    nfaStack.append(concatenateNFA)
    return numOfStates

# Performs a union operation on two NFAs we have on the stack
def unionOperation(nfaStack, numOfStates):
    nfa2 = nfaStack.pop()
    nfa1 = nfaStack.pop()
    
    newStart, numOfStates = newState(numOfStates)
    newAccept, numOfStates = newState(numOfStates)
    
    unionizedNFA = NFA(newStart, newAccept)
    unionizedNFA.addTransition(newStart, 'E', nfa1.startState)
    unionizedNFA.addTransition(newStart, 'E', nfa2.startState)
    unionizedNFA.addTransition(nfa1.acceptState, 'E', newAccept)
    unionizedNFA.addTransition(nfa2.acceptState, 'E', newAccept)
    
    unionizedNFA.transitions.extend(nfa1.transitions + nfa2.transitions)
    nfaStack.append(unionizedNFA)
    return numOfStates

# Does a kleene star operation to the NFA we have on top of the stack
def kleeneStarOperation(nfaStack, numOfStates):
    nfa1 = nfaStack.pop()
    
    newStart, numOfStates = newState(numOfStates)
    
    kleeneStarNFA = NFA(newStart, newStart)
    kleeneStarNFA.addTransition(newStart, 'E', nfa1.startState)
    kleeneStarNFA.addTransition(nfa1.acceptState, 'E', newStart)
    
    kleeneStarNFA.transitions.extend(nfa1.transitions)
    nfaStack.append(kleeneStarNFA)
    return numOfStates

# Creates an NFA for a char if it's in the alphabet ('abcdeE'), else it'll print an error message and exit
def charOperation(c, nfaStack, numOfStates, alphabet):
    if c in alphabet:
        startState, numOfStates = newState(numOfStates)
        acceptState, numOfStates = newState(numOfStates)
        charNFA = NFA(startState, acceptState)
        charNFA.addTransition(startState, c, acceptState)

        nfaStack.append(charNFA)
        return numOfStates
    else:
        print(f"ERROR: '{c}' is not valid in this Regular Expression")
        sys.exit(1)

