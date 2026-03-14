from flask import Flask


app = Flask('ping')

@app.route('/ping', methods=['GET'])
def ping():
    return 'pong is called', 200
if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)