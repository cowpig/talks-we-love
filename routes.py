from flask import Flask
app = Flask(__name__)

@app.route('/')
def main():
    return """
    <html>
    this will be the main page
    </html>
    """

@app.route('/talks/<talkname>')
def talk(talkname):
    return """
    <html>
    this will be the page that displays the talk named:<br>
    {}
    </html>
    """.format(talkname)

if __name__ == '__main__':
    app.run(debug=True)