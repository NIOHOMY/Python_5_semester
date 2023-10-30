from ..Client import Client
from ..Account import Account

class LegalPerson(Client):
    def __init__(self, name):
        super().__init__(name)
       