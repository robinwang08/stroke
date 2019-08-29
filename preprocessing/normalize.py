from __future__ import division
import os
import nibabel as nib
import numpy as np


def getMax():
    mainPath = 'F:/Research/data/resampled/'
    mttMax = 0
    rcbfMax = 0
    rcbvMax = 0
    tmaxMax = 0
    labelMax = 0

    for x in range(2, 228):
        path = mainPath + str(x)
        MTT = path + '/MTT.nii'
        if not os.path.exists(MTT):
            continue
        MTT = path + '/MTT.nii'
        n1_img = nib.load(MTT)
        img = n1_img.get_fdata()
        imgmax = img.max()
        if imgmax > mttMax:
            mttMax = imgmax
        rCBF = path + '/rCBF.nii'
        n1_img = nib.load(rCBF)
        img = n1_img.get_fdata()
        imgmax = img.max()
        if imgmax > rcbfMax:
            rcbfMax = imgmax
        rCBV = path + '/rCBV.nii'
        n1_img = nib.load(rCBV)
        img = n1_img.get_fdata()
        imgmax = img.max()
        if imgmax > rcbvMax:
            rcbvMax = imgmax
        Tmax = path + '/Tmax.nii'
        n1_img = nib.load(Tmax)
        img = n1_img.get_fdata()
        imgmax = img.max()
        if imgmax > tmaxMax:
            tmaxMax = imgmax

        label = path + '/label.nii'
        n1_img = nib.load(label)
        img = n1_img.get_fdata()
        imgmax = img.max()
        if imgmax > labelMax:
            labelMax = imgmax

        print('done with ' + str(x))


    f = open('F:/Research/data/ctnormalize.txt','a+')
    f.write('MTT: ' + str(mttMax) + '\n')
    f.write('rCBF: ' + str(rcbfMax) + '\n')
    f.write('rCBV: ' + str(rcbvMax) + '\n')
    f.write('Tmax: ' + str(tmaxMax) + '\n')
    f.write('label: ' + str(labelMax) + '\n')
    return

def normalize():
    mainPath = 'F:/Research/data/resampled/'
    newPath = 'F:/Research/data/normalized/'

    mttMax = 46.06916046142578
    rcbfMax = 655.3499755859375
    rcbvMax = 268.0205993652344
    tmaxMax = 60.0

    for x in range(2, 228):
        path = mainPath + str(x)
        normPath = newPath + str(x)

        MTT = path + '/MTT.nii'
        newMTT = normPath + '/MTT.nii'

        if not os.path.exists(MTT):
            continue

        if not os.path.exists(normPath):
            os.mkdir(normPath)

        n1_img = nib.load(MTT)
        n1_header = n1_img.header
        n1_affine = n1_img.affine
        img = n1_img.get_fdata()
        img = np.true_divide(img, mttMax)
        new_img = nib.Nifti1Image(img, n1_affine, n1_header)
        nib.save(new_img, newMTT)

        rCBF = path + '/rCBF.nii'
        newrCBF = normPath + '/rCBF.nii'
        n1_img = nib.load(rCBF)
        n1_header = n1_img.header
        n1_affine = n1_img.affine
        img = n1_img.get_fdata()
        img = np.true_divide(img, rcbfMax)
        new_img = nib.Nifti1Image(img, n1_affine, n1_header)
        nib.save(new_img, newrCBF)

        rCBV = path + '/rCBV.nii'
        newrCBV = normPath + '/rCBV.nii'
        n1_img = nib.load(rCBV)
        n1_header = n1_img.header
        n1_affine = n1_img.affine
        img = n1_img.get_fdata()
        img = np.true_divide(img, rcbvMax)
        new_img = nib.Nifti1Image(img, n1_affine, n1_header)
        nib.save(new_img, newrCBV)

        Tmax = path + '/Tmax.nii'
        newTmax = normPath + '/Tmax.nii'
        n1_img = nib.load(Tmax)
        n1_header = n1_img.header
        n1_affine = n1_img.affine
        img = n1_img.get_fdata()
        img = np.true_divide(img, tmaxMax)
        new_img = nib.Nifti1Image(img, n1_affine, n1_header)
        nib.save(new_img, newTmax)

def getROI():
    mainPath = 'F:/Research/data/padded/'
    newPath = 'F:/Research/data/padded/'

    for x in range(2, 228):
        path = mainPath + str(x)
        normPath = newPath + str(x)

        MTT = path + '/MTT.nii'
        newMTT = normPath + '/mask.nii'

        if not os.path.exists(MTT):
            continue

        if not os.path.exists(normPath):
            os.mkdir(normPath)

        n1_img = nib.load(MTT)
        n1_header = n1_img.header
        n1_affine = n1_img.affine
        img = n1_img.get_fdata()
        img[img > 0] = 1

        new_img = nib.Nifti1Image(img, n1_affine, n1_header)
        nib.save(new_img, newMTT)


def getISLESROI():
    mainPath = 'F:/Research/isles2/'
    newPath = 'F:/Research/isles2/'

    for x in range(1, 95):
        path = mainPath + 'case_' + str(x)
        normPath = newPath + 'case_' + str(x)

        MTT = path + '/CT_MTT.nii'
        newMTT = normPath + '/mask.nii'

        if not os.path.exists(MTT):
            continue

        if not os.path.exists(normPath):
            os.mkdir(normPath)

        n1_img = nib.load(MTT)
        n1_header = n1_img.header
        n1_affine = n1_img.affine
        img = n1_img.get_fdata()
        img[img > 0] = 1

        new_img = nib.Nifti1Image(img, n1_affine, n1_header)
        nib.save(new_img, newMTT)


def getPad():
    mainPath = 'F:/Research/data/normalized/'
    newPath = 'F:/Research/data/padded/'

    for x in range(2, 228):
        path = mainPath + str(x)
        normPath = newPath + str(x)
        MTT = path + '/MTT.nii'
        newMTT = normPath + '/MTT.nii'
        if not os.path.exists(MTT):
            continue
        if not os.path.exists(normPath):
            os.mkdir(normPath)

        n1_img = nib.load(MTT)
        n1_header = n1_img.header
        n1_affine = n1_img.affine
        img = n1_img.get_fdata()
        # add padding
        padded = np.pad(img, ((0, 0), (0, 0), (18, 18)), 'constant', constant_values=(0, 0))
        new_img = nib.Nifti1Image(padded, n1_affine, n1_header)
        nib.save(new_img, newMTT)

        rCBF = path + '/rCBF.nii'
        newrCBF = normPath + '/rCBF.nii'
        n1_img = nib.load(rCBF)
        n1_header = n1_img.header
        n1_affine = n1_img.affine
        img = n1_img.get_fdata()
        # add padding
        padded = np.pad(img, ((0, 0), (0, 0), (18, 18)), 'constant', constant_values=(0, 0))
        new_img = nib.Nifti1Image(padded, n1_affine, n1_header)
        nib.save(new_img, newrCBF)

        rCBV = path + '/rCBV.nii'
        newrCBV = normPath + '/rCBV.nii'
        n1_img = nib.load(rCBV)
        n1_header = n1_img.header
        n1_affine = n1_img.affine
        img = n1_img.get_fdata()
        # add padding
        padded = np.pad(img, ((0, 0), (0, 0), (18, 18)), 'constant', constant_values=(0, 0))
        new_img = nib.Nifti1Image(padded, n1_affine, n1_header)
        nib.save(new_img, newrCBV)

        Tmax = path + '/Tmax.nii'
        newTmax = normPath + '/Tmax.nii'
        n1_img = nib.load(Tmax)
        n1_header = n1_img.header
        n1_affine = n1_img.affine
        img = n1_img.get_fdata()
        # add padding
        padded = np.pad(img, ((0, 0), (0, 0), (18, 18)), 'constant', constant_values=(0, 0))
        new_img = nib.Nifti1Image(padded, n1_affine, n1_header)
        nib.save(new_img, newTmax)

        label = path + '/label.nii'
        newLabel = normPath + '/label.nii'
        n1_img = nib.load(label)
        n1_header = n1_img.header
        n1_affine = n1_img.affine
        img = n1_img.get_fdata()
        # add padding
        padded = np.pad(img, ((0, 0), (0, 0), (18, 18)), 'constant', constant_values=(0, 0))
        new_img = nib.Nifti1Image(padded, n1_affine, n1_header)
        nib.save(new_img, newLabel)

getISLESROI()