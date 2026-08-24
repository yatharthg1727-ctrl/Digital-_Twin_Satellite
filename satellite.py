class Satellite:

    def _init_(self, name):
        self.name = name
        self.battery = 100
        self.temperature = 25
        self.fuel = 100
        self.signal = 100


        def show_status(self):

            print("\nSatellite Status ")
            print("--------------")
            print("Name:", self.name)
            print("Battery:",self.battery)
            print("Temperature:",self.temperature)
            print("Fuel:", self.fuel)
            print("Signal:", self.signal)


            sat = Satellite("INSAT-X")

            sat.show_status()  