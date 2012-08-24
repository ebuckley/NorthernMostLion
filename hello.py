from flask import Flask, url_for, request, render_template #using this style of imports to help me learn where flask

app = Flask(__name__)

def valid_login(username, password):
    """docstring for valid_login"""
    if username == "ersin" and password == "buckley":
        return True
    return False

def log_the_user_in(username):
    """docstring for log_the_user_in"""
    return "Yo whaddup %s logged in yo!" % username

@app.route('/')
def index():
    """index file"""
    return "Hello World"

@app.route('/about')
def about_us():
    """about us page"""
    return "about us page"

@app.route('/u/<username>')
def show_user(username):
    """docstring for show_replay"""
    return "Hi {0}".format(username)

@app.route('/r/<int:replay_id>')
def show_replay(replay_id):
    """docstring for show_replay"""
    return "Replay %d" % replay_id

@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == "POST":
        print request.form
        if valid_login(request.form["username"],
                        request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'

    if error != None:
        return render_template('login.html', error = error)
    else:
        return render_template('login.html')


@app.errorhandler(404)
def handle_error(error):
    return render_template('error.html', error = error)


if __name__ == '__main__':
    with app.test_request_context():
        # we can test the requests here, this will all be put out to the python console
        print url_for('show_user', username = "ersin buckley")


    app.run( debug = True )



