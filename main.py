from taipy import Gui 
from view import page
import random
    


if __name__ == "__main__":
    Gui(page=page).run(dark_mode=True, use_reloader=True)
