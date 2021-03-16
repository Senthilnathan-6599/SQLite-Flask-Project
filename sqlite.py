from flask import Flask,render_template,request
import sqlite3 as sql
app =  Flask(__name__)
@app.route("/")
def user():
    return render_template("student1.html")
@app.route("/newentry")
def entry():
    return render_template("studentinformation.html")
@app.route("/insert", methods = ["POST","GET"])
def insert():
    if request.method == "POST":
        try:
           nm = request.form["nj"]
           address = request.form["add"]
           city = request.form["city"]
           pin = request.form["pin"]
           with sql.connect("database.db") as con:
             cur=con.cursor()
             cur.execute("INSERT INTO students (name,addr,city,pin) VALUES(?,?,?,?)",(nm,address,city,pin))
             con.commit()
             msg = "Message inserted successfully"
        except:
            con.rollback()
            msg = "error in insert operation"
        finally:
            return render_template("result.html",msg = msg)
            con.close()
@app.route("/list")
def list():
    with sql.connect("database.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall();
        return render_template("list.html",rows = rows)
if __name__ == "__main__":
    app.run(debug = True)
            
    