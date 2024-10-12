from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '안녕하세요, Flask!'

if __name__ == '__main__':
    app.run(debug=True)