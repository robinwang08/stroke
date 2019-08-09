import os
import pydicom

mainpath = 'F:/Research/newer/'

for root, dirs, files in os.walk(mainpath):
    for mainFolder in dirs:
        subfolder = mainpath+mainFolder
        for rootb, dirsb, filesb in os.walk(subfolder):
            accession = 0
            for file in filesb:
                dcmpath = subfolder + '/' + file
                if dcmpath.endswith('.dcm'):
                    ds = pydicom.dcmread(dcmpath)
                    accession = ds.AccessionNumber
                    series = str(ds.SeriesNumber)
                    instance = str(ds.InstanceNumber)
                    newName = series + '-' + instance + '.dcm'
                    newPath = subfolder + '/' + newName
                    try:
                        os.rename(dcmpath, newPath)
                    except FileExistsError:
                        print(dcmpath + ' file error')
                if dcmpath.endswith('.xml'):
                    os.remove(dcmpath)
        oldNamePath = mainpath + mainFolder
        newNamePath = mainpath + str(accession)
        os.rename(oldNamePath, newNamePath)
