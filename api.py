from flask import Flask, render_template, send_from_directory
import os
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("Key.json")
firebase_admin.initialize_app(cred)

app = Flask(__name__,
            static_url_path='',
            static_folder='web/static',
            template_folder='web/templates')


@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', debug=False, port=port)
