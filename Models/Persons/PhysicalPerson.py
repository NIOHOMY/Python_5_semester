from ..Client import Client
from ..Account import Account

class PhysicalPerson(Client):
    def __init__(self, name):
        super().__init__(name)
       