# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# # porifolio
# @app.route('/portfolio')
# def portfolio():
#     return render_template('porifilio.html')
# # /////////////////////

# from flask import Flask, render_template,request,redirect
# # from db import Database
# # import api
# # dbo = Database()
# app = Flask(__name__)
# # start new project
# # @app.route("/")
# # def main():
# #     return "what to do find name \n write rout name "

# # two number url
# @app.route("/register")
# def register():
#     return render_template("register.html")

# # logine url 
# @app.route("/login")
# def home():
#     return render_template("login.html")


# # my_portfolio in this page
# @app.route("/portfolio")
# def portfolio():
#     return render_template("portfolio.html")

# # this url is new start
# @app.route("/perform_template", methods=['POST'])
# def perform_register():

#     name = request.form.get("user_name")
#     email = request.form.get("user_email")
#     password1 = request.form.get("user_password")
#     password2 = request.form.get("confirm_password")
    
#     total_data=dbo.insert(name ,email,password1,password2)
#     if total_data:
#         return render_template('login.html')
#     else:
#         return render_template('register.html')
    
#     # return f"Name: {name} <br> Email: {email} <br> Password: {password1} <br> Confirm Password: {password2}"


# @app.route("/perfome_logine",methods=['POST'])
# def perfome_login():
#     email = request.form.get("email")
#     password = request.form.get("password")
#     total_data = dbo.search(email , password)
#     if total_data:
#         return redirect('/profile')
#     else:
#         return "incoret email and password"
#     return f"Email: {email} <br> Password: {password} "
# @app.route("/profile")
# def profile():
#     return render_template('profile.html')

# @app.route("/ner")
# def Ner():
#     return render_template('ner.html')

# # ner peform this url
# @app.route('/perfome_ner', methods=['POST'])
# def perform():
#     text = request.form['text']
#     print(text)   # check text
#     result = api.ner(text)
#     return result
# # /////////
# if __name__ == '__main__':
#     app.run(port=8000,debug=True)