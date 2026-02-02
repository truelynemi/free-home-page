# app.py
from flask import (Flask, render_template, request, redirect, url_for, flash, session)

# -------------------------------------------------
# APP CONFIGURATION
# -------------------------------------------------
app = Flask(__name__)

# Path to SQLite database file (created automatically if it doesn't exist)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rza.db'

# Turn off a noisy feature we don't need
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Secret key is used for flashes + sessions (keep this private in real life)
app.config['SECRET_KEY'] = 'a_long_bankai_key_i_suppose'


# -------------------------------------------------
# ROUTES FOR STATIC PAGES
# -------------------------------------------------

@app.route('/')
def index():
    return render_template('index.html')

# -------------------------------------------------
# RUN APP
# -------------------------------------------------
if __name__ == "__main__":
    # debug=True reloads the app when you change the code (useful during development)
    app.run(debug=True)