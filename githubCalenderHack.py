import moment
import pprint
import os
import random

for i in range(150):
    y=random.randrange(0,54)
    x=random.randrange(0,6)
    date=moment.now().subtract(years=1).add(days=1).add(days=x).add(weeks=y)
    print(date)
    filePath="./git.txt"
    f=open("git.txt","a")
    f.write(str(date))
    f.close()
    os.system('cmd /c "git status"')
    os.system('cmd /c "git add ./git.txt"')
    os.system('cmd /c "git commit -m "c1" --date={}"'.format(date))
os.system('cmd /c "git push origin master"')    
    
