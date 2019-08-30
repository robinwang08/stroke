import os
from shutil import copyfile

mainPath = 'F:/Research/data/segmented/'
mrPath = 'F:/Research/data/resampled/'

for x in range(2, 228):

    path = mainPath + str(x) + '/MRregistered/registered' + str(x) + 'label.nii'

    if not os.path.exists(path):
        continue

    #MTTpath = path + 'MTTnii/MTT.nii'
    #rCBFpath = path + 'rCBFnii/rCBF.nii'
    #rCBVpath = path + 'rCBVnii/rCBV.nii'
    #Tmaxpath = path + 'Tmaxnii/Tmax.nii'

    newPath = mrPath + str(x) + '/'

    if not os.path.exists(newPath):
        os.mkdir(newPath)

    #newMTTpath = newPath + 'MTT.nii'
    #newrCBFpath = newPath + 'rCBF.nii'
    #newrCBVpath = newPath + 'rCBV.nii'
    #newTmaxpath = newPath + 'Tmax.nii'

    newlabel = newPath + 'label.nii'

    #copyfile(MTTpath, newMTTpath)
    #copyfile(rCBFpath, newrCBFpath)
    #copyfile(rCBVpath, newrCBVpath)
    #copyfile(Tmaxpath, newTmaxpath)

    copyfile(path, newlabel)
