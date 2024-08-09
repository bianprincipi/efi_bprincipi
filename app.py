from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Configuración
class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Cambia esto según tu base de datos
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import *

@app.route('/')
def index():
    return render_template('index.html')

# CRUD routes for Equipo model as an example
@app.route('/equipos')
def equipo_list():
    equipos = Equipo.query.all()
    return render_template('equipo_list.html', equipos=equipos)

@app.route('/equipos/new', methods=['GET', 'POST'])
def equipo_new():
    if request.method == 'POST':
        # code to add new equipo
        pass
    return render_template('equipo_form.html')

@app.route('/equipos/<int:id>/edit', methods=['GET', 'POST'])
def equipo_edit(id):
    equipo = Equipo.query.get_or_404(id)
    if request.method == 'POST':
        # code to update equipo
        pass
    return render_template('equipo_form.html', equipo=equipo)

@app.route('/equipos/<int:id>/delete', methods=['POST'])
def equipo_delete(id):
    equipo = Equipo.query.get_or_404(id)
    db.session.delete(equipo)
    db.session.commit()
    return redirect(url_for('equipo_list'))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
