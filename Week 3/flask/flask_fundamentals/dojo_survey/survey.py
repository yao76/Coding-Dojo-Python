from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def default_form():
    return render_template('survey.html')

@app.route('/result', methods=['POST'])
def show_results():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    dojo_locations_form = request.form['locations']
    favorite_language_form = request.form['languages']
    comment_form = request.form['comment']
    return render_template("result.html", name_on_template=name_from_form, location_on_template = dojo_locations_form, favorite_language_template = favorite_language_form, comment_template = comment_form)
if __name__ == "__main__":
    app.run(debug=True)