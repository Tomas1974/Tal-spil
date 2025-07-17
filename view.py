import taipy.gui.builder as tgb
import random
from playsound import playsound
import pygame

SEJRS_ANTAL = 7
input_text = ""
display_text = ""
image = "billeder\\bird.jpg"
rigtig_forkert = ""

data = {
"name": ["Tomas", "Sussi", "Signe", "Simon"],
"score": [6, 5, 4, 3]

}

tal = 0
counter = 0
gennemløb = 0


def play_music(mp3File):
    pygame.mixer.init()
    pygame.mixer.music.load(mp3File)
    pygame.mixer.music.play()

def spil(state):
    
    global counter
    
    if counter == SEJRS_ANTAL:
           nyt_spil(state)
                       
    else:
        
        if int(state.tal) == int(state.input_text):
            
            
            state.tal = random.randint(1,100)
            print(state.tal)
            
            counter += 1
            state.rigtig_forkert = f"Rigtigt {counter}"
            play_music("lyd\\correct.mp3")
            state.image = "billeder\\rigtig.gif"
            

            
        else:
            state.rigtig_forkert = f"Forkert"
            play_music("lyd\\forkert.mp3")
            state.image = "billeder\\forkert.gif"
            counter = 0
            state.gennemløb = 0
            
            
        
        if counter == SEJRS_ANTAL:
            state.rigtig_forkert = f"Du har vundet"
            play_music("lyd\\finish.mp3")
            state.image = "billeder\\Finish.png"
            
            state.gennemløb += 1
            

    state.input_text = ""




         
def nyt_spil(state):
    global counter

    state.tal = random.randint(1,100)
    print(state.tal)
    state.rigtig_forkert = ""
    counter = 0 
    state.gennemløb = 0
    state.image = "billeder\\bird.jpg"





with tgb.Page() as page:
    tgb.text("# Mikkels tal spil", mode="md")
    
    with tgb.layout("10 40 40 10"):
    
        with tgb.layout("100"):
            pass

        with tgb.layout("100"):
            with tgb.layout("30 10 20 40"):
                tgb.input(value = "{input_text}" )
                tgb.button("Svar", on_action=spil)
                tgb.button("Gentag lyd", on_action=spil)
                tgb.button("Nyt spil", on_action=nyt_spil)
            
            tgb.text(value="{rigtig_forkert}")
            tgb.image("{image}")  # Assumes bird.jpg is in the same directory    
        

        with tgb.layout("100"):
                with tgb.layout("30 10 20 40"):
                    tgb.button("Nulstil", on_action=spil)
                    tgb.text("{gennemløb}")
                tgb.table("{data}")





 

def get_firstpage():
    return page
    

