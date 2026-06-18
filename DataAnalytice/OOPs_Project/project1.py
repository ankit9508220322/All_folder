import nlpcloud

# client = nlpcloud.Client("gpt-oss-120b", "881c25d9bf8687370bd5531a9faf41bb7f63b9a8", gpu=True)
# client.entities(
#     """John Doe started learning Javascript when he was 15
#     years old. After a couple of years he switched to Python and
#     starter learning low level programming. He is now a Go expert at Google.""",
#     searched_entity="programming languages"
# )

# import nlpcloud
class NlpApp:
    def __init__(self):
        self.__database={}
        self.__first_menu()  # input the menu first part  line number= 17
        
    def __first_menu(self):
        first_input=input("""
              how woult like to  process:
              1. Not a number register: 
              2. Already register Logine
              3. Not choice this? Exit
              
              """)
        if first_input == '1':
            self.__register()  # this line number input = 50
        elif first_input == '2':
            self.__login()  # this line number input = 65
        else:
            exit()
    # second menue is start: code this pard
    def __second_menue(self):
        second_input=input("""
              how woult like to  process:
              1. NER: 
              2. Language detection:  
              3. sentiment Analysis
              4. Logout
              
              """)
        if second_input == '1':
            self.__ner()
        elif second_input == '2':
            self.__language_detection()      
        elif second_input == '3':
            # self._setiment()
            pass
        
    # /////////////////////////////////////////////////////////////////////////////////////////////////
    def __register(self):
        name=input("Enter the Name: [] ")
        email=input("Enter the Email:[] ")
        pasword = input("Enter the Password:[] ")
        
        if email in self.__database:
            print("Email is Already  Register: ")
        else:
            self.__database[email] = [name , pasword]
            print("registation sucessfull: ")
            print(self.__database)
            self.__first_menu()
            self.__login()
            
        #    lohine page this part
        
    def __login(self):
        email = input("enter the email: ")
        pasword = input("enter the password: ")
        if email in self.__database:
            if self.__database[email][1] == pasword:
                print("login sucess full:  ")
                self.__second_menue()
            else:
                print("Worng pasword: ")
                self.__login()
        else:
            print("this email is not register:  ")
            self.__first_menu()
# this part is Near
    def __ner(self):
       paragrapg = input("enter the paragraph:  ")
       search_term = input("what would you like to search:  ")
    #    API server work in lile connect thr __ner:
       client = nlpcloud.Client("gpt-oss-120b", "5e9aac2b3b5f541a27637e2b1811a725633cc90c", gpu=True)
       response = client.entities(paragrapg, searched_entity=search_term)
       print(response)
    
obj = NlpApp()