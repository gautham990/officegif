import os
import socket
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    hostname = socket.gethostname()
    message = os.getenv('MESSAGE', 'This is default message')
    secretcode = os.getenv('SECRETCODE', 'No secet code')
    return render_template('index.html', message=message, secretcode=secretcode, hostname=hostname)
if __name__ == '__main__':
    app.run(debug=True)
