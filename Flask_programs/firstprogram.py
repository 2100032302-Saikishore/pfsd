from flask import Flask,render_template
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"
@app.route("/emp/<int:emp1>")
def show_emp(emp1):
    return 'EMP ID NUMBER %d' %emp1
@app.route("/emp1/<float:emp1>")
def show_emp1(emp1):
    return 'EMP ID NUMBER %f' %emp1
@app.route("/ksk")
def index():
    return render_template("hello.html")
if __name__ =="__main__":
    app.run()