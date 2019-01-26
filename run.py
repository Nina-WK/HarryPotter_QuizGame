import os
from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)



@app.route('/')
def index_page():
    return render_template("index_page.html")
    
@app.route('/game')
def game_page():
    return render_template("game_page.html")
    
@app.route('/score')
def score_page():
    return render_template("score_page.html")
    
@app.route('/contact')
def contact_page():
    return render_template("contact_page.html")











if __name__ == '__main__':
   app.run(host=os.environ.get('IP'),
           port=int(os.environ.get('PORT')),
           debug=True)