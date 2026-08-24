from health_score import calculate_health
from backend.main import app as backend_app

sample_data = {
    "battery": 85,
    "fuel": 70,
    "signal": 90,
}

score = calculate_health(sample_data)
print("\nHealth Score:", score)

app = backend_app