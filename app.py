import sqlite3
import os
from flask import Flask, render_template, url_for, request, flash, g, redirect, session, json
from FDataBase import FDataBase

DATABASE = 'app.db'
DEBUG = True
SECRET_KEY = "1234"

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '1234'

app.config.update(dict(DATABASE = os.path.join(app.root_path, 'app.db')))

def connect_db():
  conn = sqlite3.connect(app.config['DATABASE'])
  conn.row_factory = sqlite3.Row
  return conn

def create_db():
  db = connect_db()
  with app.open_instance_resource('sq_db.sql', mode = 'r') as f:
    db.cursor().executescript(f.read())
    db.commit()
    db.close()

create_db()

def get_db():
  if not hasattr(g, 'link_db'):
    g.link_db = connect_db()
  return g.link_db

@app.route('/', methods = ["POST", "GET"])
@app.route('/registration', methods = ["POST", "GET"])
def registration():
  db = get_db()
  dbase = FDataBase(db)
  if request.method == "POST":
    print(request.base_url)
    if len(request.form["name"]) > 2:
      if dbase.checkIfUserExists(request.form["name"]):
        flash("Username exists", category="error")
      else:
        res = dbase.addUser(request.form["name"], request.form["password"])
        if not res:
          flash("User registration error", category="error")
        else:
          flash("User regged", category="success")
          return render_template("reg-auth.html", status = "Authorization")
    else:
      flash("malo bukv", category="error")
  return render_template("reg-auth.html", status = "Registration")

@app.route('/authorization', methods = ["POST", "GET"])
def authorization():
  db = get_db()
  dbase = FDataBase(db)
    
  print(dbase.getYourPoints(request.form["name"]))

  if request.method == "POST":
    if 'userLogged' in session and session['userLogged'] == request.form["name"]:
      return redirect(url_for("main", user = session['userLogged']))
    else:
      if not dbase.checkIfUserExists(request.form["name"]):
        flash("User does not exists", category="error")
      else:
        res = dbase.defineUser(request.form["name"], request.form["password"])
        if not res:
          flash("User logging error", category="error")
        else:
          flash("User logged", category="success")
          session['userLogged'] = request.form["name"]
          return redirect(url_for("main", user = session['userLogged']))
        
  return render_template("reg-auth.html", status = "Authorization")

@app.route("/main/<user>")
def main(user):
  db = get_db()
  dbase = FDataBase(db)
  if 'userLogged' in session:
    return render_template("main.html", user = user, leaders = dbase.getLeaders(), yourPoints = dbase.getYourPoints(user), tasksWeb = dbase.getTasksWeb())

@app.route("/main", methods = ["POST", "GET"])
def mainWithoutName():
  db = get_db()
  dbase = FDataBase(db)
  if dbase.getSolution(request.form["flag"]):
    trueFlag = True
    points = dbase.getUserPoints(session['userLogged'])[0]['pointValue'] + 200
    print(points)
    dbase.gainPoints(session['userLogged'], points)
    return render_template("main.html", user = session['userLogged'], leaders = dbase.getLeaders(), yourPoints = dbase.getYourPoints(session['userLogged']), tasksWeb = dbase.getTasksWeb(), trueFlag = json.dumps(trueFlag,  sort_keys=True, default=bool))
  else:
    if 'userLogged' in session:
      return redirect(url_for("main", user = session['userLogged']))
  

@app.route("/taskWeb/<number>")
def taskWeb(number):
  return render_template(f"/tasks/web/{number}/{number}.html")

@app.teardown_appcontext
def close_db(error):
  if hasattr(g, 'link_db'):
    g.link_db.close()

if __name__ == '__main__':
  app.run(debug=True)