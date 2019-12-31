api="e146e3c1e9413582394cdfd51f8975e8210db0d8"
import moment
import pprint
import os
import random

for i in range(2):
    # x=random.randrange(0,54)
    # y=random.randrange(0,6)
    # date=moment.now().subtract(years=1).add(days=1).add(weeks=x).add(days=y)
    # print(date)
    date="2020-01-01T01:05:13+05.50"
    filePath="./git.txt"
    f=open("git.txt","a")
    f.write(str(date))
    f.close()
    os.system('cmd /c "git status"')
    os.system('cmd /c "git add ."')
    os.system('cmd /c "git commit -m "c2" --date={}"'.format(date))
    os.system('cmd /c "git push origin master"')
        
    
