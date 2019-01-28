import os , shutil
import Extension as ex
adress = input("Enter Director Path")
path = os.path.join(adress)
files = os.listdir(path)

amade = 0
vmade = 0
dmade = 0

def transferaudio(file):
    global amade
    if(amade == 0):
        os.mkdir(path+"\\audio")
        shutil.move(path+file,path+"\\audio")
        amade = 1
    else:
        shutil.move(path+file,path+"\\audio")

def transfervideo(file):
    global vmade
    if(vmade == 0):
        os.mkdir(path+"\\video")
        shutil.move(path+file,path+"\\video")
        vmade = 1
    else:
        shutil.move(path+file,path+"\\video")

def transferdata(file):
    global dmade
    if(dmade == 0):
        os.mkdir(path+"\\data")
        shutil.move(path+file,path+"\\data")
        dmade = 1
    else:
        shutil.move(path+file,path+"\\data")



def configure(res,file):
    if res == 'audio':
        transferaudio(file)
    elif res =="video":
        transfervideo(file)
    elif res == "data":
        transferdata(file)

def filter(file):
    res = ex.checkExtension(file)
    if (res == None):
        print("Invalid Extension "+file)
    else:
        configure(res, file)

for file in files:
    filter(file)
