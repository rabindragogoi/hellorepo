from flask import Flask, jsonify
import json
app = Flask(__name__)

@app.route('/get_connections')
def firstapp():
    return jsonify({'message': 'pong'}), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8399)

