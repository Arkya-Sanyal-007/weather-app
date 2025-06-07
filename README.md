# 🌦 Tkinter Weather App

A simple and elegant desktop weather application built using **Python**, **Tkinter**, and the **OpenWeatherMap API**. Enter a city name to fetch real-time weather data including temperature, condition, humidity, wind speed, and an icon.

---

## 🚀 Features

- 🌍 Fetches live weather data using OpenWeatherMap API  
- 🌤 Displays current temperature, weather conditions, and wind/humidity  
- 🌗 Detects Day or Night using weather icon code  
- 🖼️ Displays weather icons visually  
- 🎨 Clean and responsive GUI built with `Tkinter`  
- ❗ Includes proper error handling for invalid input or API failures  

---

## 🛠 Requirements

Install required libraries using pip:

```bash
pip install requests pillow
````

---

## 🧾 How to Run

1. Clone or download the repo.
2. Replace the placeholder API key with your own in the code:

   ```python
   API_KEY = "your_api_key_here"
   ```

   Get one from [OpenWeatherMap](https://openweathermap.org/api).
3. Run the script:

   ```bash
   python weather_app.py
   ```

---

## 💡 GUI Overview

* **Input Field**: Enter the name of the city.
* **Get Weather** button: Triggers data fetch and updates the screen.
* **Weather Info**: Displays city name, temperature, weather condition, humidity, and wind speed.
* **Day/Night Detection**: Based on the weather icon.
* **Icon**: Weather condition icon fetched and displayed dynamically.

---

## 🖼 Sample Output

```
![{DD4FC0EB-D8CF-431C-92F2-FEE6F499A890}](https://github.com/user-attachments/assets/edd74eaa-5cc5-4c3a-a149-3cb142706d29)

```

An icon matching the condition (like sun, clouds, etc.) will also be shown.

---

## 📁 File Structure

```
weather_app.py      # Main app file
README.md           # You're reading it
```

---

## 🧪 Error Handling

* ⚠️ Shows alert if no city is entered
* ❌ Displays error if city not found or request fails
* 🌐 Catches API/network issues and displays a readable message

---

## 📊 Future Ideas

* [ ] Add 5-day forecast
* [ ] Save user preferences (last searched city)
* [ ] Switch between metric/imperial units
* [ ] Add dark/light mode toggle

---

## 📜 License

MIT License — free to use, modify, and share.

---

## 🙌 Credits

* [OpenWeatherMap](https://openweathermap.org/) for the weather API
* [Pillow](https://python-pillow.org/) for image processing
* Python's built-in `tkinter` and `requests`

---

### 🧠 Tip

Make sure your system supports GUI apps and Tkinter is installed. This app **won’t work in headless environments** (like most remote servers without a desktop environment).

```
---
