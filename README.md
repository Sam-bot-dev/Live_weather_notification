# 🌡️ Weather Notification App (Windows 10 Toast)

A simple Python script that fetches the current temperature of your chosen city using the OpenWeatherMap API and displays it as a desktop notification using Windows 10 toast alerts.

## 🔧 Technologies Used

- **`requests`** – To fetch weather data from the OpenWeatherMap API.
- **`bs4` (BeautifulSoup)** – Included for future HTML parsing (not required for current script but imported).
- **`win10toast`** – To display toast notifications on Windows desktop.

> ⚠️ **Note:** `win10toast` does **not work on Replit** or non-Windows systems. Use a Windows PC to see the notifications.

---

## 📦 Installation

1. Clone the repository or download the script.
2. Install the required Python packages:

```bash
pip install requests bs4 win10toast
