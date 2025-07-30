    
from taipy import Gui 
from view import page

    

flask_app = Gui(page=page).run(dark_mode=True, run_server=False).get_flask_app()
