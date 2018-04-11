from flask import Flask, render_template, redirect

def run():
    app = Flask(__name__)
    app.run()
    from .views import *
