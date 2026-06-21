from flask import Flask,jsonify,request
import ipl #  yah file name import huaa hai
app = Flask(__name__)

@app.route('/')
def home():
    return "jai ram ji ki"

@app.route('/api/team')
def teams():
    response = ipl.teamsApi()
    return jsonify(response)


# second Api
@app.route('/api/teamevteame')
def teamvteamv():
    # put the same name url team1 $ team2
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    response=ipl.team_vs_team(team1 ,team2)
    return jsonify(response)

app.run(debug=True)


