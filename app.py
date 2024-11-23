import sqlite3
import os
from flask import Flask, render_template, url_for, request, flash, g, redirect, session, json, send_file, send_from_directory
from flask_socketio import SocketIO, emit
from FDataBase import FDataBase

DATABASE = 'app.db'
DEBUG = True
SECRET_KEY = "1234"

tasksSections = ["TasksWeb", "TasksCrypto", "TasksForensic", "TasksReverse", "TasksSteganography", "TasksPPC", "TasksOSINT", "tasksPWN"]
graphicsSave = [] 

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '1234'
socketio = SocketIO(app)

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
    if len(request.form["name"]) > 2:
      if dbase.checkIfUserExists(request.form["name"]):
        flash("Username exists", category="error")
      else:
        res = dbase.addUser(request.form["name"], request.form["password"], dbase.createTrueFlags(request.form["name"],  tasksSections), request.form["team"])
        if not res:
          flash("User registration error", category="error")
        else:
          flash("User regged", category="success")
          dbase.addUserPoints(request.form["name"])
          return render_template("reg-auth.html", status = "Authorization")
    else:
      flash("malo bukv", category="error")
  return render_template("reg-auth.html", status = "Registration")

@app.route('/authorization', methods = ["POST", "GET"])
def authorization():
  db = get_db()
  dbase = FDataBase(db)
    

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
    if len(dbase.getLeaders()) < 3:
      leaders = dbase.getLeaders()
    else:
      leaders = [dbase.getLeaders()[0], dbase.getLeaders()[1], dbase.getLeaders()[2]]
    return render_template("main.html", user = user, leaders = leaders, yourPoints = dbase.getYourPoints(user), tasksWeb = dbase.getTasks("TasksWeb"), tasksCrypto = dbase.getTasks("TasksCrypto"), tasksForensic = dbase.getTasks("TasksForensic"), tasksReverse = dbase.getTasks("TasksReverse"), tasksSteganography = dbase.getTasks("TasksSteganography"), tasksPPC = dbase.getTasks("TasksPPC"), tasksOSINT = dbase.getTasks("TasksOSINT"), tasksPWN = dbase.getTasks("TasksPWN"), sections = dbase.getSectionsLen(tasksSections), trueFlags = dbase.getUser(session['userLogged']))

@app.route("/main", methods = ["GET"])
def mainWithoutName():
  if 'userLogged' in session:
    return redirect(url_for("main", user = session['userLogged']))
  

@app.route("/TasksWeb/<number>")
def taskWeb(number):
  return render_template(f"/tasks/web/{number}/{number}.html")

@app.route("/TasksReverse/<number>")
def taskReverse(number):
  if number in ["1"]:
    folder = f"/ctf_web/templates/tasks/reverse/{number}/"
    files = os.listdir(folder)
    filename = files[0]
    return send_from_directory(folder, filename, as_attachment=True)
  return render_template(f"/tasks/web/{number}/{number}.html")

@app.route("/TasksSteganography/<number>")
def taskSteganography(number):
  if number in ["1"]:
    folder = f"/ctf_web/templates/tasks/steganography/{number}/"
    files = os.listdir(folder)
    filename = files[0]
    return send_from_directory(folder, filename, as_attachment=True)
  return render_template(f"/tasks/web/{number}/{number}.html")

@app.teardown_appcontext
def close_db(error):
  if hasattr(g, 'link_db'):
    g.link_db.close()


@socketio.on('client_event')
def handle_client_event(data):    

    db = get_db()
    dbase = FDataBase(db)

    if dbase.getSolution(data[0], dbase.get_section(data[1], tasksSections)):
      if not (dbase.checkTrueFlag(session['userLogged'], data[1])):
        taskPoints = 100 * dbase.getPointsMultiplier(dbase.get_section(data[1], tasksSections), data[0])
        points = dbase.getYourPoints(session['userLogged'])[0]['pointValue'] + taskPoints
        dbase.gainPoints(session['userLogged'], points)
        team = dbase.getUser(session['userLogged'])[0]['team']
        teamPoints = dbase.getTeamPoints(team)[0]['pointValue'] + taskPoints
        dbase.gainTeamPoints(team, teamPoints)
        print(dbase.getUser(session['userLogged'])[0]['trueFlags'])
        
        otherTeam = dbase.getOtherTeam(team)

        teamData = {
          'title': team,
          'points': teamPoints,
          'otherTeamPoints': otherTeam[0]['pointValue'],
        }
        emit('gainTeamPoints', teamData, broadcast=True)

      dbase.sendFlag(dbase.setFlag(dbase.getUser(session['userLogged'])[0]['trueFlags'], data[1]), session['userLogged'])
      data = {
        'taskId': data[1],
        'isFlagValid': True,
        'points': points
      }

      dbase.addTeamSolution(team, dbase.getUser(session['userLogged'])[0]['trueFlags'])
      print(dbase.getUser(session['userLogged'])[0]['trueFlags'])

      emit('server_response', data)
    else:
      points = dbase.getYourPoints(session['userLogged'])[0]['pointValue']
      data = {
        'taskId': data[1],
        'isFlagValid': False,
        'points': points
      }
      emit('server_response', data)

@socketio.on('save_graphics')
def save_graphics(graphics):
  global graphicsSave
  graphicsSave = []
  graphicsSave.append(graphics['labels'])
  graphicsSave.append(graphics['team1'])
  graphicsSave.append(graphics['team2'])

@socketio.on('user_connected')
def handle_connect():
    global graphicsSave
    emit("load_data", graphicsSave)

if __name__ == '__main__':
  socketio.run(app, host='127.0.0.1', port=5000)