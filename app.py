import os
import socket
import requests
from flask import Flask, render_template

app = Flask(__name__)

def fetch_random_office_gif():
    giphy_api_key = os.getenv('GIPHY_API_KEY')
    if not giphy_api_key:
        print("Giphy API key not found.")
        return None

    endpoint = f'https://api.giphy.com/v1/gifs/random?api_key={giphy_api_key}&tag=the office'

    try:
        response = requests.get(endpoint)
        if response.status_code == 200:
            gif_url = response.json()['data']['image_original_url']
            return gif_url
    except Exception as e:
        print(f"Error fetching GIF: {e}")

    return None

@app.route('/')
def index():
    gif_url = fetch_random_office_gif()
    hostname = socket.gethostname()
    message = os.getenv('MESSAGE', 'This is default message')
    return render_template('index.html', gif_url=gif_url, message=message, hostname=hostname)
if __name__ == '__main__':
    app.run(debug=True)
