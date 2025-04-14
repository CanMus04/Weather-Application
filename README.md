# 🌦️ Weather App using OpenWeatherMap API

A beginner-friendly command-line weather application written in Python.  
It fetches and displays real-time weather data for any city using the OpenWeatherMap API.

---

## 🧠 About the Project

This project seemed simple at first — just grab some weather data and print it out. But things got complicated quickly once I started dealing with APIs, error handling, and JSON structures.

To be completely honest: I followed a tutorial and adapted much of the code. I didn't come up with the logic on my own, but I did learn how API requests work, how to parse JSON in Python, and how to handle different edge cases.

What challenged me the most was making sure the app responds clearly to user input errors (like entering a wrong city) and still keeps running.

---

## ✨ Features

- 🔎 Check current weather for any city  
- 🌡️ Shows temperature, "feels like", condition, and humidity  
- ⚠️ Gracefully handles invalid city names or connection issues  
- 🧼 Clean command-line interface  
- 🌍 English weather descriptions (`lang="en"`)

---

## 🛠️ How It Works

1. The user is prompted to enter a city name  
2. The program sends a request to OpenWeatherMap's API  
3. Weather data is parsed from JSON  
4. The relevant details are displayed in a readable format  
5. If something goes wrong, a helpful error message is shown  

---

## ▶️ Live Demo

> No live version available — run it locally via terminal as shown below.

---

## 🧰 Technologies Used

- Python 3  
- [`requests`](https://pypi.org/project/requests/) library  
- [OpenWeatherMap API](https://openweathermap.org/api)

---

## 📦 Installation & Usage

### 🔑 Get Your API Key

1. Register for free at [OpenWeatherMap](https://openweathermap.org/)  
2. Copy your API key  
3. Paste it into the script (`API_KEY = "your_api_key_here"`)

---

### 💻 Run the Program

```bash
# Clone the repo
git clone https://github.com/CanMus04/weather-application.git

# Go into the project directory
cd weather-application

# Run the Python script
python weather_application.py
