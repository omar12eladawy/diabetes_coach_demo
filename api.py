from flask import Flask, render_template
import os
import firebase_admin
from firebase_admin import credentials


app = Flask(__name__, template_folder='')


cred = credentials.Certificate("Key.json")
firebase_admin.initialize_app(cred)


@app.route('/')
def hello():
    return render_template('home.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', debug=False, port=port)
