def calculate_health(data):
    battery = float(data.get("battery", 0))
    fuel = float(data.get("fuel", 0))
    signal = float(data.get("signal", 0))

    health = (
        battery * 0.3 +
        fuel * 0.3 +
        signal * 0.2 +
        20
    )

    return round(health, 2)