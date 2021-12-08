from flask import Flask
from faker import Faker
app = Flask(__name__)


@app.route('/requirements/')
def printer():
    with open('requirements.txt', 'r') as f:
        text = f.read()
        return text


@app.route('/generate-users/')
def user():
    users = Faker()
    for _ in range(2):
        return f'{users.name()}! {users.email()}'

@app.route('/mean/')
def date():
    with open()