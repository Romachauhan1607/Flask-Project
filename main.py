from flask import Flask,jsonify
import requests

app = Flask(__name__)

#Route
@app.route("/")
def Homepage():
    return "<h1>Welcome to the Homepage<h1>" 

@app.route("/add",methods=['POST'])
def addition():
    if request.method=="POST":
        result=request.json['num1']+request.json[num2]
        return "The summation is {}".format(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001)



