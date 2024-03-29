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

    path = '/media/user1/my4TB/robin/stroke/isles2/'

    train = X_train['FileNumber']
    validation = X_validation['FileNumber']
    test = X_test['FileNumber']

    # create config files
    trainmtt = open(config.train_MTT, 'w')
    trainrcbf = open(config.train_rCBF, 'w')
    trainrcbv = open(config.train_rCBV, 'w')
    traintmax = open(config.train_Tmax, 'w')
    traingt = open(config.train_GT, 'w')
    trainroi = open(config.train_roi, 'w')

    for x in train:
        trainmtt.write(path + 'case_' + str(x) + '/CT_MTT.nii' + '\n')
        trainrcbf.write(path + 'case_' + str(x) + '/CT_CBF.nii' + '\n')
        trainrcbv.write(path + 'case_' + str(x) + '/CT_CBV.nii' + '\n')
        traintmax.write(path + 'case_' + str(x) + '/CT_Tmax.nii' + '\n')
        traingt.write(path + 'case_' + str(x) + '/CT_OT.nii' + '\n')
        trainroi.write(path + 'case_' + str(x) + '/mask.nii' + '\n')
    trainmtt.close()
    trainrcbf.close()
    trainrcbv.close()
    traintmax.close()
    traingt.close()
    trainroi.close()

    validationmtt = open(config.validation_MTT, 'w')
    validationrcbf = open(config.validation_rCBF, 'w')
    validationrcbv = open(config.validation_rCBV, 'w')
    validationtmax = open(config.validation_Tmax, 'w')
    validationgt = open(config.validation_GT, 'w')
    validationpred = open(config.validation_pred, 'w')
    validationroi = open(config.validation_roi, 'w')
    for x in validation:
        validationmtt.write(path + 'case_' + str(x) + '/CT_MTT.nii' + '\n')
        validationrcbf.write(path + 'case_' + str(x) + '/CT_CBF.nii' + '\n')
        validationrcbv.write(path + 'case_' + str(x) + '/CT_CBV.nii' + '\n')
        validationtmax.write(path + 'case_' + str(x) + '/CT_Tmax.nii' + '\n')
        validationgt.write(path + 'case_' + str(x) + '/CT_OT.nii' + '\n')
        validationroi.write(path + 'case_' + str(x) + '/mask.nii' + '\n')
        validationpred.write(str(x) + '-pred.nii' + '\n')
    validationmtt.close()
    validationrcbf.close()
    validationrcbv.close()
    validationtmax.close()
    validationgt.close()
    validationpred.close()
    validationroi.close()

    testmtt = open(config.test_MTT, 'w')
    testrcbf = open(config.test_rCBF, 'w')
    testrcbv = open(config.test_rCBV, 'w')
    testtmax = open(config.test_Tmax, 'w')
    testgt = open(config.test_GT, 'w')
    testpred = open(config.test_pred, 'w')
    testroi = open(config.test_roi, 'w')
    for x in test:
        testmtt.write(path + 'case_' + str(x) + '/CT_MTT.nii' + '\n')
        testrcbf.write(path + 'case_' + str(x) + '/CT_CBF.nii' + '\n')
        testrcbv.write(path + 'case_' + str(x) + '/CT_CBV.nii' + '\n')
        testtmax.write(path + 'case_' + str(x) + '/CT_Tmax.nii' + '\n')
        testgt.write(path + 'case_' + str(x) + '/CT_OT.nii' + '\n')
        testroi.write(path + 'case_' + str(x) + '/mask.nii' + '\n')
        testpred.write(str(x) + '-pred.nii' + '\n')
    testmtt.close()
    testrcbf.close()
    testrcbv.close()
    testtmax.close()
    testgt.close()
    testpred.close()
    testroi.close()

    print('Created new config files split')