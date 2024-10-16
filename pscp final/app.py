from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/objective")
def objective():
    return render_template("objective.html")

@app.route("/page3")
def page3():
    return render_template("page3.html",)

@app.route("/page4")
def page4():
    fname=request.args.get('fname')
    fage=request.args.get('fage')
    return render_template("page4.html",data={"name":fname,"age":fage})

@app.route("/page5")
def page5():
    fname=request.args.get('fname')
    return render_template("page5.html",data={"name":fname})

@app.route("/page6")
def page6():
    return render_template("page6.html")

@app.route("/page7")
def page7():
    return render_template("page7.html")

@app.route("/page8")
def page8():
    return render_template("page8.html")

@app.route("/page9")
def page9():
    return render_template("page9.html")

@app.route("/page10")
def page10():
    return render_template("page10.html")

if __name__ == "__main__":
    app.run(port=8000,debug=True)