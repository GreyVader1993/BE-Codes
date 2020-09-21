from flask import Flask, render_template, redirect, request, jsonify
from mongoengine import *
from A3_BoothSJ import booth_call
app = Flask(__name__, template_folder = "common", static_folder = "common")

app.config['MONGODB_SETTINGS'] = {
    "db" : "cl3",
    "host" : "localhost",
    "port" : 27017
}

connect(db = 'cl3', host = 'localhost', port = 27017)

def getOtherNumber():
    from models import Number #Prevents circular dependencies
    num_obj = Number.objects()
    return num_obj[0].number

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/getNumber', methods = ['GET', 'POST'])
def get_numbers():
    data = int(request.form['number'])
    num = getOtherNumber()
    print num
    ans = booth_call(data, num)

    return jsonify({"data" : ans})
