from flask import Flask, request, render_template_string
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

    return render_template_string('''
        <form method="post">
            Character ID: <input type="text" name="character_id">
            <input type="submit" value="Get Character">
        </form>
        {% if character_data %}
            {% if character_data.error %}
                <p><strong>Error:</strong> {{ character_data.error }}</p>
            {% else %}
                <h2>Character Information</h2>
                <p><strong>Name:</strong> {{ character_data.name }}</p>
                <p><strong>Height:</strong> {{ character_data.height }}</p>
                <p><strong>Mass:</strong> {{ character_data.mass }}</p>
                <p><strong>Hair Color:</strong> {{ character_data.hair_color }}</p>
                <p><strong>Eye Color:</strong> {{ character_data.eye_color }}</p>
            {% endif %}
        {% endif %}
    ''', character_data=character_data)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
