class Runway:
    def __init__(self, name):
        self.name = name
        self.available = True
        self.current_flight = None
        self.remaining_time = 0

    def occupy(self, flight, duration):
        self.available = False
        self.current_flight = flight
        self.remaining_time = duration

    def tick(self):
        if not self.available:
            self.remaining_time -= 1
            if self.remaining_time <= 0:
                self.release()

    def release(self):
        self.available = True
        self.current_flight = None
        self.remaining_time = 0
