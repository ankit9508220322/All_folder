from flask import Flask, render_template, request, redirect, session,jsonify
from db import Database
import api

dbo = Database()
app = Flask(__name__)
app.secret_key = "secret123"   


# start new project
@app.route('/')
def home():
    if 'email' in session:   
        return render_template('profile.html')
    else:
        return render_template('profile.html')


# register page
@app.route("/register")
def register():
    return render_template("register.html")

# register form
@app.route("/perform_registation", methods=['POST'])
def perform_register():
    name = request.form.get("user_name")
    email = request.form.get("user_email")
    password1 = request.form.get("user_password")
    password2 = request.form.get("confirm_password")
    
    data = dbo.insert(name, email, password1, password2)

    if data:
        return render_template('login.html',message="registation sucess full Logine Now")
    else:
        return render_template('register.html',message="Email Already Exit")
        
# login page
@app.route('/peforme_form',methods=['POST'])
def gatedata():
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    cource = request.form.get("cname")
    city = request.form.get("city")
    block = request.form.get("block")
    polic_station = request.form.get("pstation")
    pincode = request.form.get("zcode")
    date = request.form.get("date")
    time = request.form.get("time")
    reasion = request.form.get("reasion")
    responce= fname,lname,email,cource,city,block,polic_station,pincode,date,time,reasion
    print(responce)


@app.route("/login")
def login():   # duplicate name fix
    return render_template("login.html")

# login form
@app.route("/perfome_logine", methods=['POST'])
def perfome_login():
    email = request.form.get("email")
    password = request.form.get("password")
    response = dbo.search(email, password)

    if response:
        session['email'] = email   # 👈 same naming use
        return redirect('/profile')
    else:
        return "incorrect email and password"
    
# portfolio (protected)
@app.route('/portfolio')
def portfolio():
    if 'email' not in session:
        return redirect('/login')
    return render_template('portfolio.html')

# portfolio second number
@app.route('/portfolio2')
def portfolio2():
    return render_template('/portfolio2.html')

# profile (protected)
@app.route("/profile")
def profile():
    if 'email' not in session:
        return redirect('/login')
    return render_template('profile.html')


# ner (protected)
@app.route('/ner')
def ner():
    if 'email' not in session:
        return redirect('/login')
    return render_template('ner.html')


# ner perform
@app.route('/perfome_ner', methods=['POST'])
def perform():
    text = request.form.get('text')   # ✅ fix
    result = api.ner_text(text)       # ✅ fix
    print(result)
    result=''
    for i in result['entities']:
        result = result+i['name']+" "+ i['category'+"\n"]
    return render_template('ner.html',result=result)

# .form to contact me 
@app.route('/form_contact')
def contact_form():

    if 'email' not in session:
        return redirect('/register')
    return render_template('/form.html')

# 


if __name__ == "__main__":
    app.run(debug=True,port=7000)