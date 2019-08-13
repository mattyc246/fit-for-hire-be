from app import app, socketio
import fitforhire_api
import fitforhire_web

socketio.run(app, host="0.0.0.0")
