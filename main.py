import pandas as pd
from modules.engine.mamdani.driver import MamdaniInferenceEnginer as mmdn;
from modules.fis import FIS

if(__name__=='__main__'):
    data=pd.read_csv('./data/wine.data',sep=',',names=[
        'type','x1','x2','x3','x4','x5','x6','x7','x8','x9','x10','x11','x12','x13'
        ])
    mmd=mmdn()
    fis=FIS(inputs=data,die=mmd);
    fis.start();