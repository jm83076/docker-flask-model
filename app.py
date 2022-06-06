from flask import Flask
from flask import request
from flask import jsonify
import pickle
import perceptron


app = Flask(__name__)


@app.route('/')
def hello():
    return("Welcome to Jan Matynia's Flask app!")


@app.route('/predict', methods = ["GET"])

def get_prediction():

    # Getting features values e.g.
    #/predict?sl=4.5&sw=2.3&pl=1.3&pw=0.3
    sepal_length = float(request.args.get('sl'))   
    sepal_width = float(request.args.get('sw'))
    petal_length = float(request.args.get('pl'))
    petal_width = float(request.args.get('pw'))
    
    features = [sepal_length, sepal_width, petal_length, petal_width]
    
    with open("model_perc.pkl", "rb") as picklefile:
        model = pickle.load(picklefile)
    picklefile.close()
    
    
    predicted_class = int(model.predict(features))
    
    return jsonify(features = features, predicted_class = predicted_class)


if __name__ == "__main__":
    app.run(port=5001)
