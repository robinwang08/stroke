class Config(object):
    SEED = 123
    CSV_FILE = './data.csv'

    VALIDATION_SPLIT = .33
    TEST_SPLIT = .30

    train_MTT = './examples/configFiles/stroke/train/trainChannels_MTT.cfg'
    train_rCBF = './examples/configFiles/stroke/train/trainChannels_rCBF.cfg'
    train_rCBV = './examples/configFiles/stroke/train/trainChannels_rCBV.cfg'
    train_Tmax = './examples/configFiles/stroke/train/trainChannels_Tmax.cfg'
    train_GT = './examples/configFiles/stroke/train/trainGtLabels.cfg'

    validation_MTT = './examples/configFiles/stroke/validation/validationChannels_MTT.cfg'
    validation_rCBF = './examples/configFiles/stroke/validation/validationChannels_rCBF.cfg'
    validation_rCBV = './examples/configFiles/stroke/validation/validationChannels_rCBV.cfg'
    validation_Tmax = './examples/configFiles/stroke/validation/validationChannels_Tmax.cfg'
    validation_GT = './examples/configFiles/stroke/validation/validationGtLabels.cfg'

    test_MTT = './examples/configFiles/stroke/test/testChannels_MTT.cfg'
    test_rCBF = './examples/configFiles/stroke/test/testChannels_rCBF.cfg'
    test_rCBV = './examples/configFiles/stroke/test/testChannels_rCBV.cfg'
    test_Tmax = './examples/configFiles/stroke/test/testChannels_Tmax.cfg'
    test_GT = './examples/configFiles/stroke/test/testGtLabels.cfg'

config = Config()
