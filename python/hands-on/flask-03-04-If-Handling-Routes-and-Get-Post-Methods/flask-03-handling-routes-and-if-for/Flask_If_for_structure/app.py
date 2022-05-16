from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def head():
    first = "This is my first conditiıns experience"
    return render_template("index.html", message=first)

@app.route("/list")
def header():
    names = ['Apple', 'Google', "Samsung", "Honda", "Amazaon", "IBM", "Microsoft", "Tesla"]
    return render_template("body.html", object = names)

if __name__=="__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=80)