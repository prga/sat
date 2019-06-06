'''
Written by Paola Accioly in June/2019.
'''
def readInputs():
    inputs = []
    return inputs

def readClauses(inputs):
    clauses = []
    return clauses

def readVariables(clauses):
    variables = []
    return variables

def readFormula():
    inputs = readInputs()
    clauses = readClauses(inputs)
    variables = readVariables(clauses)
    result = {'clauses':clauses, 'variables':variables}
    return result

def nextAssignment(currentAssignment):
    nextAssignment = []
    return nextAssignment

def doSolve(clauses, assignment):
    isSat = False
    while ((not isSat) and  '''must check whether this is the last assignment or not'''):
        '''does this assignment satisfy the formula? If so, make isSat true. 

        if not, get the next assignment and try again.'''
        assignment = nextAssignment(assignment)
    result = {'isSat': isSat, 'satisfyingAssignment': None}
    if (isSat):
        result['satisfyingAssignment'] = assignment

    return result

def solve():
    formula = readFormula()
    result = doSolve(formula['clauses'], formula['variables'])
    return result
