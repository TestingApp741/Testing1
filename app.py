```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Welcome to the Learning App!")

@app.route('/learn', methods=['POST'])
def learn():
    data = request.json
    return jsonify(message=f"Learning about {data.get('topic')}"), 201

if __name__ == '__main__':
    app.run(debug=True)
```