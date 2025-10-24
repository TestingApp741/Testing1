```python
from flask import Flask, request, jsonify

app = Flask(__name__)

carpools = []

@app.route('/carpool', methods=['POST'])
def create_carpool():
    data = request.json
    carpool = {
        'id': len(carpools) + 1,
        'driver': data['driver'],
        'passengers': data.get('passengers', []),
        'destination': data['destination'],
        'date': data['date']
    }
    carpools.append(carpool)
    return jsonify(carpool), 201

@app.route('/carpool', methods=['GET'])
def get_carpools():
    return jsonify(carpools), 200

@app.route('/carpool/<int:carpool_id>', methods=['GET'])
def get_carpool(carpool_id):
    carpool = next((c for c in carpools if c['id'] == carpool_id), None)
    if carpool is None:
        return jsonify({'error': 'Carpool not found'}), 404
    return jsonify(carpool), 200

@app.route('/carpool/<int:carpool_id>', methods=['DELETE'])
def delete_carpool(carpool_id):
    global carpools
    carpools = [c for c in carpools if c['id'] != carpool_id]
    return jsonify({'message': 'Carpool deleted'}), 204

if __name__ == '__main__':
    app.run(debug=True)
```