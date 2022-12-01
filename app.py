from flask import Flask,render_template,request,redirect
from dbms import addData,fetchData,specificData,updateData,deleteData

app=Flask(__name__)

#first Routing
@app.route("/")
def home_fun():
    return render_template("home.html")

#Secnod Routing
@app.route("/reglink")
def reg_func():
    return render_template("register.html")


#foruth Routing
@app.route("/savelink",methods=['POST'])
def save_func():
    email_id=request.form['email']
    username=request.form['username']
    password=request.form['password']
    t=(email_id,username,password)
    addData(t)
    #return "<h1>Registration Done!!!!!!!!!!!</h1>"
    return redirect("/reglink")

#foruth Routing
@app.route("/loginlink")
def login_func():
    return render_template("login.html")

#Fifth routing
@app.route("/savelink2",methods=['POST'])
def save2_func():
    username=request.form['username']
    password=request.form['password']
    if username=="admin" and password=="admin":
        return redirect("/displaylink")
    else:
        return redirect("/loginlink")
    

#sixth routing
@app.route("/displaylink")
def display_func():
    datalist=fetchData()
    return render_template("display.html",data=datalist)

#seventh routing
@app.route("/editlink/<int:id>")
def edit_func(id):
    datalist=specificData(id)
    return render_template("edit.html",data=datalist)

#eighth Routing
@app.route("/updatelink/<int:id>",methods=['POST'])
def update_func(id):
    email=request.form['email']
    username=request.form['username']
    password=request.form['password']
    t=(email,username,password,id)
    updateData(t)
    return redirect("/displaylink")

@app.route("/deletelink/<int:id>")
def delete_func(id):
    deleteData(id)
    return redirect("/displaylink")


if __name__=="__main__":
    app.run(debug=True)