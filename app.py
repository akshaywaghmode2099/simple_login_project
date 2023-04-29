from flask import *  
app = Flask(__name__)  
@app.route("/")
def html():
    return render_template("login.html")
  
@app.route('/login',methods = ['POST'])  
def login(): 
      uname=request.form['uname']  
      passwrd=request.form['pass']  
      if uname=="Akshay" and passwrd=="Akshay@2099":  
          return "<h1 style='color:Red'>Welcome</h1>"
      elif uname=="Prasad" and passwrd=="Prasad@2099":
             return "<h1 style='color:Red'>Welcome</h1>"
      elif uname=="SID" and passwrd=="SID@2099": 
           return "<h1 style='color:Red'>Welcome</h1>"
           
          
      else:
          return "<h1 style='color:green'>Plz clear Information</h1>"
   
if __name__ == '__main__':  
   app.run(debug = True)  