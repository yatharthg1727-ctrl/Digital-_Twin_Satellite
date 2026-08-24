class DigitalTwin:

    def __init__(self):
        self.battery = 0
        self.temperature = 0
        self.fuel = 0
        self.signal = 0

    def update(self, data):

        self.battery = data["battery"]
        self.temperature = data["temperature"]
        self.fuel = data["fuel"]
        self.signal = data["signal"]

    def display(self):

        print("\nDigital Twin")
        print("------------")
        print("Battery:", self.battery)
        print("Temperature:", self.temperature)
        print("Fuel:", self.fuel)
        print("Signal:", self.signal)