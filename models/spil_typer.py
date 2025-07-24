from abc import ABC

class SpilType(ABC):
    sejrsantal_for_score = 4

    def __init__(self, spørgsmåls_liste):
        
        
        self.start_image = "billeder\\bird.jpg"
        self.sejr_billede = "billeder\\Finish.png"
        self.rigtig_billede =  "billeder\\rigtig.gif"
        self.forkert_billede = "billeder\\forkert.gif"
        self.spørgsmåls_liste = spørgsmåls_liste
        


class SkrivTal(SpilType):

    def __init__(self, spørgsmåls_liste):
        super().__init__(spørgsmåls_liste)

    

    
