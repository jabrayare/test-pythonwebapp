from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "<p> Hello World(Made some changes here and pushed to azure deveops repo!) </p>"

if __name__ == "__main__":
  app.run()