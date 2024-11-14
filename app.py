from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    character_data = None
    if request.method == 'POST':
        character_id = request.form.get('character_id')
        if character_id:  # Check if character_id is not empty
            api_url = f'https://swapi.py4e.com/api/people/{character_id}/'
            response = requests.get(api_url)
            if response.status_code == 200:
                character_data = response.json()
            else:
                character_data = {'error': 'Character not found.'}  # Add error handling

    return render_template('index.html', character_data=character_data)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
