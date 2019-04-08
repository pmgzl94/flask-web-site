from flask import Flask, session

app = Flask(__name__);
app.config.from_object('config');

app.secret_key = 'any random string'

from app import views

