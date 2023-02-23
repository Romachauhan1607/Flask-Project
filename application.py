from flask import Flask,jsonify,render_template
import requests

application = Flask(__name__)
app=application

#Route
@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/aboutus')
def aboutus():
    return "we are ineuron"

@app.route('/operation',methods=['POST'])
def operation():
    if request.method=='POST':
        operation = request.json['operation']
        num1 = request.form['num1']
        num2 = request.form['num2']
        result = num1 + num2
        return "The Operation is {} and the result is {}".format(operation,result)

        result = 0
        if operation == "add":
            result = num1+num2
        elif operation == "multiply":
            result = num1*num2
        elif operation == "division":
            result = num1/num2
        else:
            result = num1-num2
        
        return "render_template"("result.html",result=result)
    
if __name__ == "__main__":
 app.run(host="0.0.0.0",port=5001)

