from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkboard ():
    return render_template("index.html", x = 8, y = 8)
    
@app.route('/<int:x>')
def checkboard_x (x):
    return render_template("index.html", x = x, y = 8)
    
@app.route('/<int:x>/<int:y>')
def checkboard_x_y(x,y):
    return render_template("index.html", x = x, y = y)

if __name__ =='__main__':
    app.run(debug=True)
    