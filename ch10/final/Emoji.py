import requests
import html

class Emoji:
  def __init__(self):
    self.emotion = ""
    self.api_url = ""
    self.emoji_html = ""
    self.HOT_TEMP = 70
    self.COLD_TEMP = 40
    self.EMOJI_LIST_NUMBER = 0
    self.emoji = ''
  def get(self,weather):
    '''
    gets an a random emoji html code from its called group based on tempreture from emojihub api
    args: weather(int)- tempreture outside
    '''
    if weather >= self.HOT_TEMP:
      self.reaction = "woohoo beach day here I come"
      self.emotion = "face-positive"
    elif weather <= self.COLD_TEMP:
      self.reaction = "not another cold day"
      self.emotion = "face-negative"
    else:
      self.reaction = "could be better, could be worse"
      self.emotion = "face-neutral"
    self.api_url = (f"https://emojihub.yurace.pro/api/random/group/{self.emotion}")
    emoji_response_json = requests.get(self.api_url).json()
    self.emoji_html = emoji_response_json["htmlCode"]

  def emojify(self):
    '''
    turns emoji html code into printable emoji 
    '''
    self.emoji = html.unescape(self.emoji_html[self.EMOJI_LIST_NUMBER])
    