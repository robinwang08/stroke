import os
import csv
from strokeConfig import config
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

if __name__ == '__main__':
    dataset = pd.read_csv(config.CSV_FILE)

    length = len(dataset.columns) - 1
    X = dataset.iloc[:, 0:length]
    y = dataset.iloc[:, length]

    X_train, X_val_test, y_train, y_val_test = train_test_split(X, y, test_size=config.VALIDATION_SPLIT, random_state=config.SEED)
    X_validation, X_test, y_validation, y_test = train_test_split(X_val_test, y_val_test, test_size=config.TEST_SPLIT, random_state=config.SEED)

    path = '/media/user1/my4TB/robin/stroke/normalized/'

    train = X_train['FileNumber']
    validation = X_validation['FileNumber']
    test = X_test['FileNumber']

    # create config files
    trainmtt = open(config.train_MTT, 'w')
    trainrcbf = open(config.train_rCBF, 'w')
    trainrcbv = open(config.train_rCBV, 'w')
    traintmax = open(config.train_Tmax, 'w')
    traingt = open(config.train_GT, 'w')
    for x in train:
        trainmtt.write(path + str(x) + '/MTT.nii' + '\n')
        trainrcbf.write(path + str(x) + '/rCBF.nii' + '\n')
        trainrcbv.write(path + str(x) + '/rCBV.nii' + '\n')
        traintmax.write(path + str(x) + '/Tmax.nii' + '\n')
        traingt.write(path + str(x) + '/label.nii' + '\n')
    trainmtt.close()
    trainrcbf.close()
    trainrcbv.close()
    traintmax.close()
    traingt.close()

    validationmtt = open(config.validation_MTT, 'w')
    validationrcbf = open(config.validation_rCBF, 'w')
    validationrcbv = open(config.validation_rCBV, 'w')
    validationtmax = open(config.validation_Tmax, 'w')
    validationgt = open(config.validation_GT, 'w')
    for x in validation:
        validationmtt.write(path + str(x) + '/MTT.nii' + '\n')
        validationrcbf.write(path + str(x) + '/rCBF.nii' + '\n')
        validationrcbv.write(path + str(x) + '/rCBV.nii' + '\n')
        validationtmax.write(path + str(x) + '/Tmax.nii' + '\n')
        validationgt.write(path + str(x) + '/label.nii' + '\n')
    validationmtt.close()
    validationrcbf.close()
    validationrcbv.close()
    validationtmax.close()
    validationgt.close()

    testmtt = open(config.test_MTT, 'w')
    testrcbf = open(config.test_rCBF, 'w')
    testrcbv = open(config.test_rCBV, 'w')
    testtmax = open(config.test_Tmax, 'w')
    testgt = open(config.test_GT, 'w')
    for x in test:
        testmtt.write(path + str(x) + '/MTT.nii' + '\n')
        testrcbf.write(path + str(x) + '/rCBF.nii' + '\n')
        testrcbv.write(path + str(x) + '/rCBV.nii' + '\n')
        testtmax.write(path + str(x) + '/Tmax.nii' + '\n')
        testgt.write(path + str(x) + '/label.nii' + '\n')
    testmtt.close()
    testrcbf.close()
    testrcbv.close()
    testtmax.close()
    testgt.close()

    print('Created new config files split')