from __future__ import with_statement
from functools import singledispatch
from unicodedata import numeric
from flask import Flask
from flask import render_template, redirect, request, url_for

app = Flask(__name__)

friend_list = [{"name": "Tyler Nachman" } ]

@app.route('/')
def index():
    if request.method == 'GET':
        return render_template('index.html')
    return render_template('index.html', pageTitle='Vertical Tank Maintenance')

@app.route('/about')
def about():
    if request.method == 'GET':
        return render_template('about.html')
    return render_template('about.html', pageTitle='About Us')

@app.route('/estimate', methods=['GET', 'POST'])
def estimate():
    if request.method == 'POST':
        form = request.form
        radius = float(form['radius'])
        height = float(form['height'])
        pi = 3.14
        top = pi * radius**2
        sides = 2 * (pi * (radius * height))
        area = top + sides
        sqft = area / 144
        material = sqft * 25
        labor = sqft * 15
        estimate = round(material + labor, 2)
        return render_template('estimate.html', quote=estimate)
    return render_template('estimate.html', pageTitle="Get an Estimate")


if __name__ == '__main__':
    app.run(debug=True)
