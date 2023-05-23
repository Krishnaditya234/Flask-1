#Importing flask module in the project
from flask import Flask
app = Flask(__name__)
@app.route("/index")
def first_webpage():
    name = "Flask"
    return render_template("index.html",index_variable = name)
app.run(debug=True)