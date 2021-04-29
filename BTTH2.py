# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 08:18:20 2021

@author: DELL
"""

import random
import numpy as np
import statistics
import seaborn as sns
import statsmodels.api as sm
import pylab as py

data = np.random.normal(0,1,1000)
print(data)

class ProjectOne:
   
    def __init__(self, data):
        
         self.data = data
         self.mean = np.mean(data)
         self.med =  np.median(data)
         self.std = np.std(data)
         self.mode = statistics.mode(data)
         self.max = np.max(data)
         self.min = np.min(data)
         
   
    def percentile(self, p):
        return np.percentile(self.data, p)
    def hits(self):
        return sns.histplot(self.data, kde=True)
    def qq(self):
        return sm.qqplot(self.data, line ='45')
    
Pj = ProjectOne(data)
print(' Mean = ', Pj.mean)
print(' Med = ', Pj.med)
print(' Std = ', Pj.std)
print(' Mod =', Pj.mode)
print(' Max = ', Pj.max)
print(' Min = ', Pj.min)
print(' Bách phân vị 25% = ', Pj.percentile( 0.25) )
print(' Bách phân vị 75% = ', Pj.percentile( 0.75) )
Pj.hits()
Pj.qq()
#print(ProjectOne(data).data)

        