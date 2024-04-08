from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/home")
def home():
    return "Hi There, welcome to homepage of my AWS Web Services"

@app.route("/about-Us")
def index():
    return "About This Page"

@app.route("/data")
def data():
    sample_data = {"Name" : "Rayan", "Age" : 19, "Class" : "LC01"}
    return jsonify(sample_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

