from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your Spoonacular API key
API_KEY = 'YOUR_SPOONACULAR_API_KEY'
BASE_URL = 'https://api.spoonacular.com/recipes/findByIngredients'

@app.route('/', methods=['GET', 'POST'])
def index():
    recipes = []
    if request.method == 'POST':
        ingredients = request.form.get('ingredients')
        if ingredients:
            response = requests.get(BASE_URL, params={
                'apiKey': API_KEY,
                'ingredients': ingredients,
                'number': 5  # Number of recipes to return
            })
            if response.status_code == 200:
                recipes = response.json()
            else:
                recipes = []
    
    return render_template('index.html', recipes=recipes)

if __name__ == "__main__":
    app.run(debug=True)
