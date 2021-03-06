from kano.webapp import WebApp

class Draw(WebApp):
    def __init__(self):
        super(Draw, self).__init__()

        self._index = "http://localhost:8000"
        self._title = "Draw"
        self._app_icon = '/usr/share/icons/Kano/88x88/apps/kano-draw.png'

        self._decoration = False
        self._maximized = True

        # Enable developer extras to allow error reporting to work
        self._inspector = True
