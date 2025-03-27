from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('name'))

@app.route('/name', methods=['GET', 'POST'])
def name():
    if request.method == 'POST':
        nome = request.form.get('nome')
        return redirect(url_for('index', nome=nome))
    return render_template('name.html')

@app.route('/sucesso')
def index():
    nome = request.args.get('nome') 
    return render_template('index.html', nome = nome)


if __name__ == '__main__':
    app.run(debug=True)
