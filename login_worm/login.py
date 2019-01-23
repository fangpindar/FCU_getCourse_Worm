from flask import Flask, request
from flask import render_template
import worm
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def login():
    if request.method == 'POST':
        return worm.worm(request.values['ID'],request.values['Password'])

    return render_template("app.html")

if __name__ == '__main__':
    app.debug = True
    app.run(port = 5000)    
