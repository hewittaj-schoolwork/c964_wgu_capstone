from flask import Flask
from flask.app import Flask

# Whenever you pass in name you help determine the root path

app = Flask(__name__)

# Root directory
# @ signifies a decorator - way to wrap a function and modify its behavior
@app.route('/') 
def index():
    return "This is the homepage."

@app.route('/tuna')
def tuna():
    return "<h2>Tuna is good<h2>"

# a variable goes inbetween angled brackets
@app.route('/profile/<username>')
def profile(username):
    return "Hey there %s" % username

@app.route('/post/<int:post_id>')
def post(post_id):
    return "Post ID is %s" % post_id

# Start this application/web server
# Only start the web server when this file is requested directly
if __name__ == "__main__":
    app.run(debug=True)