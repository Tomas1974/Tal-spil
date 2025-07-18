import taipy.gui.builder as tgb
import random
from playsound import playsound
import pygame

SEJRS_ANTAL = 7
input_text = ""
display_text = ""
image = "billeder\\bird.jpg"
rigtig_forkert = ""
spil_tekst = ""
svar_knap = "Nyt spil"

start_forfra = True

data = {
"Navn": ["Tomas", "Sussi", "Signe", "Simon"],
"Score": [6, 5, 4, 3]

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
    global start_forfra

    state.svar_knap = "Svar"
    
    
    if counter == SEJRS_ANTAL or start_forfra:
           
           
           nyt_spil(state)

                       
    else:
        
        try:
            indtastet_værdi = int(state.input_text)
           

            if state.tal == indtastet_værdi:
                
                
                
                
                
                counter += 1
                state.rigtig_forkert = f"Rigtige: {counter}. Tal: {state.tal}"
                play_music("lyd\\correct.mp3")
                state.image = "billeder\\rigtig.gif"
                state.spil_tekst = f"Spørgsmål {counter}"
                state.tal = random.randint(1,100)
                print(state.tal)
                

                
            else:
                state.rigtig_forkert = f"Forkert {state.tal}"
                play_music("lyd\\forkert.mp3")
                state.image = "billeder\\forkert.gif"
                counter = 0
                
                state.svar_knap = "Nyt spil"
                start_forfra = True
        
    
                
                
            
            if counter == SEJRS_ANTAL:
                state.svar_knap = "Fortsæt"
                state.rigtig_forkert = f"Du har vundet"
                play_music("lyd\\finish.mp3")
                state.image = "billeder\\Finish.png"
                
                state.gennemløb += 1
        
        except ValueError:
            state.rigtig_forkert = f"Indtast et tal"


    state.input_text = ""




         
def nyt_spil(state):
    global counter
    global start_forfra

    state.spil_tekst = f"Spørgsmål 1"
    state.tal = random.randint(1,100)
    print(state.tal)
    state.rigtig_forkert = ""
    counter = 0 
    state.image = "billeder\\bird.jpg"

    if start_forfra:
        state.gennemløb = 0
        
    
    start_forfra = False
    





with tgb.Page() as page:
    tgb.text("# Mikkels tal spil", mode="md")
    
    with tgb.layout("10 40 40 10"):
    
        with tgb.layout("100"):
            pass

        with tgb.layout("100"):
            tgb.text("{spil_tekst}")
            with tgb.layout("30 10 20 40"):
                tgb.input(value = "{input_text}" )
                tgb.button("{svar_knap}", on_action=spil)
                tgb.button("Gentag lyd", on_action=spil)
                
            
            tgb.text(value="{rigtig_forkert}")
            tgb.image("{image}")  # Assumes bird.jpg is in the same directory    
        

        with tgb.layout("100"):
                with tgb.layout("30 10 20 40"):
                    tgb.button("Nulstil", on_action=spil)
                    tgb.text("Score: {gennemløb}")
                tgb.table("{data}")





 

def get_firstpage():
    return page
    

