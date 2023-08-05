# from flask import Flask, render_template
# from os import listdir
# from os.path import isfile, join
# app = Flask(__name__)


# @app.route("/")
# def home():
#     a = ""
#     # for i in listdir("./app/templates"):
#     #     a = a + i + "<br>"
#     return render_template("./app/templates/index.html")
from flask import Flask, render_template
app = Flask(__name__)
 
@app.route('/')
def home():
   return render_template('index.html')
if __name__ == '__main__':
   app.run()