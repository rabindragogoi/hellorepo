from flask import Flask,jsonify
app = Flask(__name__)

@app.route('/get_connections')
def first_app():

    data_dict = {'result' : 'welcome'}
    return jsonify(data_dict)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8399)

