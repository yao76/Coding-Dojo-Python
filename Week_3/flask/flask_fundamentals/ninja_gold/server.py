from flask import Flask, render_template, request, redirect, session
import random
import datetime
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
@app.route('/')
def index():
    try:
        session['total_gold']
    except KeyError:
        session['total_gold'] = 0
    try:
        session['activities']
    except KeyError:
        session['activities'] = []

    return render_template("index.html")
@app.route('/process_money', methods=['POST'])
def process_money():
    now = datetime.datetime.now()
    button_pressed = request.form['hidden']
    session["state"] = "Earned"
    if button_pressed == 'farm':
        print('farm')
        farm_gold = random.randint(10,20)
        session['total_gold'] += farm_gold
        print(f"farm gold: {farm_gold}")
        print(f"total gold: {session['total_gold']}")
        session['activities'].append(session["state"] + " " + str(farm_gold) + ' from the farm! ' + now.strftime("%Y/%m/%d %I:%M %p")) 
        print(session['activities'])
    elif button_pressed == 'cave':
        print('cave')
        cave_gold = random.randint(5,10)
        session['total_gold'] += cave_gold
        print(f"cave gold: {cave_gold}")
        session['activities'].append(session["state"] + " " + str(cave_gold) + ' from the cave! ' + now.strftime("%Y/%m/%d %I:%M %p"))
        print(f"total gold: {session['total_gold']}")
    elif button_pressed == 'house':
        print('house')
        house_gold = random.randint(2,5)
        session['total_gold'] += house_gold
        session['activities'].append(session["state"] + " " + str(house_gold) + ' from the house! ' + now.strftime("%Y/%m/%d %I:%M %p"))
        print(f"house gold: {house_gold}")
        print(f"total gold: {session['total_gold']}")
    elif button_pressed == 'casino':
        print('casino')
        casino_gold = random.randint(-50,50)
        session['total_gold'] += casino_gold
        if casino_gold < 0:
            session["state"] = "lost"
            print(session["state"])
            casino_gold = -1*casino_gold
            session['activities'].append('Entered casino and ' + session["state"] + " " +str(casino_gold) + ' gold! Ouch... ' + now.strftime("%Y/%m/%d %I:%M %p"))
        else:
            session["state"] = "won"
            print(session["state"])
            session['activities'].append('Entered casino and ' + session["state"] + " " + str(casino_gold) + ' gold! Huzzah! ' + now.strftime("%Y/%m/%d %I:%M %p"))
        print(f"casino gold: {casino_gold}")
        print(f"total gold: {session['total_gold']}")
    return redirect("/")
@app.route("/clear")
def reset():
    session['total_gold'] = 0
    session['activities'] = []
    return redirect('/')
if __name__ == "__main__":
    app.run(debug=True)