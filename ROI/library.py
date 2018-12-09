import itemkey as itk


""" 
    Main library with static definitions of item consumptions according to recipe
    Based on game version A8.1:0.812a
"""

class cBuilding:
    """ 
        Class to encapsulate a production building
    """

    def __init__(self, name='', btype='', numFields=1, efficiency=1):
        """ 
        Creates a building object
        """
        if btype not in itk.buildingDict.keys():
            raise ValueError('Building ' + btype + ' is not identified')

        self.name = name
        self.input = itk.buildingDict[btype][2]
        self.output = itk.buildingDict[btype][1]
        self.type = btype
        self.fields = numFields
        self.efficiency = efficiency

    def describe(self):
        """ 
        Print basic info of this building object
        """
        print("Factory Name:", self.name, '\n',
              "Factory Type:", self.type, '\n',
              "Number of fields", "{0:2d}".format(self.fields), '\n',
              "Efficiency", "{0:4.2f}".format(self.efficiency))
    
class cCompany:
    """ 
        Class to encapsulate a company production assets
    """


x = cBuilding('Water 1', 'Water Siphon', 3, 0.333)
x.describe()