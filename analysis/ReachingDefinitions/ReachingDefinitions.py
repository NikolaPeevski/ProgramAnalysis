from analysis.Analysis import Analysis
from microCTypes.VariableAssignmentStatement import VariableAssignmentStatement
from microCTypes.VariableDeclaration import VariableDeclaration


class ReachingDefinitions(Analysis):
    killSet = []

    genSet = []

    def __init__(self, program):
        """
        Base class for all program analysis
        Contains the abstract analyse method that performs
        the actual analysis step for the program
        :param program: The program to analyse
        """
        super().__init__(program)

        self.contraints = []

        self.edges = []

        self.initialConstraints = []

        for programPoint in program:  # Create initial constrants based on variables across the program
            if type(programPoint) == VariableAssignmentStatement or type(programPoint) == VariableDeclaration:  # if it's a variable declaration or variable assignment
                new = (programPoint.getName(), '?')  # create new constraint
                if not self.initialConstraints.__contains__(new):  # if the constraint is not already in the initial constraints - this would be the case with multiple assigments of variable X
                    self.initialConstraints.append(new)  # add the constraint

    def analyse(self, step):

        output = step[0].constraint.copy()  # Copy the constraints so we can work with them safely

        if type(step[1]) == VariableAssignmentStatement:  # If type variable assignment
            initialConstraints = step[0].constraint  # get the constraints we know from the node we're going from
            for constraint in initialConstraints:  # For all these constraints
                if constraint[0] == step[
                    1].getName():  # If the assignments variable is represented in a known constraint
                    output.remove(constraint)  # Remove that constraints - kill it
            genSet = (step[1].getName(), str(step[1].label))  # create a genSet based on the name of variable and the label of the node we're going to
            output.append(genSet)  # Put the new constraint into the known constraints
        if type(step[1]) == VariableDeclaration:  # If type variable declaration)
            initialConstraints = step[0].constraint  # get the constraints we know from the node we're going from
            for constraint in initialConstraints:  # For all these constraints
                if constraint[0] == step[1].getName():  # If the assignments variable is represented in a known constraint
                    output.remove(constraint)  # Remove that constraints - kill it
            genSet = (step[1].getName(), str(""))  # create a genSet based on the name of variable because it is a declaration, set the set to empty
            output.append(genSet)  # Put the new constraint into the known constraints
        # For all other types, skip analysis
        # Forward the constraints
        return output
