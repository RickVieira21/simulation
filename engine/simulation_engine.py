from core.flight import Flight
from core.runway import Runway

class SimulationEngine:
    def __init__(self, cognitive_profile, complexity_profile):
        self.cognitive = cognitive_profile
        self.complexity = complexity_profile

        self.flights = []
        self.runways = [
            Runway("A"),
            Runway("B"),
            Runway("C")
        ]

    
    def get_runway(self, name):
        for runway in self.runways:
            if runway.name == name:
                return runway
        return None
    

    def assign_flight_to_runway(self, flight, runway):
        if not runway.available:
            return False

        # duração dependente da complexidade?
        duration = self.complexity.runway_occupation_time

        runway.occupy(flight, duration)
        flight.assigned_runway = runway.name

        return True



    def generate_flight(self):
        if len(self.flights) >= self.complexity.max_flights:
            return None

        # Exemplo simples 
        flight = Flight(
            callsign="TAP" + str(len(self.flights) + 100),
            eta=30,
            priority=self.complexity.has_priorities
        )
        self.flights.append(flight)
        return flight
