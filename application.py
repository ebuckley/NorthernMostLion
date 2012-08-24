#using this style of imports to help me learn where flask
import os
import sc2reader
from stats import *
from flask import Flask, url_for, request, render_template, redirect, url_for
from werkzeug import secure_filename
from sc2reader.utils import Length
from random import randrange

UPLOAD_FOLDER = "C:\Users\Ersin\NorthernMostLion\uploads"
ALLOWED_EXTENSIONS = set(['zip', '7z', 'tar.gz', 'SC2Replay'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 50 * 1024 * 1024

def allowed_file( filename ):
    """validate that the file being upload is allowed"""
    return '.' in filename and \
            filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods = ['GET', 'POST'])
def index():
    """Home page"""
    error = None
    if request.method == "POST":
        file = request.files['inputfile']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('show_replay', replay_id = filename))

        else:
            error = "Invalid file upload"
            return render_template('index.html', error = error)

    return render_template('index.html')

@app.route('/about')
def about_us():
    """about us page"""
    return "about us page"

@app.route('/u/<username>')
def show_user(username):
    """docstring for show_replay"""
    return "Hi {0}".format(username)

@app.route('/r/<replay_id>')
def show_replay(replay_id):
    """docstring for show_replay"""

    # load the replay file
    path = os.path.join( UPLOAD_FOLDER, replay_id)
    replays = sc2reader.read(path, load_level = 4)
    replay = replays[0]

    players = list()
    winners = list()

    for team in replay.teams:
        for person in team:
            players.append(person)
            if person.result == "Win":
                winners.append(person)


    return render_template('replayview.html', winners = winners, matchlength = replay.length ,players = players)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == "POST":
        if valid_login(request.form["username"],
                        request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'

    if error != None:
        return render_template('login.html', error = error)
    else:
        return render_template('login.html')


# web server error handling

@app.errorhandler(404)
@app.errorhandler(405)
def handle_error(error):
    return render_template('error.html', error = error)


if __name__ == '__main__':
    with app.test_request_context():
        # we can test the requests here, this will all be put out to the python console
        print url_for('show_user', username = "ersin buckley")
        print url_for('show_replay', replay_id = "1239081290389.sc2replay")


    app.run( debug = True )



