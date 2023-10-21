from ..Client import Client
from ..Account import Account

class LegalPerson(Client):
    def __init__(self, name):
        #account = Account()
        super().__init__(name)
       