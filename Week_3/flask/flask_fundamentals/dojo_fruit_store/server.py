from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    strawberry_form = request.form['strawberry']
    raspberry_form = request.form['raspberry']
    apple_form = request.form['apple']
    first_name_form = request.form['first_name']
    last_name_form = request.form['last_name']
    student_id_form = request.form['student_id']
    count = int(strawberry_form) + int(raspberry_form) + int(apple_form)
    return render_template("checkout.html", strawberry_template = strawberry_form, raspberry_template = raspberry_form, apple_template = apple_form, first_name_template = first_name_form, last_name_template = last_name_form, student_id_template = student_id_form, total_fruit_template = count)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    