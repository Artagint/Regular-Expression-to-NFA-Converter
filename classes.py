# This file holds the main classes for the NFA and its transitions

# Init the Transition with states and symbol
class Transition:
    def __init__(self, state1, symbol, state2):
        self.state1 = state1
        self.symbol = symbol
        self.state2 = state2

# Init the NFA with start, accpet, an empty list, and a function to add transitions
class NFA:
    def __init__(self, startState, acceptState):
        self.startState = startState
        self.acceptState = acceptState
        self.transitions = []

    def addTransition(self, state1, symbol, state2):
        self.transitions.append(Transition(state1, symbol, state2))

