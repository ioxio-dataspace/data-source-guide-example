from fastapi import FastAPI, Request
import random

app = FastAPI()


@app.post("/Meteorology/Weather_v0.1")
async def get_weather(request: Request):
    # Parse the JSON request body manually
    body = await request.json()

    # Extract lat, lon, and when (if provided)
    lat = body.get("lat")
    lon = body.get("lon")

    if lat is None or lon is None:
        return {"detail": "lat and lon are required."}

    # Generate random weather data
    weather_response = {
        "temperature": round(random.uniform(-20, 35), 1),
        "humidity": round(random.uniform(10, 90)),
        "pressure": round(random.uniform(980, 1050)),
        "windSpeed": round(random.uniform(0, 15), 1),
        "windDirection": round(random.uniform(0, 360)),
        "precipitation": round(random.uniform(0, 10), 1),
        "visibility": round(random.uniform(0, 50000)),
    }

    return weather_response
