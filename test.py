from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Welcome to Python Flask App!</h1> <p1>hello this sample page</p1>"

if __name__ == "__main__":
    app.run()
