from flask import Flask, request, jsonify
from joblib import load

clf = load("clf.joblib")

app = Flask(__name__)

@app.route("/")
def status():
    return "Ready!"

@app.route("/predict", methods=["POST"])
def predict():
    data_dict = request.get_json()

    student = data_dict["student"]
    balance = data_dict["balance"]
    income = data_dict["income"]

    X_predict = [[student, balance, income]]

    default = clf.predict(X_predict)[0]
    probabily_of_default = clf.predict_proba(X_predict)[0][1]

    return jsonify({
        "default": bool(default),
        "probabily_of_default": float(probabily_of_default)
    })

if __name__ == "__main__":
    app.run(debug=True)