def estimate_footprint(mode: str, distance_km: float) -> float:
    emissions = {
        "car": 0.18,         # kg CO₂/km
        "train": 0.04,
        "bike": 0.0,
        "bus": 0.09
    }
    return emissions.get(mode, 0.18) * distance_km
