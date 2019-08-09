import os
import pydicom


def processFiles(mainpath, orig):
    if not os.path.isdir(mainpath):
        return
    for root, dirs, files in os.walk(mainpath):
        for mainFolder in dirs:
            subfolder = mainpath + '/' + mainFolder
            for rootb, dirsb, filesb in os.walk(subfolder):
                for subdirsb in dirsb:
                    subfolderb = mainpath + '/' + mainFolder + '/' + subdirsb
                    for rootc, dirsc, filesc in os.walk(subfolderb):
                        for subdirsc in dirsc:
                            subfolderc = subfolderb + '/' + subdirsc
                            for rootd, dirsd, filesd in os.walk(subfolderc):
                                for subdirsc in dirsd:
                                    subfolderd = subfolderc + '/' + subdirsc
                                    for roote, dirse, filese in os.walk(subfolderd):
                                        for files in filese:
                                            filePath = subfolderd + '/' + files
                                            rawPath = orig + 'raw/'
                                            if not os.path.exists(rawPath):
                                                os.makedirs(rawPath)
                                            newPath = rawPath + files
                                            os.rename(filePath, newPath)
    return


path = 'F:/Research/data/raw'

for x in range(228):
    z = path + '/' + str(x + 1) + '/CT/'
    y = z + 'DICOM'
    processFiles(y, z)



