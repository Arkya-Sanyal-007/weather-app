import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO

# ✅ Replace with your actual API key
API_KEY = "your_api_key_here"

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Required", "Please enter a city name.")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            city_name = data['name']
            country = data['sys']['country']
            temp = data['main']['temp']
            condition = data['weather'][0]['main']
            description = data['weather'][0]['description']
            humidity = data['main']['humidity']
            wind = data['wind']['speed']
            icon_code = data['weather'][0]['icon']
            
            # 🔍 Detect Day or Night
            time_of_day = "Day" if icon_code.endswith("d") else "Night"
            day_night_label.config(text=f"{condition} - {time_of_day}")

            # 📝 Display weather info
            result = (
                f"{city_name}, {country}\n"
                f"🌡 Temperature: {temp}°C\n"
                f"🌤 {condition} ({description})\n"
                f"💧 Humidity: {humidity}%\n"
                f"💨 Wind: {wind} m/s"
            )
            result_label.config(text=result)

            # 🌐 Fetch and display weather icon
            icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
            icon_response = requests.get(icon_url)
            img_data = icon_response.content
            img = Image.open(BytesIO(img_data))
            img = img.resize((75, 75))
            icon_img = ImageTk.PhotoImage(img)
            icon_label.config(image=icon_img)
            icon_label.image = icon_img

        else:
            result_label.config(text=f"❌ Error: {data.get('message', 'City not found')}")
            icon_label.config(image='')
            day_night_label.config(text='')

    except Exception as e:
        result_label.config(text=f"❌ Error: {e}")
        icon_label.config(image='')
        day_night_label.config(text='')

# 🎨 GUI Setup
fixed_color = "#fbfbfb"
root = tk.Tk()
root.title("🌦 Weather App")
root.geometry("400x430")
root.resizable(False, False)
root.configure(bg=fixed_color)

tk.Label(root, text="Enter City Name:", font=("Arial", 12), bg=fixed_color).pack(pady=10)
city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather).pack(pady=10)

icon_label = tk.Label(root, bg="#0f9de4")
icon_label.pack()

# ➕ Day/Night Label below icon
day_night_label = tk.Label(root, text="", font=("Arial", 12), bg=fixed_color)
day_night_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 12), justify="center", bg=fixed_color)
result_label.pack(pady=10)

root.mainloop()
