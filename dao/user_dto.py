# Classe utilizzata come DTO, per "mappare" una riga della tabella User
from dataclasses import dataclass

@dataclass
class UserDTO:
    id : int
    name : str
    phone : str

    def __str__(self):
        return str(self.id)+" "+self.name+" "+self.phone

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.id < other.id

    def __hash__(self):
        return hash(self.id)