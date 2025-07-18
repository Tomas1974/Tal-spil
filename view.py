import taipy.gui.builder as tgb
import random
from utilities import play_music
from score import score_tabel, tjeck_score

SEJRS_ANTAL = 7
input_text = ""
display_text = ""
image = "billeder\\bird.jpg"
rigtig_forkert = ""
spil_tekst = ""
svar_knap = "Nyt spil"

start_forfra = True
gentag_activ=False



tal = 0
counter = 0
score = 0

    

def spil(state):
    
    global counter
    global start_forfra

    state.svar_knap = "Svar"
    
    
    if counter == SEJRS_ANTAL+1 or start_forfra:
           
           
           nyt_spil(state)

                       
    else:
        
        

        try:
            indtastet_værdi = int(state.input_text)
            state.gentag_activ=True

            
           

            if state.tal == indtastet_værdi:
                
                
                
                
                state.rigtig_forkert = "Rigtige"
                counter += 1
                                
                state.spil_tekst = f"Spørgsmål {counter}"
                state.image = "billeder\\rigtig.gif"
                
                state.tal = random.randint(1,100)
                play_music(f"lyd\\{state.tal}.mp3")
                

                
                

                
            else:
                state.rigtig_forkert = f"Forkert {state.tal}"
                play_music("lyd\\forkert.mp3")
                state.image = "billeder\\forkert.gif"
                counter = 0
                state.score_tabel = tjeck_score(state.score)
                state.svar_knap = "Nyt spil"
                start_forfra = True
                state.gentag_activ=False
        
    
                
                
            
            if counter == SEJRS_ANTAL+1:
                state.svar_knap = "Fortsæt"
                state.spil_tekst = "Runde gennemført"
                state.gentag_activ=False
                
                play_music("lyd\\finish.mp3")
                state.image = "billeder\\Finish.png"
                
                state.score += 1
                state.rigtig_forkert = f"Score {state.score}"
        
        except ValueError:
            state.rigtig_forkert = f"Indtast et tal"


    state.input_text = ""




         
def nyt_spil(state):
    global counter
    global start_forfra

    state.spil_tekst = f"Spørgsmål 1"
    state.tal = random.randint(1,100)
    state.gentag_activ=True
    play_music(f"lyd\\{state.tal}.mp3")
    print(state.tal)
    state.rigtig_forkert = ""
    counter = 1 
    state.image = "billeder\\bird.jpg"

    if start_forfra:
        state.score = 0
        
    
    start_forfra = False
    

def gentag(state):
    play_music(f"lyd\\{state.tal}.mp3")


with tgb.Page() as page:
    tgb.text("# Mikkels tal spil", mode="md")
    
    with tgb.layout("10 40 40 10"):
    
        with tgb.layout("100"):
            pass

        with tgb.layout("100"):
            tgb.text("{spil_tekst}")
            with tgb.layout("30 10 20 40"):
                tgb.input("{input_text}", on_action=spil, action_keys=["ENTER"] )
                tgb.button("{svar_knap}", on_action=spil)
                tgb.button("Gentag lyd", on_action=gentag, active = "{gentag_activ}")
                
            
            tgb.text(value="{rigtig_forkert}")
            tgb.image("{image}")  # Assumes bird.jpg is in the same directory    
        

        with tgb.layout("100"):
                with tgb.layout("30 10 20 40"):
                    #tgb.button("Nulstil", on_action=spil)
                    tgb.text("Score: {score}")
                tgb.table("{score_tabel}")





 

def get_firstpage():
    return page
    

