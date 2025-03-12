from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def hello():
    return render_template('index.html', nome = 'visitante')

@app.route('/aula07/<nome>')

def mensagem(nome):
    return f'boa noite {nome}!! espero que esteja tudo bem!'

if __name__ == '__main__':
    app.run(debug=True)
