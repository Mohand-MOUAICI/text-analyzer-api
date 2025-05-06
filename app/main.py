from fastapi import FastAPI, Query
from pydantic import BaseModel
import spacy
from app.carbon_utils import estimate_footprint

app = FastAPI()
nlp = spacy.load("en_core_web_sm")

class TextRequest(BaseModel):
    text: str

@app.get("/route")
def get_route(from_city: str = Query(...), to_city: str = Query(...), mode: str = Query("car")):
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

@app.post("/summarize")
def summarize(request: TextRequest):
    # Exemple simplifié
    sentences = request.text.split('.')
    summary = sentences[0] if sentences else ""
    return {"summary": summary.strip()}

@app.post("/sentiment")
def sentiment(request: TextRequest):
    # Simulation sentiment simple
    if "love" in request.text.lower():
        return {"sentiment": "positive"}
    return {"sentiment": "neutral"}

@app.post("/entities")
def entities(request: TextRequest):
    doc = nlp(request.text)
    ents = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    return {"entities": ents}
