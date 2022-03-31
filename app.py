from flask import Flask
from flask import render_template, redirect, request, url_for

app = Flask(__name__)

friend_list = [{"name": "Tyler Nachman" } ]

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Tyler\'s Friends')

@app.route('/about')
def about():
    return render_template('about.html', pageTitle='About Mike')

@app.route('/estimate', methods=['GET', 'POST'])
def estimate():
    if request.method == 'POST':
        form = request.form
        radius = float(form['radius'])
        height = float(form['height'])
        
        estimate=radius+height
        return render_template('estimate.html', quote=estimate)
    return render_template('estimate.html')


if __name__ == '__main__':
    app.run(debug=True)
