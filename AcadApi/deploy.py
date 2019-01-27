from flask import Flask , request
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

class Crawl:
     
  def login(self,urlfromparam,payload):
      self.session_requests = requests.session()
      self.url = urlfromparam
      self.result = self.session_requests.post(self.url,data = payload)
      self.result = self.session_requests.get(
	  'http://acadplusvk.in/student/'
      )
      self.soup = BeautifulSoup(self.result.content,'html.parser')  
      info = self.soup.find_all("h3", class_="panel-title")[0].text
      if(str(info).__contains__('Administrator')):
        return "Invalid Login"
      else:
        return "Login Sucessfully"
  
  def info(self):
      name = self.soup.find_all("h3", class_="panel-title")[0].text
      data= name + "\n"
      table = self.soup.find_all("table",class_="table table")
      for row in table:
        data = data + row.text + "\n"
      return str(data)
  
  def atten(self):
       info = " "
       data = self.soup.select("b")
       for content in data:
         info = info + content.text + "\n"
       return info  
      

c = Crawl()      

@app.route('/login/<username>/<password>')
def status(username,password):
    payload = {
	"myusername":username, 
	"mypassword":password, 
    }
    info = c.login('http://acadplusvk.in/links/usercheck.php',payload) 
    return info

@app.route('/info')
def info():
    return c.info()

@app.route('/attendance')
def attendance():
    return c.atten()

@app.route('/')
def hello():
    return "welcome TO ERP API"  
  
        
    
   


if __name__ == '__main__':
   app.run()
