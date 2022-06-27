from flask import Flask,request

app=Flask(__name__)


@app.route('/home')
def hello_internet():
    return "Hello Internet!"

@app.route('/maybe/<int:number>')
def maybe(number):
    maybe=int(number)*int(number)
    return str(maybe)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')