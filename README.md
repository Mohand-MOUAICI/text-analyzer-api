# Green Route Advisor 🌱

Une API Python FastAPI qui estime l’empreinte carbone d’un trajet entre deux villes selon le mode de transport.

## Endpoints

### `GET /route?from=Paris&to=Lyon&mode=car`

Réponse :
```json
{
  "distance_km": 465,
  "carbon_footprint_kg": 83.7,
  "advice": "Consider taking a train for lower emissions."
}
