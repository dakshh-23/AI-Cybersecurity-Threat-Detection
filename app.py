from flask import Flask
from flask import render_template
from flask import jsonify

import random

app = Flask(__name__)

@app.route('/')

def dashboard():

    return render_template(
        'index.html'
    )

@app.route('/live_data')

def live_data():

    traffic = random.randint(200,1000)

    threats = random.randint(0,20)

    cpu = random.randint(10,90)

    ram = random.randint(20,95)

    status = random.choice([
        "SAFE",
        "THREAT DETECTED"
    ])

    return jsonify({

        "traffic": traffic,

        "threats": threats,

        "cpu": cpu,

        "ram": ram,

        "status": status

    })

if __name__ == '__main__':

    app.run(debug=True)