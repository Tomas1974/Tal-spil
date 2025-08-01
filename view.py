import taipy.gui.builder as tgb

from utilities import play_music
from score import score_tabel, tjeck_score
from models.spil_typer import SkrivTal
from collections.abc import Iterable



spil_type = SkrivTal()

sejrsantal_for_score: int = spil_type.sejrsantal_for_score
image: str = spil_type.start_image

input_text: str = ""
display_text: str = ""

rigtig_forkert: str = ""
spil_tekst: str = ""
svar_knap: str = "Nyt spil"

start_forfra: bool = True
aktiv_gentag_lyd: bool=False


spørgsmålsværdi: Iterable = []

sejrs_antal: int = 0
score: int = 0

    

def spil(state):
    
    
    if state.sejrs_antal == sejrsantal_for_score+1 or state.start_forfra:
           nyt_spil(state)
                       

    else:
        
                
                
        if spil_type.er_et_tal:
            try: 
                indtastet_værdi = int(state.input_text)
            except:
                state.rigtig_forkert = f"Indtast et tal"

        
        state.input_text = ""
                    
        if state.spørgsmålsværdi[state.sejrs_antal-1] == indtastet_værdi: #Rigtig besvarelse
            rigtig_besvarelse(state)
                    
        else:
            forkert_besvarelse(state)
        
        
             



def rigtig_besvarelse(state):
      
    state.sejrs_antal += 1

    if state.sejrs_antal == sejrsantal_for_score+1:
                sejr(state)
    else:               
        spørgsmål_respons(state, "Rigtige", spil_type.rigtig_billede)
        nyt_spørgsmål(state)


def forkert_besvarelse(state):


    state.sejrs_antal = 0   #Forkert besvarelse
    spørgsmål_respons(state, f"Forkert {state.spørgsmålsværdi[state.sejrs_antal-1]}", spil_type.forkert_billede)
                                                
    #play_music("static/lyd/forkert.mp3")
                
    state.score_tabel = tjeck_score(state.score)
    state.score = 0
    state.svar_knap = "Nyt spil"
    state.start_forfra = True
    state.aktiv_gentag_lyd=False


def sejr(state):
    
    state.score += 1
    spørgsmål_respons(state, f"Score {state.score}" , spil_type.sejr_billede)


    state.svar_knap = "Fortsæt"
    state.spil_tekst = "Runde gennemført"
    state.aktiv_gentag_lyd=False
    #play_music("static/lyd/finish.mp3")

         
def nyt_spil(state):
    
    state.sejrs_antal=1
    
    if state.score % 2==0:
        state.spørgsmålsværdi = [] 
        state.spørgsmålsværdi = spil_type.spørgsmåls_streng()
        
    nyt_spørgsmål(state)
    spørgsmål_respons(state, "", spil_type.start_image)
    
    
    if state.start_forfra:
        state.start_forfra = False
        
    

def spørgsmål_respons(state, rigtig_forkert, image):
    state.rigtig_forkert = rigtig_forkert
    #state.image = image


def nyt_spørgsmål(state):
    
    state.svar_knap = "Svar"
    if state.score % 2==0:
         state.spil_tekst = f"Spørgsmål {state.sejrs_antal}:  {state.spørgsmålsværdi[state.sejrs_antal-1]}"
    else:

        letters = len(str(state.spørgsmålsværdi[state.sejrs_antal-1]))
        state.spil_tekst = f"Spørgsmål {state.sejrs_antal}: { "*" * letters}"
        
    #play_music(f"static/lyd/{state.spørgsmålsværdi[state.sejrs_antal-1]}.mp3")
    state.aktiv_gentag_lyd=True



def gentag(state):
    #play_music(f"static/lyd/{state.spørgsmålsværdi[state.sejrs_antal-1]}.mp3")
    pass


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
            tgb.image("{image}")  
        

        with tgb.layout("100"):
                with tgb.layout("30 10 20 40"):
                    tgb.text("Score: {score}")
                tgb.table("{score_tabel}")





 

def get_firstpage():
    return page
    

