import time

class SystemMessage:
    def __init__(self, text):
        self.text = text
        self.created_at = time.time()
        self.acknowledged = False
        self.ack_time = None

    def acknowledge(self):
        self.acknowledged = True
        self.ack_time = time.time()

    @property
    def reaction_time(self):
        if self.ack_time:
            return self.ack_time - self.created_at
        return None
