import os
from flask import Flask, render_template, request, jsonify
import replicate

app = Flask(__name__)
app.secret_key = 'arkas_studio_secret_key_change_in_production'

# Configurez votre clé API Replicate (idéalement via une variable d'environnement)
# os.environ["REPLICATE_API_TOKEN"] = "VOTRE_TOKEN_REPLICATE_ICI"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return redirect(url_for('dashboard'))
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/generate', methods=['POST'])
def generate_music():
    """ Route API pour interroger Replicate (MusicGen) """
    data = request.get_json()
    prompt = data.get('prompt', '')
    genre = data.get('genre', '')

    if not prompt:
        return jsonify({'error': 'Le prompt est obligatoire'}), 400

    # Fusion du style musical et du prompt
    full_prompt = f"{genre} style: {prompt}"

    try:
        # Appel du modèle MusicGen de Meta sur Replicate
        output = replicate.run(
            "meta/musicgen:b05b1d261cd7346307a304eca54837c3cd42ea530b1ac53e137260d799a7f0d0",
            input={
                "prompt": full_prompt,
                "model_version": "stereo-large",
                "duration": 15  # Durée en secondes
            }
        )
        
        # Output contient l'URL du fichier audio généré
        return jsonify({'audio_url': output})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
