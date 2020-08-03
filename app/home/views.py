from flask import render_template
from app import model

def home():
    
    return render_template('home/home.html')