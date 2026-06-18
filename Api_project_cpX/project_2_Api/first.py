from flask import Flask,jsonify
import first2
app = Flask(__name__)

@app.route('/name')
def first():
    return "jai ram ji ki"

@app.route('/city')
def city():
    city_name = first2.final
    return jsonify(city_name)
app.run(debug=True)