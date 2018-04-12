from flask import Flask, render_template, redirect


app = Flask(__name__)
app.secret_key = 'sjlidfghofq978041y7asouiv807b1f2b9usaxkcjn'
from .views import *
#app.run()
