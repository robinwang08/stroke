import dicom2nifti
import os
import gzip
import shutil

fromPath = 'F:/Research/data/raw'

for x in range(2, 3):
    path = fromPath + '/' + str(x) + '/CT/separate'
    toPath = fromPath + '/' + str(x) + '/CT/rawnii/'
    if os.path.isdir(path):
        firstFolder = os.listdir(path)
        singleFolderPath = path + '/' + firstFolder[0] + '/'
        if not os.path.isdir(toPath):
            os.mkdir(toPath)
        dicom2nifti.convert_directory(singleFolderPath, toPath)

        rawnii = os.listdir(toPath)
        if len(rawnii) > 1:
            print('Error, more than 1 file output ' + str(x))

        fileName = toPath + '/' + rawnii[0]
        newFileName = toPath + '/raw.nii'

        with gzip.open(fileName, 'rb') as f_in:
            with open(newFileName, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        os.remove(fileName)

            #dicom2nifti.dicom_series_to_nifti(singleFolderPath, toPath, reorient_nifti=True)
        #except:
            #print("An exception occurred: " + str(x))
