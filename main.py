import requests
from rich import print
from rich.markdown import Markdown

def welcome():
    """Welcome message"""
    print("Welcome to the AI Bikepacking Itinerary Planner! Your virtual biker companion")

    welcome()
#Create a function to display current weather. Weather Function.
def display_current_weather(location):
    """ Get current weather condition for starting point and ending point """
    api_key = "290724cd93ad94b31t54c30cca2o800f"
    api_url = f"https://api.shecodes.io/weather/v1/current?query={location}&key={api_key}"

    response = requests.get(api_url)
    response_data = response.json()
    temperature = round(response_data['temperature']['current'])
    condition = response_data['condition']['description']
    windspeed = response_data['wind']['speed']

    print(f"\nThe current temperature in [bold]{location}[/bold] is [bold]{temperature}[/bold]°C, [bold]{condition}[/bold].\n")
    print(f"\nThe windspeed in [bold]{location}[/bold] is {windspeed} km/hr.")


#Create a function to generate itinerary. Itinerary Function.
def generate_itinerary(origin, destination, duration):
    """ Generate a travel itinerary using AI and direct links to resources """

    print (f"Generating itinerary from {origin} to {destination}...")

    api_key = "290724cd93ad94b31t54c30cca2o800f"
    prompt = f"Generate the itinerary from {origin} to {destination} in {duration} days by bike. Add a backpacking referece blog. Add emojis to make it more readable. Add approximate time per kilometer biking."
    context = "You are a travel agency specialized in bikepacking experiences."
    api_url = f"https://api.shecodes.io/ai/v1/generate?prompt={prompt}&context={context}&key={api_key}"

    #call api
    response = requests.get(api_url)
    response_data = response.json()
    itinerary = Markdown(response_data['answer'])

    print(itinerary)



#Get user input
origin = input("Where are you starting from? ").strip().capitalize()
destination = input("What's your final destination? ").strip().capitalize()
duration = input("How many days will you travel bikepacking? (enter numbers only i.e.: 4) ")

def credit():
    """Credit"""
    print("The AI Backpacking Itinerary was built by Leticia Gmx 🇲🇽")
#Call SheCodes AI API
#Display itinerary
if origin and destination and duration.isdigit():
    display_current_weather(origin)
    display_current_weather(destination)
    generate_itinerary(origin, destination, duration)
else:
    print ("Something went wrong. Try again.")
#Call Weather API
#Display origin and destination
