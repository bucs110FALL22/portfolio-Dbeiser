from Weather import Weather
from Geoplugin import Geoplugin
from Emoji import Emoji
from OutputFormatter import OutputFormatter
weather = Weather()
geo = Geoplugin()
emoji = Emoji()
output = OutputFormatter(weather,geo,emoji)

def main():
  '''
  retrieves info from geo class, weather class and emogi class, then calls output class to put all of the information into readable ASCII text
  '''
  geo.get()
  weather.get(geo.lat,geo.lon)
  emoji.get(weather.temp)
  output.pprint()

if __name__ == "__main__":
  main()