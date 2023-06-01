import os
import shutil

from_dir = "c:/users/stanz/downloads"

list = os.listdir(from_dir)
print(list)

for file in list :
    name,ext = os.path.splitext(file)
    print(name)
    print(ext)
