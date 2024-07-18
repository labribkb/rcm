import numpy as np
import math



__author__ = "Luc-Etienne Pommé"
__copyright__ = "Copyright 2024, Univ. Bordeaux"
__credits__ = ["Luc-Etienne Pommé"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Romain Giot"
__email__ = "romain.giot@u-bordeaux.fr"
__status__ = "Prototype"



rng = np.random.default_rng()

class ConfMat:
    def __init__(self, nb_classes=10, density = 0.5, min_success=0): #min_success in [0, 1]
        self.nbClasses = nb_classes
        self.samplesByClass = 1000
        self.minSuccess = int(max(min(min_success, 1) * self.samplesByClass, 1))
        self.matrix = np.zeros((self.nbClasses, self.nbClasses))
        self.density = density # density=1: all cells are non-0, density=0: all cells are 0 (cells=non-diag)
        
    
    def density2nbCellsToFill(self,):
        return math.ceil(self.density * self.nbClasses * (self.nbClasses-1))
    
    
    def p(self, tolist=True):
        if tolist:
            return (self.matrix.tolist())
        else:
            return (self.matrix)
        
        
    def getMatrix(self,):
        return np.asarray(self.matrix)
        
        
    def randNumbers2Cells(self, randomNbList):
        res = []
        for rn in randomNbList:
            line = rn // (self.nbClasses-1)
            theorCol = rn - line*(self.nbClasses-1)
            if theorCol >= line:
                res.append((line, theorCol+1))
            else:
                res.append((line, theorCol))
            
        cl = []
        for classNum in range(self.nbClasses):
            cl.append([])
            
        for line, col in res:
            cl[line].append(col)
        
        return cl
    
    
    def build(self,):
        self.matrix = np.zeros((self.nbClasses, self.nbClasses))
        # Fill up the diagonal
        for i in range(self.nbClasses):
            self.matrix[i,i] = self.samplesByClass
        
        # Chose cells to fill
        nbCellsToFill = self.density2nbCellsToFill()
        highBound = self.nbClasses * (self.nbClasses-1)
        numbers = rng.choice(highBound, size=nbCellsToFill, replace=False)
        coordsList = self.randNumbers2Cells(numbers)
        
        for line, allCols in enumerate(coordsList):
            if len(allCols) > 0:
                sumRemoved = 0
                nbToRemove = np.random.randint(len(allCols), self.samplesByClass - self.minSuccess)
                self.matrix[line, line] -= nbToRemove
                for col in range(len(allCols)-1):
                    realNbPerCell = np.random.randint(1, nbToRemove - sumRemoved - (len(allCols)-col))
                    sumRemoved += realNbPerCell
                    self.matrix[line, allCols[col]] += realNbPerCell
                self.matrix[line, allCols[-1]] += (nbToRemove-sumRemoved)
                
        return self.matrix