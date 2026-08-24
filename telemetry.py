import random

def generate_telemetry():

    battery = random.randint(50, 100)
    temperature = random.randint(20, 70)
    fuel = random.randint(40, 100)
    signal = random.randint(50, 100)

    return {
        "battery": battery,
        "temperature": temperature,
        "fuel": fuel,
        "signal": signal
    }


data = generate_telemetry()

print(data)
