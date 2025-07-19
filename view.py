import taipy.gui.builder as tgb
import random
from utilities import play_music
from score import score_tabel, tjeck_score
import time

sejrsantal_for_scoring = 7
input_text = ""
display_text = ""
image = "billeder\\bird.jpg"
rigtig_forkert = ""
spil_tekst = ""
svar_knap = "Nyt spil"

start_forfra = True
aktiv_gentag_lyd=False



spørgsmålstal = 0
sejrs_antal = 0
score = 0

    

def spil(state):
    
           
    
    if sejrs_antal == sejrsantal_for_scoring+1 or start_forfra:
           nyt_spil(state)

                       
    else:
                

        try:
            indtastet_værdi = int(state.input_text)
                                   

            if state.spørgsmålstal == indtastet_værdi: #Rigtig besvarelse
                                
                rigtig_besvarelse(state)
                
                
            else:
                
                forkert_besvarelse(state)
                
        
                                    
            
            if sejrs_antal == sejrsantal_for_scoring + 1:
                sejr(state)
                                              
                                
                
        except ValueError:
            state.rigtig_forkert = f"Indtast et tal"


def rigtig_besvarelse(state):
    global sejrs_antal
      
    sejrs_antal += 1               
    spørgsmål_respons(state, "Rigtige", "billeder\\rigtig.gif")
    nyt_spørgsmål(state)


def forkert_besvarelse(state):

    global sejrs_antal
    global start_forfra #Hvis man svarer forkert eller lige startet
    
    
    sejrs_antal = 0   #Forkert besvarelse
    spørgsmål_respons(state, f"Forkert {state.spørgsmålstal}", "billeder\\forkert.gif")
                                                
    play_music("lyd\\forkert.mp3")
                
    state.score_tabel = tjeck_score(state.score)
    state.svar_knap = "Nyt spil"
    start_forfra = True
    state.aktiv_gentag_lyd=False


def sejr(state):
    
    state.score += 1
    spørgsmål_respons(state, f"Score {state.score}" , "billeder\\Finish.png")


    state.svar_knap = "Fortsæt"
    state.spil_tekst = "Runde gennemført"
    state.aktiv_gentag_lyd=False
    play_music("lyd\\finish.mp3")

         
def nyt_spil(state):
    global sejrs_antal
    global start_forfra

    
    sejrs_antal = 1 
    nyt_spørgsmål(state)
    spørgsmål_respons(state, "", "billeder\\bird.jpg")
    
    
    if start_forfra:
        state.score = 0
        start_forfra = False
        
    

def spørgsmål_respons(state, rigtig_forkert, image):
    state.rigtig_forkert = rigtig_forkert
    state.image = image


def nyt_spørgsmål(state):
    
    state.input_text = ""
    state.svar_knap = "Svar"
    state.spil_tekst = f"Spørgsmål {sejrs_antal}"
    state.spørgsmålstal = random.randint(1,100)
    play_music(f"lyd\\{state.spørgsmålstal}.mp3")
    state.aktiv_gentag_lyd=True



def gentag(state):
    play_music(f"lyd\\{state.spørgsmålstal}.mp3")


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
                tgb.button("Gentag lyd", on_action=gentag, active = "{aktiv_gentag_lyd}")
                
            
            tgb.text(value="{rigtig_forkert}")
            tgb.image("{image}")  # Assumes bird.jpg is in the same directory    
        

        with tgb.layout("100"):
                with tgb.layout("30 10 20 40"):
                    tgb.text("Score: {score}")
                tgb.table("{score_tabel}")





 

def get_firstpage():
    return page
    

