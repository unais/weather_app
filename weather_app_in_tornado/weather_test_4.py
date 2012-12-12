'''
Created on 10-Dec-2012

@author: unais
'''
import urllib2
import ast
import tornado.ioloop
import tornado.web



def getWeatherCondition(city) :
    try :
        url = "http://openweathermap.org/data/2.1/forecast/city?q="
        url += city
        req = urllib2.Request(url)
        response=urllib2.urlopen(req)
    except Exception :
        print("Not a matched city")
    return response.read()
"""
def get_tem(city):
    Data_str =  getWeatherCondition(city)
    Data = ast.literal_eval(Data_str)  # for converting string to dict
    Temperature =  Data['list'][0]['main']['temp']
    Humidity    =  Data['list'][0]['main']['humidity']
    Pressure    =  Data['list'][0]['main']['pressure']
    print "Temperature : " , Temperature - 272.15 , "Celcius"
    print "Humidity    : " , Humidity , "%"
    print "Pressure    : " , Pressure , "mbar"
    return Temperature

"""

def print_weather(place):
    Data_str =  getWeatherCondition(place)
    Data = ast.literal_eval(Data_str)
   # print Data
    Temperature =  Data['list'][0]['main']['temp']
    Humidity    =  Data['list'][0]['main']['humidity']
    Pressure    =  Data['list'][0]['main']['pressure']
    Result      =  place , Temperature , Humidity , Pressure
    return Result
"""
def Test():
    print_weather("USA")  
    print_weather("Washington")
    print_weather("Havana")
    print_weather("Mumbai")
    print_weather("Palakkad")
    print_weather("Kochi")
    print_weather("Chennai")
  """
   
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        weather_data = print_weather("Kochi")
        data = weather_data[0] +"Temperature : "+str(weather_data[1]) +"Humidity: "+ str(weather_data[2]) +"Pressure :" + str(weather_data[3])
        self.write(data)

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()