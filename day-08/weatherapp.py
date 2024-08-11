import requests


# api_key = "40f37c911820e9f79b38ca25c98f6815"

##


# while True:
#     city = input("Enter the city name : ")
#     url = f'http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&appid={api_key}'
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         tamp = data['main']['temp']
#         desc = data['weather'][0]['description']
#         print(f"The Temprature of {city} is {tamp:.1f}C and {desc}")

#     else:
#         print("Featching error")
    
    
#     if city == 'exit':
#         break


    
class City:
    def __init__(self,city):
        self.city = city
        self.get_data()

    def get_data(self):
        try: 
            # self.url = f'http://api.openweathermap.org/data/2.5/weather?units=metric&q={self.city}&appid=40f37c911820e9f79b38ca25c98f6815'
            self.responce = requests.get( f'http://api.openweathermap.org/data/2.5/weather?units=metric&q={self.city}&appid=40f37c911820e9f79b38ca25c98f6815')
        except:
            print({"Internet issue :("})

        self.data = self.responce.json()
        self.temp = self.data['main']['temp']
        self.desc = self.data['weather'][0]['description']
        self.temp_min = self.data['main']['temp_min']
        self.temp_max = self.data['main']['temp_max']
    def temp_print(self):
        print(f"The Temprature of {self.city} is {self.temp:.1f}° C")
        print(f'The Description is : {self.desc}')
        print(f"Today's High Temparature is: {self.temp_max}° C")
        print(f"Today's Minimum Temparature is: {self.temp_min}° C")




while True:
    city = input("Enter the City Name that you want to check  Temprature: ")
    if city == 'exit':
       break
    city1 = City(city)
    city1.temp_print()
    
