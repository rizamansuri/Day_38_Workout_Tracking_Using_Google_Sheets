# Nutrition API - https://www.nutritionix.com/business/api
# Get API keys - https://developer.nutritionix.com/
# https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit
# Natural language for exercise - https://developer.syndigo.com/docs/natural-language-for-exercise
# Authenticate your request - https://sheety.co/docs/authentication.html
# Sheety API - https://sheety.co/
import os
import requests
from datetime import *

APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = "https://api.sheety.co/5a073229871404ae00d517ab515dc028/copyOfMyWorkouts/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

exercise_text = input("Tell me which exercise you did: ")
parameters = {
    "query": exercise_text,
    "gender": "female",
    "weight_kg": 47,
    "height_cm": 151,
    "age": 21
}

result = requests.post(EXERCISE_ENDPOINT, headers=headers, json=parameters).json()
# print(result)

# Bearer Token Authentication
bearer_headers = {"Authorization": "Bearer riza"}

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
for exercise in result['exercises']:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEET_ENDPOINT,json=sheet_inputs,headers=bearer_headers)
    print(sheet_response.text)
