import random
import string
from flask import *
app=Flask(__name__)
@app.route("/string")
def randstr():
    return render_template("string.html")
@app.route("/strting", methods=["GET"] )
def hello():
       id = request.form["id"]
       result_str = ''.join(random.sample(string.ascii_lowercase, id))
       return(result_str)
if __name__=="__main__":
    app.run()