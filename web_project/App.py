from flask import Flask, render_template,request
import requests
app = Flask(__name__)

@app.route('/teame1')
def teame1():
    result = requests.get('http://127.0.0.1:5000/api/team')
    data= result.json()['teams']
    return render_template('web.html',data = data)


@app.route('/api/teamevteame')
def teame2():
    teame1 = request.args.get('teame1')
    teame2 = request.args.get('teame2')
    response = requests.get('http://127.0.0.1:5000/api/teamevteame?team1={}&team2={}'.format(teame1,teame2))
    response = response.json()
    return response

app.run(debug=True)