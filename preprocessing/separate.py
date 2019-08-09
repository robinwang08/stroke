import os
import pydicom

mainpath = 'F:/Research/newer/'

#mainpath = 'C:/research/deepmedic/data/'

for root, dirs, files in os.walk(mainpath):
    for mainFolder in dirs:
        subfolder = mainpath+mainFolder
        for rootb, dirsb, filesb in os.walk(subfolder):
            seriesList = list()
            for file in filesb:
                dcmpath = subfolder + '/' + file
                if dcmpath.endswith('.dcm'):
                    if os.path.isfile(dcmpath):
                        ds = pydicom.dcmread(dcmpath)
                        series = ds.SeriesNumber
                        if series not in seriesList:
                            seriesList.append(series)

            rCBV = 0
            rCBF = 0
            MTT = 0
            Tmax = 0

            for x in seriesList:
                if x+1 in seriesList and x+2 in seriesList and x+3 in seriesList:
                    rCBV = x
                    rCBF = x+1
                    MTT = x+2
                    Tmax = x+3


            for file in filesb:
                dcmpath = subfolder + '/' + file
                if dcmpath.endswith('.dcm'):
                    if os.path.isfile(dcmpath):
                        ds = pydicom.dcmread(dcmpath)
                        series = ds.SeriesNumber
                        if series == rCBV:
                            rCBVpath = subfolder + '/' + 'rCBV'
                            if not os.path.isdir(rCBVpath):
                                os.makedirs(rCBVpath)
                            newPath = subfolder + '/' + 'rCBV/' + file
                            os.rename(dcmpath, newPath)

                        if series == rCBF:
                            rCBFpath = subfolder + '/' + 'rCBF'
                            if not os.path.isdir(rCBFpath):
                                os.makedirs(rCBFpath)
                            newPath = subfolder + '/' + 'rCBF/' + file
                            os.rename(dcmpath, newPath)

                        if series == MTT:
                            MTTpath = subfolder + '/' + 'MTT'
                            if not os.path.isdir(MTTpath):
                                os.makedirs(MTTpath)
                            newPath = subfolder + '/' + 'MTT/' + file
                            os.rename(dcmpath, newPath)

                        if series == Tmax:
                            Tmaxpath = subfolder + '/' + 'Tmax'
                            if not os.path.isdir(Tmaxpath):
                                os.makedirs(Tmaxpath)
                            newPath = subfolder + '/' + 'Tmax/' + file
                            os.rename(dcmpath, newPath)
