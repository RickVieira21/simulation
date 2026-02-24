import random

from core.flight import Flight
from core.runway import Runway

class SimulationEngine:
    def __init__(self, cognitive_profile, complexity_profile):
        self.cognitive = cognitive_profile
        self.complexity = complexity_profile

        self.total_errors = 0
        self.constraint_errors = 0
        self.expiration_errors = 0

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

        # pista ocupada
        if not runway.available:
            #self.total_errors += 1
            return False

        # constraint violation
        if flight.required_runway is not None:
            if runway.name != flight.required_runway:
                self.constraint_errors += 1
                self.total_errors += 1
                return "CONSTRAINT_VIOLATION"

        duration = self.complexity.runway_occupation_time
        runway.occupy(flight, duration)
        flight.assigned_runway = runway.name

        return True



    def generate_flight(self):
        if len(self.flights) >= self.complexity.max_flights:
            return None

        # Exemplo  
        flight = Flight(
            callsign="TAP" + str(len(self.flights) + 100),
            eta=30,
            priority=self.complexity.has_priorities
        )

        if self.complexity.has_constraints:
            # probabilidade de ter constraint 
            if random.random() < 0.4:
                flight.required_runway = random.choice(self.runways).name
                
        self.flights.append(flight)

        return flight
