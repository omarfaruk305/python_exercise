import requests
from bs4 import BeautifulSoup
import re

from sqlalchemy import between


from page import Page


cities = [["Amsterdam", "2759794"], [
    "Groningen", '2755251'], ["Rotterdam", '2747891']]


class Weather:

    # Add your parameters
    def __init__(self, city_id):
        """
        This init functiom takes the city, which is an id.

        It also requests the page, and stores the result of the request in the self.page
        """

        # Compose your request URL here
        url = f"https://www.bbc.com/weather/{city_id}"

        # Request the page -> Create a instance of the Page class here with the url you have created above
        requested_page = Page(url)

        # Get the Beautiful Soup HTML page -> call the get_html method of requested_page
        self.page = requested_page.get_html()

    # Add get_weather method
    def get_weather(self, days):
        """
        Takes as parameter the max number of days (between 1 and 6).

        Should return an array of dictonaries per day with the day, weather type
        max. degrees celcius and min. degrees celcius.
        """
        listofdays = []

        for day in range(days):

            mainpath = self.page.find('a', id=f'daylink-{day}')
            mainpath_celcius = mainpath.find_all(
                'span', {'class': "wr-value--temperature--c"})
            weather = mainpath.find('div', {
                'class': 'wr-day__weather-type-description wr-js-day-content-weather-type-description wr-day__content__weather-type-description--opaque'}).text

            if mainpath.find(['div', 'span'], class_='wr-date').span is not None:
                day = mainpath.find(
                    ['div', 'span'], class_='wr-date').find('span', class_='wr-date__long').next
            else:
                day = mainpath.find('span', class_='wr-date').text
            date = mainpath.find('span',class_ = 'wr-date__longish').text
            print(date)

            # will ask
            # day = self.page.find(
            #     'div',class_ = "wr-c-map-controls")
            # print(day)

            # print(day)
            if len(mainpath_celcius) == 1:
                mainpath_celcius.append((mainpath_celcius[0]))
            listofdays.append([{'max_celcius': mainpath_celcius[0].text,
                                'min_celcius': mainpath_celcius[1].text,
                                'weather': weather,
                                'day':day}])

        # Add your Beautiful Soup code here to extract all the necessary data

        # Limit the number of returned items from the list, by using list slicing
        return listofdays

    # Your print function
    def print_weather(self, day):
        """
        This function takes the data of a single day, and prints a string that includes the
        date, the weather type, max. degrees celcius and min. degrees celcius
        """
        return (f"{day['day']} will be {day['weather']}, with a maximum of {day['max_celcius']} degrees and a minimum of {day['min_celcius']} degrees.")

        # Add your print statement here

    # Your print function

    def average_temp(self, listofdays):
        """
        This function returns the average min and max temp of the following 5 days
        """
        sumofmax = 0
        sumofmin = 0
        # Add your Beautiful Soup code here to extract all the necessary data
        for day in listofdays:
            sumofmax += int(day[0]['max_celcius'].strip('°'))
            sumofmin += int((day[0]['min_celcius'].strip('°')))

        # Divide the sum of min degrees by the number of days
        avg_min_temp = sumofmin/len(listofdays)

        # Divide the sum of max degrees by the number of days
        avg_max_temp = sumofmax/len(listofdays)

        return avg_min_temp, avg_max_temp


def main():
    print("Welcome to the weather CLI. Let's start:")
    while True : 
        location = int(input(
            "Select location for weather data (pick a number) \n 1) Amsterdam \n 2) Groningen \n 3) Rotterdam \n Your answer:  "))

        # Match the given number with the corresponding city
        if location == 1:

            city = 'Amsterdam'
        elif location == 2:
            city = 'Groningen'
        elif location == 3:
            city = 'Rotterdam'


        try : 
            print(f"You have selected {city}")
        except (UnboundLocalError) :
            print('Invalid option')
            continue
        break

    number_of_days = int(input(
        "Select the max number of days (between 1 and 6) of which you want to get the weather data : "))
    print(f"You have selected: {number_of_days} day(s)")

    for city_name, city_id in cities:
        if city == city_name:
            city_id = city_id
            break
    print(city_id)

    # Initialization of the Weather class
    weather = Weather(city_id)

    # call the get_weather method on the weather variable that you just created

    weather_date = weather.get_weather(number_of_days)

    print("We have found the following data:")

    # Loop trough the get_weather data
    for day in weather_date:
        # Call your print method of the Weather class
        print(weather.print_weather(day[0]))

    # break

    # Print the average min and max temps
    print('min and max avg of temp are : ',  weather.average_temp(weather_date))


main()
