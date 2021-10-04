import os



diret = "C:\\ffmpeg-20190601-4158865-win64-static\\bin\\"
diretIN = "D:\\Nnet\\RawDataset\\KyarrilKara\\"
diretOUT = "D:\\Nnet\\ProcessedDataset\\KyarrilKara\\"

path = diretIN

file_list = os.listdir(path)

data = []

for aa in file_list:

    import copy
    copyA = copy.deepcopy(aa)

    aa = aa.replace("【Karaoke】 ", "",1)
    aa = aa.replace("【Karaoke】", "",1)
    
    aa = aa.replace("[Karaoke] ", "",1)
    aa = aa.replace("[karaoke]", "",1)

    aa = aa.replace("【on vocal】 ", "[1]",1)
    aa = aa.replace("【on vocal】", "[1]",1)

    aa = aa.replace("【off vocal】 ", "[0]",1)
    aa = aa.replace("【off vocal】", "[0]",1)
    
    aa = aa.replace("[on vocal] ", "[1]",1)
    aa = aa.replace("[on vocal]", "[1]",1)

    aa = aa.replace("[off vocal] ", "[0]",1)
    aa = aa.replace("[off vocal]", "[0]",1)
    
    aa = aa.replace("[Karaoke  on vocal] ", "[1]",1)
    aa = aa.replace("[Karaoke  on vocal]", "[1]",1)

    aa = aa.replace("[Karaoke  off vocal] ", "[0]",1)
    aa = aa.replace("[Karaoke  off vocal]", "[0]",1)

    aa = (aa.encode('ascii', 'ignore')).decode("utf-8")

    if "[0]" in aa:
        aa = aa.replace("[0]", "",1)
        aa = "[0]" + aa
        data.append([aa,copyA])
    elif "[1]" in aa:
        aa = aa.replace("[1]", "",1)
        aa = "[1]" + aa
        data.append([aa,copyA])
 
data.sort()

import shutil

ToFile = []
for aaa in data:

    if "[0]" in aaa[0]:

        for bbb in data:

            if "[1]" in bbb[0]:
                if aaa[0][3:] in bbb[0][3:]:
                    ToFile.append([aaa,bbb])
                    #print(aaa)
                    #print(bbb)
                    break

import numpy as np
import subprocess

np.save(diretOUT + "KyarrilKara", ToFile)
an = np.load( diretOUT +"KyarrilKara.npy")

for ss in an:
    
    A = ss[0][1][:-4]
    B = ss[0][0][:-4]
    result = subprocess.Popen(
        diret+"ffmpeg -i "+'"'+diretIN+A+".mp4"+'"'+" -vn -acodec copy "+'"'+diretOUT+B+".aac"+'"', 
        shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = result.communicate()
    result.kill()
    print( ss[0][0][:-4] )
    
    A = ss[1][1][:-4]
    B = ss[1][0][:-4]
    result = subprocess.Popen(
        diret+"ffmpeg -i "+'"'+diretIN+A+".mp4"+'"'+" -vn -acodec copy "+'"'+diretOUT+B+".aac"+'"', 
        shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = result.communicate()
    result.kill()
    print( ss[1][0][:-4] )

print(len(an))


