from flask import Flask, request
import json


app = Flask(__name__)

text = 'hello, world!'

@app.route('/')
def hello():

    return text

@app.route('/good', methods=['POST'])
def good():
    data = request.get_data().decode(encoding='utf-8')
    text = json.loads(data)['text']
    print(text)
    return text

## おまじない
if __name__ == "__main__":
    app.run(debug=True)