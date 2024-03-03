from flask import Flask, request, jsonify, render_template
from anilist_api import fetch_anime_by_genre
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
@app.route('/')
def home():
    return render_template('index.html')  # Renders the home page

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    genre = data.get('genre')
    
    if not genre:
        return jsonify({"error": "Genre not provided"}), 400
    
    recommendations = fetch_anime_by_genre(genre)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
