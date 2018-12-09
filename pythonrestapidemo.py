from flask import Flask

app = Flask(__name__)

#Flask is a framework for rest api

@app.route('/')
def home():
    return '<h1>Hello Python Training</h1>'

@app.route('/<name>')
def homename(name):
    return '<h1>Hello Python Training</h1>'.format(name)

if __name__=='__main__':
    app.run(debug=True)