#!venv/bin/python
from flask import request, jsonify, url_for, render_template
from pay import app, db, auth
from models import ParkingDB


@app.route('/')
@app.route('/index')
def index():
    return "Hello World!"


@app.route('/claim', methods=['POST'])
def claim():
    if request.method == 'POST':
        parking_id = request.json.get('parking_id')
        parking = ParkingDB.query

@app.route('/parking', methods=['GET'])
def parking():
    if request.method == 'GET':
        parking = ParkingDB.query.all()
        json_parking = map(get_parking_json, parking)
        return jsonify(parking=json_parking)
    if request.method == 'POST':
        claim_or_relinquish = int(request.json.get('id')) # -1_or_1
        parking = ParkingDB.query.filter_by(id=id).first()
        parking.num_spots += claim_or_relinquish
        db.session.commit()
        return "Success"
    return "Fuck you"


@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template("park.html")
    if request.method == 'POST':
        print request.form
        lat = request.form['latitude']
        long = request.form['longitude']
        num_spots = request.form['num_spots']
        street = request.form['street']
        rate = request.form['rate']

        parking = ParkingDB(lat=lat, long=long,
            num_spots=num_spots, street=street, rate=rate)

        db.session.add(parking)
        db.session.commit()

        return render_template("park.html",
                    lat = lat, long = long,
                    num_spots = num_spots,
                    street = street, rate = rate)
    return "Fuck you"


def get_parking_json(parking):
    return {'id': parking.id,
            'latitude': parking.lat,
            'longitude': parking.long,
            'num_spots': parking.num_spots,
            'street': parking.street,
            'rate': parking.rate }

