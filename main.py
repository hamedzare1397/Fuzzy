import random

import numpy
import pandas as pd
import numpy as np
from modules.engine.mamdani.driver import MamdaniInferenceEnginer as mmdn;
from modules.fis import FIS
from modules.membershipFunctions.triangle import Triangle

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
    roles_label = np.zeros((3,3,3,3,3,3,3,3,3,3,3,3,3))
    roles_data = np.zeros((3,3,3,3,3,3,3,3,3,3,3,3,3))
    dimentions =14
    s=(Triangle(copy_data["x10"][0],*dimension_points[2]).exec())

    for data_index in train_index:
        max = -1
        for x1 in range(3):
            for x2 in range(3):
                for x3 in range(3):
                    for x4 in range(3):
                        for x5 in range(3):
                            for x6 in range(3):
                                for x7 in range(3):
                                    for x8 in range(3):
                                        for x9 in range(3):
                                            for x10 in range(3):
                                                for x11 in range(3):
                                                    for x12 in range(3):
                                                        for x13 in range(3):
                                                            min = np.amin([
                                                                Triangle(copy_data["x1"][data_index], *dimension_points[x1]).exec(),
                                                                Triangle(copy_data["x2"][data_index], *dimension_points[x2]).exec(),
                                                                Triangle(copy_data["x3"][data_index], *dimension_points[x3]).exec(),
                                                                Triangle(copy_data["x4"][data_index], *dimension_points[x4]).exec(),
                                                                Triangle(copy_data["x5"][data_index], *dimension_points[x5]).exec(),
                                                                Triangle(copy_data["x6"][data_index], *dimension_points[x6]).exec(),
                                                                Triangle(copy_data["x7"][data_index], *dimension_points[x7]).exec(),
                                                                Triangle(copy_data["x8"][data_index], *dimension_points[x8]).exec(),
                                                                Triangle(copy_data["x9"][data_index], *dimension_points[x9]).exec(),
                                                                Triangle(copy_data["x10"][data_index], *dimension_points[x10]).exec(),
                                                                Triangle(copy_data["x11"][data_index], *dimension_points[x11]).exec(),
                                                                Triangle(copy_data["x12"][data_index], *dimension_points[x12]).exec(),
                                                                Triangle(copy_data["x13"][data_index], *dimension_points[x13]).exec(),
                                                            ])
                                                            if min>max:
                                                                max = min
                                                                if(roles_data[x1][x2][x3][x4][x5][x6][x7][x8][x9][x10][x11][x12][x13]<min):
                                                                    roles_label[x1][x2][x3][x4][x5][x6][x7][x8][x9][x10][x11][x12][x13] = copy_data["type"][data_index]
                                                                    roles_data[x1][x2][x3][x4][x5][x6][x7][x8][x9][x10][x11][x12][x13] = min


    print(roles)
    #end create fazzi

    #mmd=mmdn()
    #fis=FIS(inputs=data,die=mmd);
    #fis.start();