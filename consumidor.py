from observer import Observer

class Consumidor(Observer):
    def __init__(self):
        super().__init__()

    def update(self, message):
        print(message)