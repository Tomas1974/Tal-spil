import taipy.gui.builder as tgb
import random
from playsound import playsound

input_text = ""
display_text = ""
image = "bird.jpg"
rigtig_forkert = ""

data = {
"name": ["Tomas", "Sussi", "Signe", "Simon"],
"score": [6, 5, 4, 3]

}

tal = random.randint(1,100)
print(tal)
counter = 0
gennemløb = 0


def spil(state):
    
    global counter
    
    if counter == 7:
           counter = 0
            
    
    
    if int(state.tal) == int(state.input_text):
        
        
        state.tal = random.randint(1,100)
        print(state.tal)
        
        counter += 1
        state.rigtig_forkert = f"Rigtigt {counter}"
        playsound('path/to/your/soundfile.mp3')
        
        
    else:
        state.rigtig_forkert = f"Forkert"
        counter = 0

    
    if counter == 7:
        state.rigtig_forkert = f"Du har vundet"
        state.gennemløb += 1
        counter = 0




         
def nyt_spil(state):
    global counter

    state.tal = random.randint(1,100)
    print(state.tal)
    state.rigtig_forkert = ""
    counter = 0 




with tgb.Page() as page:
    tgb.text("# Mikkels tal spil", mode="md")
    
    with tgb.layout("10 40 40 10"):
    
        with tgb.layout("100"):
            pass

        with tgb.layout("100"):
            with tgb.layout("30 10 20 40"):
                tgb.input(value = "{input_text}" )
                tgb.button("Spil", on_action=spil)
                tgb.button("Gentag", on_action=spil)
                tgb.button("Nyt spil", on_action=nyt_spil)
            
            tgb.text(value="{rigtig_forkert}")
            tgb.image("{image}")  
        

        with tgb.layout("100"):
                with tgb.layout("30 10 20 40"):
                    tgb.button("Nulstil", on_action=spil)
                    tgb.text("{gennemløb}")
                tgb.table("{data}")





 

def get_firstpage():
    return page
    

