import itemkey as itk
import numpy as np

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

    def __init__(self, cBuildingList=[]):
        """ 
        Creates a company object with building list as asset
        """
        self.assets = cBuildingList
        self.calculated = False

    def calculate_input_output(self):
        """ 
        Calculates the array of input/output as number of items required/produced
        every 15 days
        """
        prodInp = [0] * len(itk.itemDict)
        prodOut = [0] * len(itk.itemDict)
        for building in self.assets:
            mult = building.fields * building.efficiency
            for item in building.input:
                if len(item) == 0:
                    continue
                prodInp[itk.itemDict[item[0]]] += mult * item[2] * 15 / item[1]
            for item in building.output:
                if len(item) == 0:
                    continue
                prodOut[itk.itemDict[item[0]]] += mult * item[2] * 15 / item[1]
        
        self.totalInp = prodInp
        self.totalOut = prodOut
        self.calculated = True

    def print_net_production(self):
        if not self.calculated:
            self.calculate_input_output()
        labelmap = {v:k for k, v in itk.itemDict.items()}
        netprod = np.array(self.totalInp) - np.array(self.totalOut)
        for i in range(len(itk.itemDict)):
            if netprod[i] != 0:
                print("{0:7.2f}".format(netprod[i]), labelmap[i])

