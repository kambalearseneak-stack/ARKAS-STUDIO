from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
# Clé secrète nécessaire pour la gestion de la session et des messages (flash)
app.secret_key = 'arkas_studio_secret_key_change_in_production'

@app.route('/')
def home():
    """ Page d'accueil principal de ARKAS STUDIO """
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """ Gestion de la connexion """
    if request.method == 'POST':
        # Traitement du formulaire de connexion
        email = request.form.get('email')
        password = request.form.get('password')
        # Logique d'authentification à implémenter plus tard
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """ Gestion de l'inscription """
    if request.method == 'POST':
        # Traitement de l'inscription
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        # Logique de création de compte à implémenter plus tard
        return redirect(url_for('dashboard'))
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    """ Tableau de bord utilisateur (génération musicale) """
    return render_template('dashboard.html')

if __name__ == '__main__':
    # Mode debug activé pour le développement
    app.run(host='0.0.0.0', port=5000, debug=True)
