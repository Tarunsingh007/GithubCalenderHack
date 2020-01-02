api="e146e3c1e9413582394cdfd51f8975e8210db0d8"
import moment
import pprint
import os
from git import *


filePath="./git.txt"
date=moment.now()
print(date)

f=open("git.txt","a")
f.write(str(date))
f.close()

# # for i in range(1):
# os.system('cmd /c "git status"')
# os.system('cmd /c "git add ."')
# # os.system('cmd /c "git commit -m "c2""')
# # os.system('cmd /c "git push origin master"')
    
    
