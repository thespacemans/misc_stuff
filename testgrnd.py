"""
class Test:
    '''this is a docstring description for class Test'''
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def printout(self):
        print(self.field1, ", ", self.field2)

testObj = Test("Str", 3)

testObj.printout()
print(testObj.__doc__)
"""
# -------------------------------------------------------------
class velocity:
    '''class for velocity data object'''
    def __init__(self, increment, total):
        self.incr = increment
        self.total = total

    def addTotal(self, increment):
        self.total += increment
