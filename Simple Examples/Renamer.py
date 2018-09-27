import os;
path = "E:\Walpaper";
data = os.listdir("E:\Walpaper");
i=0;
while(i<len(data)):
    if not data[i].startswith("demo.py"):
        os.rename(os.path.join(path,data[i]),os.path.join(path,str(i)+".jpg"))
    i = i + 1;