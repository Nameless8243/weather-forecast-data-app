import requests

API_KEY = "66707d219a57fae3c5f37344830ef210"


def get_data(city, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]

    return filtered_data


if __name__ == "__main__":
    print(get_data(city="Budapest", forecast_days=3))
