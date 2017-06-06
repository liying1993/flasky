from flask import Flask,request,render_template,flash
app = Flask(__name__)

@app.route('/')
def index():
    flash("lalalala")
    user_agent = request.headers.get("User-Agent")
    return '<p>Your broeser is %s</p>'%user_agent

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello ,%s!</h1>'%name

if __name__ == "__main__":
    app.run(debug=True)