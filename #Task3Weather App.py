import requests
import tkinter as tk
from tkinter import messagebox

def get_weather():
    city = city_entry.get()
    api_key = "052cc77a1fa05f46b13ba9aefc615bd6"
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")

    if weather_data.json()["cod"] == "404":
        messagebox.showerror("Error", "No city found")
    else:
        weather = weather_data.json()["weather"][0]["main"]
        temp_fahrenheit = weather_data.json()["main"]["temp"]
        temp_celsius = (temp_fahrenheit - 32) * 5 / 9
        result_text.set(f"The weather in {city} is {weather}.\nThe temperature is {temp_celsius:.2f} Celsius.")


window = tk.Tk()
window.title("Weather App")
window.geometry("300x200")
tk.Label(window, text="Enter city:").pack(pady=10)
city_entry = tk.Entry(window)
city_entry.pack(pady=10)
tk.Button(window, text="Get Weather", command=get_weather).pack(pady=10)
result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text)
result_label.pack(pady=10)
window.mainloop()
