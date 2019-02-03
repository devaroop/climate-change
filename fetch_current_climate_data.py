import requests, json
import time, datetime
#import ciso8601
#def get_unix_time (s):
 #   return time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple())
    # to get time in seconds:
    #return time.mktime(ts.timetuple())

# Enter your API key here 
api_key = "0c6527e1e073a790890aa665fb699de3"
lat_n_long = "18.5204,73.8567"

# base_url variable to store url 
base_url = "https://api.darksky.net/forecast/"
  
# Give city name 
city_name = "Pune"

#time = str(get_unix_time("03/02/2019"))
#time = "2018-02-01T00:00:00"
# complete_url variable to store 
# complete url address 
complete_url = base_url + api_key + "/" + lat_n_long
#complete_url += "," + time
# get method of requests module 
# return response object 
response = requests.get(complete_url) 
  
# json method of response object  
# convert json format data into 
# python format data 
x = response.json()
x = json.dumps(json.loads(response.text), indent=4, ensure_ascii=False)
print(x)

