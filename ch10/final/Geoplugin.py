import requests

class Geoplugin():
  def __init__(self):
    self.api_url = "http://www.geoplugin.net/json.gp?ip=xx.xx.xx.xx"
  def get(self):
    '''
    retrieves users ip adress and from this gets the users lat, lon, state, and town using Geoplugin api
    '''
    ip_response_json = requests.get(self.api_url).json()
    self.lat = ip_response_json["geoplugin_latitude"]
    self.lon = ip_response_json["geoplugin_longitude"]
    self.location = (ip_response_json["geoplugin_city"] + " " +  ip_response_json["geoplugin_regionName"])
    if ip_response_json["geoplugin_city"] == "":
      self.location = "YOUR LOCATION"
