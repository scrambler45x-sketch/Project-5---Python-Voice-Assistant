import webbrowser

def get_weather(city):
    city = city.strip()

    if city:
        url = f"https://www.google.com/search?q=weather+{city}"
        webbrowser.open(url)
        return f"Showing weather for {city}."

    return "Please tell me a city name."