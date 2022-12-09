import requests

class Weather:
  def __init__(self):
    self.api_url = ''
    self.temp = 0
    self.rain_chance = []
      
  def get(self,lat,lon):
    '''
    gets the tempreture of where the user is using open-meteo api
    args: lat(int) users latatude, lon(int)- users longitude
    '''
    self.api_url = (f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m&temperature_unit=fahrenheit")
    weather_reponse_json = requests.get(self.api_url).json()
    weather_temps = weather_reponse_json["hourly"]["temperature_2m"]
    self.temp = int((sum(weather_temps) / len(weather_temps)))

    