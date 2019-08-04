from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    session['number'] = random.randint(1, 100)
    print(session['number'])
    return render_template('numbergame.html')

@app.route('/guess', methods=['POST'])
def guess():
    if int(request.form['guess']) == session['number']:
        result = "Correct"
        return render_template('correct.html', result=result, num = int(request.form['guess']))
    elif int(request.form['guess']) < session['number']:
        result = "Too Low"
        return render_template('numbergame.html', result=result)
    else:
        result = "Too High"
        return render_template('numbergame.html', result=result)
@app.route("/correct")
def reset():
    session.clear()
    return redirect('/')
if __name__ == "__main__":
    app.run(debug=True)