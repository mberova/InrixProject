from flask import Flask
from optimize import opt as optimize

app = Flask(RouteRush)

@app.route('/opt', methods = ['GET'])
def opt(): 
    res = optimize() # TODO: Convert this to JSON
    return res

@app.route('/home', methods = ['GET'])
def home(): 
    res = optimize() # TODO: Convert this to JSON
    return res

if __name__ == '__main__':
    app.run(debug=True)