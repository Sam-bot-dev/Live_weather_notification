# i have used few lib win10toast,request as well bs4
#win10toast is used to show desktop notification
#request is used to get the data from the website
#bs4 is used to parse the data
import requests
from win10toast import ToastNotifier
from bs4 import BeautifulSoup
n=ToastNotifier()
def getdata(url):
    r=requests.get(url="https://weather.com/en-IN/?Goto=Redirected")
    return r.text
htmldata= getdata("https://weather.com/en-IN/?Goto=Redirected")
soup=BeautifulSoup(htmldata,"html.parser")
current_temp=soup.find_all("span",class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY")
chances_rain = soup.find_all("div",  
                             class_= "_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf") 
temp = (str(current_temp))    
temp_rain = (str(chances_rain) )

result = "current_temp " + temp[128:-9] + "  in Gandhinagar" + "\n" +temp_rain[131:-14] 
n.show_toast("Weather update", result, duration = 10)