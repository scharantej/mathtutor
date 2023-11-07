 
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    if request.form['username'] == 'admin' and request.form['password'] == 'secret':
      session['logged_in'] = True
      return redirect(url_for('dashboard'))
    else:
      return redirect(url_for('login'))
  else:
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'POST':
    if request.form['username'] == 'admin' and request.form['password'] == 'secret':
      session['logged_in'] = True
      return redirect(url_for('dashboard'))
    else:
      return redirect(url_for('register'))
  else:
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
  if session['logged_in']:
    return render_template('dashboard.html')
  else:
    return redirect(url_for('login'))

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
  app.run(debug=True)
