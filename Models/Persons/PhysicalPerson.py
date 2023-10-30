from ..Client import Client

class PhysicalPerson(Client):
    def __init__(self, name):
        super().__init__(name)
       