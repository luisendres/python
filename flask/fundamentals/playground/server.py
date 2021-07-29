from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play/<int:x>/<shade>')
def index (x, shade):
    return render_template("index.html", x = x, shade = shade)
    
# @app.route('/dojo')
# def success():
#     return "Dojo!"

if __name__ =='__main__':
    app.run(debug=True)