from flask import Flask, url_for, request, redirect, session, escape
app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username></p>
            <p><input type=password name=password></p>
            <p><input type=submit value=Login></p>
        </form>
    '''

@app.route('/talks/')
@app.route('/talks/<talkname>')
def talks(talkname=None):
    if talkname==None:
        return "here's where we'll be able to browse the talks"
    return """
    this will be the page that displays the talk named:<br>
    {}
    """.format(talkname)

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if 'username' not in session:
        return redirect(url_for('login'))

    return "here's where we can submit a talk"



if __name__ == '__main__':
    app.run(debug=True)
