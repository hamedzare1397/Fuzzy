from matplotlib.pyplot import contour
import numpy as np
import pandas as pd

from modules.engine.inferenceSystemEngine import IInferenceEnginer as InferenceEnginer
from modules.engine.mamdani.driver import MamdaniInferenceEnginer
from modules.rules.rule import IRule as Rule

class FIS:
    name=None
    rules=None
    inputs=None
    fuzzyInput:None
    driverInferenceEnginer=None;
    defuzzifier=None;

    def __init__(self,inputs,rules=None,die:InferenceEnginer=None) -> None:
        self.rules=rules
        self.inputs=pd.DataFrame(inputs)
        self.driverInferenceEnginer=die
        
    def addRule(self,rule:Rule):
        self.rules=np.append(self.rules,rule)
        return None;
    
    def setDriverInferenceEnginer(self,driver=InferenceEnginer):
        self.driverInferenceEnginer=driver;
        return None;
    
    def start(self):
        self.fuzzifier()
        data=self.fuzzyInput
        self.driverInferenceEnginer.handle(data);


    def fuzzifier(self):
        self.inputs2fuzzy_range();


    def inputs2fuzzy_range(self):
        self.fuzzyInput=[]
        minAll=[]
        maxAll=[]
        for i,row in self.inputs.iterrows():
            newrow=[]
            for j,col in enumerate(row):
                
                if(j==0):
                    newrow.append(col)
                else:
                    print(j,self.inputs.loc[:,1].min())
                    print(self.inputs.loc[:,j])
                    min=self.inputs.loc[:,j].min()
                    minAll.append(min)
                    min=self.inputs.loc[:,j].max()                
                    maxAll.append(max)
                    newrow.append((col-min)/(max-min))
            self.fuzzyInput.append(newrow)
        print('fuzzy:',self.fuzzyInput[0][2])
        print('input:',self.inputs.loc[0][2])
        print('min:',minAll,'max:',maxAll)
        #return self.fuzzyInput
            



