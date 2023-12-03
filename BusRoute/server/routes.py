from flask import Flask, render_template, request
from optimize import opt as optimize

from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/api/opt', methods = ['GET'])
def opt(): 
    res = optimize(request) # TODO: Convert this to JSON
    return res

@app.route('/home', methods = ['GET'])
def home(): 
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)