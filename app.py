import sqlite3
import os
from flask import Flask, render_template, url_for, request, flash, g
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
menu = [{"name": "Gugu", "url": "registration"}, {"name": "Gaga", "url": "Gaga"}]

@app.route('/', methods = ["POST", "GET"])
@app.route('/registration', methods = ["POST", "GET"])
def registration():
  db = get_db()
  if request.method == "POST":
    if len(request.form["name"]) > 2:
      flash("User regged", category="success")
      print(url_for("registration"))
      print(request.form["name"])
    else:
      flash("malo bukv", category="error")
  return render_template("registration.html")

@app.teardown_appcontext
def close_db(error):
  if hasattr(g, 'link_db'):
    g.link_db.close()

@app.route('/main')
def main():
  db = get_db()
  dbase = FDataBase(db)
  return render_template("main.html", menu = dbase.getMenu())

if __name__ == '__main__':
  app.run(debug=True)