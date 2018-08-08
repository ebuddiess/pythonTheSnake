import requests as rq;
import json;
import random;
import ctypes;
import  urllib.request as downloader;
json_data = "";

class Details:
    def __init__(self):
        self.per_page=3;
        self.query="";
    def askUser(self):
        query =  input("Which Type of Wallpaper You Are Looking For ?");
        self.query = query;
        per_page = input("Enter No of Per_page Result You Want ?");
        self.per_page = per_page;


def changeWallpaper(json_data):
    imageList = [];
    for data in json_data["hits"]:
        imageList.append(data['largeImageURL'])

    imagelistLength = len(imageList);
    selectedWalpapernumber = random.randint(0, imagelistLength)
    selectedWallpaper = imageList[selectedWalpapernumber]
    print(selectedWallpaper);
    path = "E:\\Walpaper\\walpaper.jpg";
    downloader.urlretrieve(selectedWallpaper, path);
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)

def main():
     try:
         details = Details();
         details.askUser();
         response = rq.get(url='https://pixabay.com/api/?key=9765780-e9549c9bebccb5f2a2b4235c4&q='+details.query+'&image_type=photo&per_page='+details.per_page, timeout=5);
         json_data = json.loads(response.content);
         changeWallpaper(json_data);
     except:
         print("No Internet Found")

if __name__== "__main__":
    main()