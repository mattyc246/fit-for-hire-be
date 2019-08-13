from app import app, socketio
import fitforhire_api
import fitforhire_web

if __name__ == '__main__':
    socketio.run(app)
