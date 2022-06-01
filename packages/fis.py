import numpy as np

from engine.inferenceSystemEngine import IInferenceEnginer as InferenceEnginer
from rules.rule import IRule as Rule

class FIS:
    rules=None;
    inputs=None;
    driverInferenceEnginer=None;
    defuzzifier=None;

    def __init__(self,inputs,rules=None,die:InferenceEnginer=None) -> None:
        self.rules=rules
        self.inputs=inputs
        self.driverInferenceEnginer=die
        
    def addRule(self,rule:Rule):
        self.rules=np.append(self.rules,rule)
        return None;
    
    def setDriverInferenceEnginer(self,driver=InferenceEnginer):
        self.driverInferenceEnginer=driver;
        return None;
    
    def start(self):
        self.driverInferenceEnginer.handle()



if(__name__=='__main__'):
    fis=FIS([1,2,3]);
    fis.start();