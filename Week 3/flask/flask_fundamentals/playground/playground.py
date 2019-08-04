from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('playground.html', boxes = 3)
@app.route('/play/<x>')          # The "@" decorator associates this route with the function immediately following
def display_x_boxes(x):
    return render_template('playground.html', boxes = int(x))
@app.route('/play/<x>/<color>')          # The "@" decorator associates this route with the function immediately following
def change_color(x, color):
    return render_template('playground.html', boxes = int(x), box_color = color)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.