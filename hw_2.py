from flask import Flask
from faker import Faker
import csv
import requests
from flask import Response

app = Flask(__name__)


@app.route('/requirements/')
def requirements():
    with open('requirements.txt', 'r') as f:
        text = f.read()
        return text


@app.route('/generate-users/<int:users>/', methods=["GET"])
def generate_users(users):
    user = Faker()
    lst = [user.name() + ": " + user.email() for _ in range(users)]
    return Response("<br>".join(lst))


@app.route('/mean/')
def mean():
    h = []
    w = []
    with open('hw.csv') as f:
        x = csv.DictReader(f)
        for i in x:
            h += [float(i[' "Height(Inches)"']) * 2.54]
            w += [float(i[' "Weight(Pounds)"']) * 0.454]
        mean_h = sum(h) / len(h)
        mean_w = sum(w) / len(w)
        return f'weight= {mean_w: 0.2f} height= {mean_h: 0.2f}'


@app.route('/space/')
def space():
    r = requests.get('http://api.open-notify.org/astros.json')
    names = r.json()['number']
    return str(names)
