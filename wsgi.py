# to run gunicorn: 
# export FLASK_APP=app.py
# gunicorn --bind 0.0.0.0:<your-desired-port-here> wsgi:app -D

from app import app

if __name__ == "__main__":
    app.run()
