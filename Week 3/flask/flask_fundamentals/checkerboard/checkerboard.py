from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')   
def default_checkerboard():
    return render_template('checkerboard.html', cols = 8, rows = 8)
@app.route('/<x>')
def change_cols(x):
    return render_template('checkerboard.html', cols = int(x), rows = 8)
@app.route('/<x>/<y>')
def change_cols_and_rows(x,y):
    return render_template('checkerboard.html', cols = int(x), rows = int(y))

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.