import random

import numpy
import pandas as pd
import numpy as np
from modules.engine.mamdani.driver import MamdaniInferenceEnginer as mmdn;
from modules.fis import FIS

if(__name__=='__main__'):
    data=pd.read_csv('./data/wine.data',sep=',',names=[
        'type','x1','x2','x3','x4','x5','x6','x7','x8','x9','x10','x11','x12','x13'
        ])

    # start normalize
    copy_data = data.copy()
    for i in range(1,14):
        column = 'x'+str(i)
        copy_data[column] = copy_data[column] / copy_data[column].abs().max()
    print(copy_data)
    #end normalize


    #start select data for test
    percentage = 0.05
    test_index = []
    train_index =[]
    while len(test_index) < np.floor(data.shape[0]*percentage):
        rand = random.randrange(0,data.shape[0])
        if rand not in test_index:
            test_index.append(rand)
    for i in range(0,data.shape[0]):
        if i not in test_index:
            train_index.append(i)
    print(test_index)
    print(train_index)
    #end select data for test


    #start create fazzi roules => 3
    dimension_points = [[0,0,0.5],[0,0.5,1],[0.5,1,1]]

    #end create fazzi

    #mmd=mmdn()
    #fis=FIS(inputs=data,die=mmd);
    #fis.start();