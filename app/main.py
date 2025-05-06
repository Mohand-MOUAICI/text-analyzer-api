from fastapi import FastAPI, Query
from app.carbon_utils import estimate_footprint

app = FastAPI()

@app.get("/route")
def get_route(from_city: str = Query(...), to_city: str = Query(...), mode: str = Query("car")):
    # Simulation des données pour l'exemple
    distances = {
        ("Paris", "Lyon"): 465,
        ("Paris", "Marseille"): 775
    }
    distance = distances.get((from_city, to_city), 100)

    footprint = estimate_footprint(mode, distance)

    advice = "Consider taking a train for lower emissions." if mode == "car" else "Good choice!"

    return {
        "distance_km": distance,
        "carbon_footprint_kg": round(footprint, 2),
        "advice": advice
    }
