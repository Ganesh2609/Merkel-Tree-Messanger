import os
import shutil

path = "F:/Ganesh/Amrita/Subjects/Sem 3/Data Structures and Algorithms 2/Project/22017_22020"
subdirs = list(os.walk(path))[0][1]
# subdirs.remove(".dist")
# subdirs.remove("__pycache__")
# print(subdirs)

for i in subdirs:
    tempdir = list(os.walk(os.path.join(path,i)))[0][1]
    tempfi = list(os.walk(os.path.join(path,i)))[0][2]
    for j in tempdir:
        #print(os.path.join(path,i,j))
        #os.rmdir(os.path.join(path,i,j))
        shutil.rmtree(os.path.join(path,i,j))
    for j in tempfi:
        #print(os.path.join(path,i,j))
        os.remove(os.path.join(path,i,j))