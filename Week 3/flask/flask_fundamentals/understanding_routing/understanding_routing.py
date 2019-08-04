from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/dojo')
def print_dojo():
    return 'Dojo!'
@app.route('/say/<name>')
def say_blank(name):
    return 'Hi ' + name.capitalize() + '!'
@app.route('/repeat/<times>/<word>')
def repeat_word(times, word):
    print('*'*80)
    # for i in range(int(times)):
    return (word + " ") * int(times)
@app.route('/say2/<string:name>')
def say_blank2(name):
    return 'Hi ' + name.capitalize() + '!'
@app.route('/repeat2/<int:times>/<string:word>')
def repeat_word2(times, word):
    # for i in range(int(times)):
    return (word + " ") * int(times)

if __name__ == "__main__":
    app.run(debug = True)