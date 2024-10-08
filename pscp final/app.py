from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/login")
def home():
    return render_template("login.html")

@app.route("/hello")
def helloname():
    fname=request.args.get('fname')
    fage=request.args.get('fage')
    return render_template("hello.html",data={"name":fname,"age":fage})

@app.route("/page1")
def page1():
    fname=request.args.get('fname')
    return render_template("page1.html",data={"name":fname})

@app.route("/page2")
def page2():
    return render_template("page2.html")

@app.route("/page3")
def page3():
    return render_template("page3.html")

@app.route("/page4")
def page4():
    fname=request.args.get('fname')
    return render_template("page4.html",data={"name":fname})

if __name__ == "__main__":
    app.run(port=8000,debug=True)