 
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lessons')
def lessons():
    return render_template('lessons.html')

@app.route('/practice')
def practice():
    return render_template('practice.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

if __name__ == '__main__':
    app.run()
