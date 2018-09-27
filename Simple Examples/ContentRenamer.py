import  fileinput;
import os;
path = "E:\pythonProjects\Simple Examples\phpFiles";
data = os.listdir(path);
i=0;

wordtofind = input("Enter Word To Find");
wordtoreplace = input("Enter Word To Replace");

def manipulate(param):
    rfile = open(param).read()
    if rfile.__contains__(wordtofind):
        rfile = rfile.replace(wordtofind,wordtoreplace)
    wfile = open(param,'w')
    wfile.write(rfile)
    wfile.close()

while (i<len(data)):
    if not data[i].startswith("Python.py"):
        manipulate(data[i])
    i=i+1;