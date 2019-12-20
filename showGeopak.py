import pygetwindow as gw
import time, os

try:
    global PATH_TXT
    PATH_TXT = os.path.join(os.path.dirname(__file__), "Data/TextFile1.txt")
except (FileNotFoundError):
        print("Wrong file or file path textFile1.txt")

try:
    global PATH_INI
    PATH_INI = "C:\RemoteCmd\Status.ini"
except (FileNotFoundError):
        print("Wrong file or file path Status.ini")

try:
    f = open(PATH_INI, "r+")
    val = f.readlines()
    if(val[1][17] == '2'):

        if(val[1][18] == '0'):
            var = '490035-2000'
        else:
            var = '490035-2100'

    else:

        if(val[1][18] == '2'):
            var = '490035-3200'
        else:
            var = '490035-3300'

    f.close()               

except:
    print("Closing file not found")

print(gw.getAllTitles(), var)
f = open(PATH_TXT, "w")
contents = gw.getAllTitles()
for w in gw.getAllTitles():
    print("a")
    f.write(w+ '\n')
f.close()
time.sleep(5)
notepadWindow = gw.getWindowsWithTitle('GEOPAK Mode Répétition in MCOSMOS-1 v4.2.R2   - ' + var)[0]
notepadWindow.activate()