#!/usr/bin/env python3
"""
Variable definition for MicroC variables
"""


class Variable:
    def __init__(self, value):
        """ Main constructor for values """
        self.value = value

    def getvalue(self):
        """ Getting said value """
        return self.value
