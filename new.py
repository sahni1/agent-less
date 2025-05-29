import tkinter as tk
import requests

def get_weather():
    city = entry_city.get()
    api_key = "your_openweathermap_api_key"  # Replace with your API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        if data.get("cod") != 200:
            result_var.set(f"Error: {data.get('message', 'City not found')}")
            return
        
        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        
        result_var.set(f"City: {city_name}, {country}\n"
                       f"Temperature: {temp}°C\n"
                       f"Weather: {weather.capitalize()}\n"
                       f"Humidity: {humidity}%\n"
                       f"Wind Speed: {wind_speed} m/s")
    except Exception as e:
        result_var.set("Error fetching weather data!")

root = tk.Tk()
root.title("Weather Forecast")
root.geometry("400x300")

tk.Label(root, text="Enter City Name:", font="Arial 12").pack(pady=10)
entry_city = tk.Entry(root, font="Arial 12", width=25)
entry_city.pack()

tk.Button(root, text="Get Weather", font="Arial 12", command=get_weather).pack(pady=10)

result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, font="Arial 12", wraplength=350, justify="left").pack(pady=20)

root.mainloop()
