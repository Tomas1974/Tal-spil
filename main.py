from taipy import Gui
from view import page, Audio, create_audio




gui = Gui(page)
gui.register_content_provider(Audio, create_audio)
app = gui.run(dark_mode=True, run_server=True)