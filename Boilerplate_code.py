#Importing flask module in the project
from flask import Flask

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class 
@app.route("/flask_2")

def second_flask():
    return "Python is fun"

app.run(debug=True)
