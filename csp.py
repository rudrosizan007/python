from abc import ABC, abstractmethod
class Constraint(ABC):
    def __init__(self,variables):
        self.variables =variables #condition check
    @abstractmethod
    def satisfied(self,assignment) : #to check constraint satisfied or not
    #implementation override
        pass
class CSP():
    def __init__(self,variables,domains):#The __init__() initializer creates the constraints dict
        self.variables=variables
        self.domains=domains
        self.constraints={}
        for variable in self.variables:
            self.constraints[variable]=[]
            if variable not in self.domains:
                raise LookupError(
                    'every variable should have a domain assigned to it'
                )#raise an exception if any domain is missing
    def add_constraint(self,constraint):#check all variables is csp doesnt have variables not in constraint
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError('Variable not in constraint not in CSP')
            else:
                self.constraints[variable].append(constraint)#it will a
    def consistent(self,variable,assignment):#consistent() goes through every constraint for a given variable (it’s always a variable that was newly added to the assignment) and checks if the constraint is satisfied, given the new assignment. If the assignment satisfies every constraint, True is returned. If any constraint imposed on the variable isn’t satisfied, False is returned.
    #consistent() function as a method on CSP
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True
        #The base case for the recursive search is finding a valid assignment for every variable. Once we have, we return the first instance of a solution that was valid (we stop searching)
    def backtracking_search(self,assignment={}):
        #assignment is complete if every variable is assigned
        if len(assignment) ==len(self.variables):
            return assignment
            #get all the variables in the csp but not is assignment
        unassigned = [v for v in self.variables if v not in assignment]
        # get the every possible domain value of the first unassigned variable
        first = unassigned[0]
        for value in self.domains[first]:
            local_assignment =assignment.copy()
            local_assignment[first]=value
            #conditions to check constraint consistancy
            if self.consistent(first,local_assignment):
                result = self.backtracking_search(local_assignment)
                # if we didn't find the result, we will end up backtracking
                if result is not None:
                    return result
        return None
class MapColoringConstraint(Constraint):
    def __init__(self,place1,place2):#for two place that shares border to check condition
        super().__init__([place1,place2])
        self.place1=place1
        self.place2=place2
    def satisfied(self,assignment):#to check two adjacancy place have same color or not
        if self.place1 not in assignment or self.place2 not in assignment:
            return True
        return assignment[self.place1]!= assignment[self.place2]
if __name__=='__main__':
    variables=['WA','NT','SA','Q','NSW','V','T']
    domains={}
    for variable in variables:
        domains[variable]=['Red','Green','Blue']
    csp = CSP(variables,domains)
    csp.add_constraint(MapColoringConstraint("WA", "NT"))
    csp.add_constraint(MapColoringConstraint("WA", "SA"))
    csp.add_constraint(MapColoringConstraint("SA", "NT"))
    csp.add_constraint(MapColoringConstraint("Q", "NT"))
    csp.add_constraint(MapColoringConstraint("Q", "SA"))
    csp.add_constraint(MapColoringConstraint("Q", "NSW"))
    csp.add_constraint(MapColoringConstraint("NSW", "SA"))
    csp.add_constraint(MapColoringConstraint("V", "SA"))
    csp.add_constraint(MapColoringConstraint("V", "NSW"))
    csp.add_constraint(MapColoringConstraint("V", "T"))
    solution=csp.backtracking_search()
    if solution is None:
        print("No solution is found")
    else:
        print(solution)             


