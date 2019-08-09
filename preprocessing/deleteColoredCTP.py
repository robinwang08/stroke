import os
import shutil

mainpath = 'F:/Research/data/raws/'

for root, dirs, files in os.walk(mainpath):
    for mainFolder in dirs:
        subfolder = mainpath + mainFolder
        for rootb, dirsb, filesb in os.walk(subfolder):
            for dirsc in dirsb:
                if dirsc == 'CT':
                    subsubfolder = subfolder + '/CT'
                    for rootd, dirsd, filesd in os.walk(subsubfolder):
                        for minidir in dirsd:
                            if minidir == 'MTT' or minidir == 'MTTnii' or minidir == 'rCBF' or minidir == 'rCBFnii' or minidir == 'rCBV' or minidir == 'rCBVnii' or minidir == 'SECTRA' or minidir == 'TMAX' or minidir == 'TMAXnii':
                                deleteDir = subsubfolder + '/' + minidir
                                if os.path.exists(deleteDir):
                                    shutil.rmtree(deleteDir)



