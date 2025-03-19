from flask import Flask, render_template, request, jsonify  # Importando jsonify corretamente
from flask_sqlalchemy import SQLAlchemy

# Configuração do aplicativo Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tarefas.db'  # Banco de dados SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# --------------------------------------------
# Modelo do Banco de Dados
# --------------------------------------------

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    json = db.Column(db.String(1000), nullable=False)

    def __repr__(self):
        return f'<Tarefa {self.json}>'

# --------------------------------------------
# Rotas do Flask
# --------------------------------------------

@app.route('/')
def hello_world():
    return render_template('tarefas.html')

@app.route('/save_tarefa', methods=['POST'])
def salvar_tarefa():
    # Recebe os dados da requisição (JSON)
    nova_tarefa = Tarefa(
        json=request.get_json()  # Recebe o JSON e armazena no campo "json"
    )
    db.session.add(nova_tarefa)
    db.session.commit()
    return render_template('tarefas.html')

@app.route('/bd_tarefas', methods=['GET'])
def bd_tarefas():
    # Obtém todas as tarefas salvas no banco de dados
    tarefas = Tarefa.query.all()

    lista_tarefas = []
    for tarefa in tarefas:
        lista_tarefas.append({
            'id': tarefa.id,
            'json': tarefa.json
        })

    return jsonify(lista_tarefas)  # Retorna os dados em formato JSON

if __name__ == '__main__':
    app.run(debug=True)
