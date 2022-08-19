from flask import Flask,render_template,redirect,url_for
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"
@app.route("/table/<int:num>")
def table(num):
    return render_template("print-table.html",n=num)
@app.route("/emp/<int:emp1>")
def show_emp(emp1):
    return 'EMP ID NUMBER %d' %emp1
@app.route("/emp1/<float:emp1>")
def show_emp1(emp1):
    return 'EMP ID NUMBER %f' %emp1
@app.route("/ksk")
def index():
    return render_template("hello.html")
@app.route("/user/<name>")
def hello_user(name):
    if name == "admin":
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest",guest=name))
@app.route("/admin")
def hello_admin():
    return "hello Admin"
@app.route("/guest/<guest>")
def hello_guest(guest):
    return "hello %s as guest "%guest
if __name__ =="__main__":
    app.run()
