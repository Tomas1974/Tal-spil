from abc import ABC, abstractmethod

import random

class SpilType(ABC):
        

    def __init__(self):
        
        self.sejrsantal_for_score = 4
        self.start_image: str = "billeder\\bird.jpg"
        self.sejr_billede: str = "billeder\\Finish.png"
        self.rigtig_billede: str =  "billeder\\rigtig.gif"
        self.forkert_billede: str = "billeder\\forkert.gif"
        self.er_et_tal: bool= False


    @abstractmethod
    def spørgsmåls_streng(self):
        pass




class SkrivTal(SpilType):

    def __init__(self):
        super().__init__()
        self.er_et_tal: bool= True

    def spørgsmåls_streng(self) -> list:
        return [random.randint(1, 100) for num in range(1, self.sejrsantal_for_score+1)]
    

    

    
