from Weather import Weather
from Geoplugin import Geoplugin
from Emoji import Emoji
import pyfiglet
class OutputFormatter():
  def __init__(self,weather,geoplugin,emoji):
    self.FONT = 'big'
    self.EMOJI_MULTI = 3
    self.weather = weather
    self.emoji = emoji
    self.geoplugin = geoplugin
    
  def pprint(self):
    '''
    takes info from other classes, transforms it into ascii text and prints it.
    '''
    self.emoji.emojify()
    text_to_print1 = (f"it's {self.weather.temp} degrees")
    text_to_print2 = (f"in:  {self.geoplugin.location}")
    text_to_print1 = pyfiglet.figlet_format(text_to_print1, font = self.FONT)
    text_to_print2 = pyfiglet.figlet_format(text_to_print2, font = self.FONT)
    text_to_print3 = ((self.emoji.emoji * self.EMOJI_MULTI) +" "+ self.emoji.reaction +" "+  (self.emoji.emoji * self.EMOJI_MULTI))
    print(text_to_print1)
    print(text_to_print2)
    print(text_to_print3)