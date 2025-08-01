from taipy import Gui
from view import page

gui = Gui(page=page)

app = gui.run(dark_mode=True, run_server=True, use_reloader=False, return_flask_app=True)