from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import json
import os


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'mesas.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class Mesas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_mesa = db.Column(db.String(100), nullable=False)
    fichas = db.Column(db.Text, nullable=False)


class Fichas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_personagem = db.Column(db.Text, nullable=False)
    classe_personagem = db.Column(db.Text, nullable=False)
    nivel_personagem = db.Column(db.Integer)
    força_personagem = db.Column(db.Integer)
    inteligencia_personagem = db.Column(db.Integer)
    constituicao_personagem = db.Column(db.Integer)
    armadura_personagem = db.Column(db.Integer)
    ataques_personagem = db.Column(db.Text, nullable=False)

with app.app_context():
    db.create_all()  # Cria as tabelas, se necessário
    # Verifique se já existe uma mesa com esse nome
    if not Mesas.query.filter_by(nome_mesa="ROOM INICIAL").first():
        mesas = Mesas(nome_mesa="ROOM INICIAL", fichas=json.dumps([
        {"id": 1, "nome": "Romulo"},
        {"id": 2, "nome": "Alexandre"}
        ]))
        db.session.add(mesas)
        db.session.commit()

        ficha_romulo = Fichas(
        id=1,
        nome_personagem="Romulo",
        classe_personagem="Guerreiro",
        nivel_personagem=1,
        força_personagem=10,
        inteligencia_personagem=8,
        constituicao_personagem=12,
        armadura_personagem=5,
        ataques_personagem=json.dumps([
                {
                "arma": "espada",
                "bonos": 4,
                "dado": 8 
                },
                {
                "arma": "besta",
                "bonos": 3,
                "dado": 6 
                }
            ])
        )

        ficha_alexandre = Fichas(
            id=2,
            nome_personagem="Alexandre",
            classe_personagem="Mago",
            nivel_personagem=1,
            força_personagem=5,
            inteligencia_personagem=18,
            constituicao_personagem=10,
            armadura_personagem=2,
            ataques_personagem=json.dumps([
                {
                "arma": "bola de fogo",
                "bonos": 0,
                "dado": 12 
                },
                {
                "arma": "raio de gelo",
                "bonos": 3,
                "dado": 6 
                }
            ])
        )

        # Adiciona as fichas ao banco de dados
        db.session.add(ficha_romulo)
        db.session.add(ficha_alexandre)
        db.session.commit()

@app.route('/')
def home():
    mesas = Mesas.query.all()

    # Para cada mesa, converta as fichas de JSON para uma lista de dicionários
    for mesa in mesas:
        mesa.fichas = json.loads(mesa.fichas)  # Converte a string JSON para lista de dicionários
    
    return render_template('index.html', mesas=mesas)


@app.route('/mesa/<int:mesa_id>')
def mesa(mesa_id):
    # Recupera a mesa pelo ID
    mesa = Mesas.query.get_or_404(mesa_id)

    # Converte a string JSON em um objeto Python (lista de dicionários)
    try:
        fichas = json.loads(mesa.fichas) if mesa.fichas else []
        
    except json.JSONDecodeError as e:
        fichas = []
        print(f"Erro ao decodificar o JSON da mesa: {e}")
    
    # Verificar se o JSON de ataques está sendo processado corretamente
    for ficha in fichas:
        print(f"-----")
        print(f"-----")
        print(ficha)
        print(f"-----")
        print(f"-----")
        print(f"-----")
        try:
            ficha['ataques_personagem'] = json.loads(ficha['ataques_personagem']) if ficha.get('ataques_personagem') else []
            
        except json.JSONDecodeError as e:
            ficha['ataques_personagem'] = []
            print(f"Erro ao decodificar o JSON dos ataques: {e}")

    # Passa os dados para o template
    return render_template('mesa.html', mesa=mesa, fichas=fichas)

app.run(debug=True)
