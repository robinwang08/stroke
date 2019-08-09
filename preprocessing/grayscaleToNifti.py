import os
import dicom2nifti
import gzip
import shutil

mainPath = 'F:/Research/data/grayscale/'

for x in range(8, 228):
    path = mainPath + str(x) + '/'

    if not os.path.isdir(path):
        continue

    #grayscale maps
    MTTpath = path + 'MTT'
    rCBFpath = path + 'rCBF'
    rCBVpath = path + 'rCBV'
    Tmaxpath = path + 'Tmax'

    MTTniipath = path + 'MTTnii'
    rCBFniipath = path + 'rCBFnii'
    rCBVniipath = path + 'rCBVnii'
    Tmaxniipath = path + 'Tmaxnii'

    if not os.path.exists(MTTniipath):
            os.mkdir(MTTniipath)
            dicom2nifti.convert_directory(MTTpath, MTTniipath)
            rawnii = os.listdir(MTTniipath)
            fileName = MTTniipath + '/' + rawnii[0]
            newFileName = MTTniipath + '/MTT.nii'
            with gzip.open(fileName, 'rb') as f_in:
                with open(newFileName, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            os.remove(fileName)

    if not os.path.exists(rCBFniipath):
            os.mkdir(rCBFniipath)
            dicom2nifti.convert_directory(rCBFpath, rCBFniipath)
            rawnii = os.listdir(rCBFniipath)
            fileName = rCBFniipath + '/' + rawnii[0]
            newFileName = rCBFniipath + '/rCBF.nii'
            with gzip.open(fileName, 'rb') as f_in:
                with open(newFileName, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            os.remove(fileName)

    if not os.path.exists(rCBVniipath):
            os.mkdir(rCBVniipath)
            dicom2nifti.convert_directory(rCBVpath, rCBVniipath)
            rawnii = os.listdir(rCBVniipath)
            fileName = rCBVniipath + '/' + rawnii[0]
            newFileName = rCBVniipath + '/rCBV.nii'
            with gzip.open(fileName, 'rb') as f_in:
                with open(newFileName, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            os.remove(fileName)

    if not os.path.exists(Tmaxniipath):
            os.mkdir(Tmaxniipath)
            dicom2nifti.convert_directory(Tmaxpath, Tmaxniipath)
            rawnii = os.listdir(Tmaxniipath)
            fileName = Tmaxniipath + '/' + rawnii[0]
            newFileName = Tmaxniipath + '/Tmax.nii'
            with gzip.open(fileName, 'rb') as f_in:
                with open(newFileName, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            os.remove(fileName)
