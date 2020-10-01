from abc import ABC, abstractmethod
class Clothes(ABC):

    @abstractmethod
    def __init__(self, name):
        self.name = name

class Coat(Clothes):
    
    def __init__(self, name, V):        
        self.name = name
        self.V = float(V)

    @property
    def print_cloth(self):
        return f'Название: {self.name}; \nРасход ткани: {round(self.V/6.5 + 0.5, 2)}.'

class Suit(Clothes):
    
    def __init__(self, name, H):
        self.name = name
        self.H = float(H)
    
    @property
    def print_cloth(self):
        return f'Название: {self.name}; \nРасход ткани: {round(2*self.H + 0.3, 2)}.'


suit = Suit("suit_1", 4)
print(suit.print_cloth)
coat = Coat("coat_1", 5)
print(coat.print_cloth)