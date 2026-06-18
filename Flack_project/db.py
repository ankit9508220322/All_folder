import json

class Database:

    def insert(self, name, email, password, password1):

        with open('user.json', 'r') as rf:
            users = json.load(rf)

        if email in users:
            return 0
        else:
            users[email] = [name, password, password1]
            with open("user.json", "w") as wr:
                json.dump(users, wr,indent=4)
            return 1
        
    # def form(self,fname,lname,email,cource,city,block,polic_station,pincode,date,time,reasion):
    #     with open('form.json','r')as fd:
    #         forms = json.load(fd)
    #         return fname
    # this line is logine  method check 
    def search(self,email,password):
         with open('user.json', 'r') as rf:
            users = json.load(rf)
            if email in users:
                if users[email][1] == password:
                    return 1
                else:
                    return 0
            else:
                return 0