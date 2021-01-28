from flask import Flask, render_template
# from flask_talisman import Talisman

app = Flask(__name__)
# Talisman(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')
