from flask import Flask, render_template, request, redirect, session # added request

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print('*'*80)
    print(request.form)
    
    # name_from_form = request.form['name']
    # email_from_form = request.form['email']
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect("/show")
    # return render_template("show.html", name_on_template=name_from_form, email_on_template=email_from_form)

# adding this method
@app.route("/show")
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template("show.html", name_on_template=session["username"], email_on_template=session["useremail"])

if __name__ == "__main__":
    app.run(debug=True)