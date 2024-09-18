# i have used few lib win10toast,request as well bs4
#win10toast is used to show desktop notification
#request is used to get the data from the website
#bs4 is used to parse the data
#Win10toast does not work in replit (Be carefull) and Enjoy guys :)
import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
# Replace with your own OpenWeatherMap API key
API_KEY="cb996ab5a5b9f33dea4fd5ad2843d"
CITY = 'Gandhinagar'  # Replace with your desired city

def get_current_temperature(API_KEY, CITY):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        return temperature
    else:
        return None

def main():
    toaster = ToastNotifier()
    temperature = get_current_temperature(API_KEY, CITY)
    
    if temperature is not None:
        message = (f"The current temperature in {CITY} is {temperature}°C.")
        toaster.show_toast("Current Temperature", message, duration=10)
    else:
        toaster.show_toast("Error", "Could not retrieve temperature data.", duration=10)

if __name__ == "__main__":
    main()