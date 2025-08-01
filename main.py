from taipy import Gui
from view import page

gui = Gui(page=page)

# This is what Heroku will call when using a WSGI server like gunicorn
app = gui.run(dark_mode=True, run_server=True, use_reloader=False, return_flask_app=True)