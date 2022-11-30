# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 15:10:25 2021

@author: Waqar
"""
import time

import os
from os import path
import shutil


timestr = time.strftime("%Y%m%d")

src = r"C:\Users\waqar\Downloads\\"
dst = r"N:\COVerAGE-DB\Automation\Idaho-vaccine\\"


#for fileName in os.listdir("."):
 #   os.rename(fileName, fileName.replace("2021", "ali"))
   
  
files = [i for i in os.listdir(src) if i.startswith("Vaccinated") and path.isfile(path.join(src, i))]
for f in files:
    shutil.copy(path.join(src, f), dst)
    os.remove(os.path.join(src, f))
 


old_file = os.path.join(r"N:\COVerAGE-DB\Automation\Idaho-vaccine", "Vaccinated vs General Pop by Age Group.xlsx")
new_file = os.path.join(r"N:\COVerAGE-DB\Automation\Idaho-vaccine", "Vaccinated vs General Pop by Age Group"+timestr+".xlsx")
os.rename(old_file, new_file)
