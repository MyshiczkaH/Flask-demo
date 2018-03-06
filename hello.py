from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.template_filter('cap')#sablona - muze se jmenovat jinak nez ta fce
def capitalize(word):
    return word[0].upper() + word[1:]


@app.route('/')
def index():
    return 'Ahoj Pyladies!'

@app.route('/url/')
def url():
    return url_for('hello',name='PETR', count=123, _external=True)
#external da celou adresu
#'hello' je tady jeno funkce viz radek 18

@app.route('/hello/')
@app.route('/hello/<name>/')
@app.route('/hello/<name>/<int:count>')
def hello(name='world', count=1):
    return render_template('hello.html', name=name)
