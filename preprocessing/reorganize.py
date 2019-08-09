import os
from shutil import copyfile

#mainPath = 'F:/Research/data/grayscale/'
mrPath = 'F:/Research/data/resampled/'

for x in range(2, 228):

    #path = mainPath + str(x) + '/'
    mrxpath = mrPath + str(x) + '/'

    label = mrxpath + 'label.nii'

    if not os.path.exists(label):
        continue

    #MTTpath = path + 'MTTnii/MTT.nii'
    #rCBFpath = path + 'rCBFnii/rCBF.nii'
    #rCBVpath = path + 'rCBVnii/rCBV.nii'
    #Tmaxpath = path + 'Tmaxnii/Tmax.nii'



    #newPath = 'F:/Research/data/stroke/' + str(x) + '/'

    newPath = 'F:/Research/data/normalized/' + str(x) + '/'

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

    copyfile(label, newlabel)