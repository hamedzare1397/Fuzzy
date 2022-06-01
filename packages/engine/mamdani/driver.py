from packages.engine.inferenceSystemEngine import IInferenceEnginer
from packages.engine.mamdani.defuzzifiers.defuzzifier import Defuzzifier


class MamdaniInferenceEnginer(IInferenceEnginer):
    
    def __init__(self,defuzzifier:Defuzzifier=None) -> None:
        super().__init__()
        self.defuzzifier=defuzzifier

    def setDefuzzifier(self,defuzzifier:Defuzzifier):
        self.defuzzifier=defuzzifier
        return None;

    def handle():
        pass