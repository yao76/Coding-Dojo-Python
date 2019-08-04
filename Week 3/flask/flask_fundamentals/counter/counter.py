from flask import Flask, render_template, request, redirect, session # added request

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
# our index route will handle rendering our form
@app.route('/')
def visits():
    # if 'visits' in session:
    #     session['visits'] = session.get('visits') + 1  # reading and updating session data
    # else:
    #     session['visits'] = 1 # setting session data
    # #return "Total visits: {}".format(session.get('visits'))
    # return render_template("counter.html", num_visits = session['visits'])
    session['visits'] += 1
    return render_template("counter.html")
@app.route('/add_two')
def add_two():
    session['visits'] += 2
    return render_template("counter.html")
@app.route('/destroy_session/')
def delete_visits():
    session['visits'] = 0
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)