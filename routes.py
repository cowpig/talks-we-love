import flask as fsk
import utils
app = fsk.Flask(__name__)

def get_user():
    if "username" in fsk.session:
        return (fsk.session['username'], True)
    else:
        return (fsk.request.remote_addr, False)

@app.route('/')
def index():
    user, logged_in = get_user()
    return fsk.render_template("index.html", logged_in=logged_in, username=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    user, logged_in = get_user()
    if fsk.request.method == 'POST':
        if utils.check_password(fsk.request.form['username'], fsk.request.form['password']):
            fsk.session['username'] = fsk.request.form['username']
            fsk.redirect(fsk.url_for("index"))
        else:
            error = True

    return fsk.render_template("login.html", error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    user, logged_in = get_user()
    if logged_in:
        fsk.redirect(fsk.url_for("index"))
    elif fsk.request.form['username'] and fsk.request.form['password']:
        success, msg = utils.set_password(fsk.request.form['username'],
                                        fsk.request.form['password'])
        if success:
            fsk.redirect(fsk.url_for("index"))
        else:
            print "Uh oh! There was an error: \n {}".format(msg)
 
@app.route('/talks/')
@app.route('/talks/<talkname>')
def talks(talkname=None):
    user, logged_in = get_user()
    if talkname==None:
        return "here's where we'll be able to browse the talks"
    return """
    this will be the page that displays the talk named:<br>
    {}
    """.format(talkname)

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    user, logged_in = get_user()
    if 'username' not in fsk.session:
        return fsk.redirect(fsk.url_for('login'))

    return "here's where we can submit a talk"


if __name__ == '__main__':
    app.run(debug=True)
