from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def hello():
    name = "Hello World!!"
    return name

@app.route('/good', methods=['POST'])
def good():
    data = request.get_data()
    print(data)
    return data

## おまじない
if __name__ == "__main__":
    app.run(debug=True)