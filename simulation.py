import time
from telemetry import generate_telemetry
from save_data import save_data

while True:

    data = generate_telemetry()

    save_data(data)

    print(data)

    time.sleep(5)