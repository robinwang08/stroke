
import os

mainpath = 'F:/Research/data/grayscale/'

for root, dirs, files in os.walk(mainpath):
    for mainFolder in dirs:
        subfolder = mainpath + mainFolder
        for rootb, dirsb, filesb in os.walk(subfolder):

            for outfile in filesb:
                deleteFile = subfolder + '/' + outfile
                if os.path.exists(deleteFile):
                    os.remove(deleteFile)

            for dirsc in dirsb:
                subsubfolder = subfolder + '/' + dirsc
                for rootd, dirsd, filesd in os.walk(subsubfolder):
                    for file in filesd:
                        dcmpath = subsubfolder + '/' + file
                        if "-" not in dcmpath:
                            os.remove(dcmpath)


