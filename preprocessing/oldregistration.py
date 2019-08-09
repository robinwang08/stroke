

import os
from pathlib import Path

mainPath = 'F:/Research/data/grayscale/'
rawMain = 'F:/Research/data/segmented/'

for x in range(1, 228):
    path = mainPath + str(x) + '/'
    unixPath = './data/grayscale/' + str(x) + '/'
    rawPathFile = rawMain + str(x) + '/' + str(x) + '.nii'
    unixrawPathFile = './data/segmented/' + str(x) + '/' + str(x) + '.nii'

    if not os.path.exists(rawPathFile):
        continue

    if not os.path.exists(path):
        continue

    #grayscales
    MTTpath = path + 'MTTnii'
    rCBFpath = path + 'rCBFnii'
    rCBVpath = path + 'rCBVnii'
    Tmaxpath = path + 'Tmaxnii'

    unixMTTpath = unixPath + 'MTTnii'
    unixrCBFpath = unixPath + 'rCBFnii'
    unixrCBVpath = unixPath + 'rCBVnii'
    unixTmaxpath = unixPath + 'Tmaxnii'

    initialCommand = '/mnt/c/Program\ Files/Slicer\ 4.10.2/Slicer.exe --launch BRAINSFit --fixedVolume '

    outpath = path + 'MRregistered'
    if not os.path.exists(outpath):
        os.mkdir(outpath)

    if os.path.isdir(MTTpath):
        outpath = './data/grayscale/' + str(x) + '/MRregistered'
        command = initialCommand + '\'' + unixrawPathFile + '\'' + ' --movingVolume ' + '\'' + unixMTTpath + '/MTT.nii' + '\'' + ' --outputVolume ' + '\'' + outpath + '/registeredMTT.nii' + '\'' + ' --transformType Rigid,ScaleVersor3D,ScaleSkewVersor3D,Affine --initializeTransformMode useMomentsAlign --interpolationMode Linear --samplingPercentage .02'
        print(command)
    else:
        print('Error, missing MTT for ' + str(x))

    if os.path.isdir(rCBFpath):
        outpath = './data/grayscale/' + str(x) + '/MRregistered'
        command = initialCommand + '\'' + unixrawPathFile + '\'' + ' --movingVolume ' + '\'' + unixrCBFpath + '/rCBF.nii' + '\'' + ' --outputVolume ' + '\'' + outpath + '/registeredrCBF.nii' + '\'' + ' --transformType Rigid,ScaleVersor3D,ScaleSkewVersor3D,Affine --initializeTransformMode useMomentsAlign --interpolationMode Linear --samplingPercentage .02'
        print(command)
    else:
        print('Error, missing rCBF for ' + str(x))

    if os.path.isdir(rCBVpath):
        outpath = './data/grayscale/' + str(x) + '/MRregistered'
        command = initialCommand + '\'' + unixrawPathFile + '\'' + ' --movingVolume ' + '\'' + unixrCBVpath + '/rCBV.nii' + '\'' + ' --outputVolume ' + '\'' + outpath + '/registeredrCBV.nii' + '\'' + ' --transformType Rigid,ScaleVersor3D,ScaleSkewVersor3D,Affine --initializeTransformMode useMomentsAlign --interpolationMode Linear --samplingPercentage .02'
        print(command)
    else:
        print('Error, missing rCBV for ' + str(x))

    if os.path.isdir(Tmaxpath):
        outpath = './data/grayscale/' + str(x) + '/MRregistered'
        command = initialCommand + '\'' + unixrawPathFile + '\'' + ' --movingVolume ' + '\'' + unixTmaxpath + '/Tmax.nii' + '\'' + ' --outputVolume ' + '\'' + outpath + '/registeredTmax.nii' + '\'' + ' --transformType Rigid,ScaleVersor3D,ScaleSkewVersor3D,Affine --initializeTransformMode useMomentsAlign --interpolationMode Linear --samplingPercentage .02'
        print(command)
    else:
        print('Error, missing Tmax for ' + str(x))
