import random
from engine.system_message import SystemMessage  

class SystemMessageManager:
    def __init__(self, engine):
        self.engine = engine

    def should_send_message(self):
        r = random.random()
        print(r)
        return r < self.engine.cognitive.message_frequency

    def generate_message(self):
        messages = self.engine.cognitive.messages
        text = random.choice(messages)
        return SystemMessage(text)

