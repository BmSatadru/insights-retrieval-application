from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/another-endpoint', methods=['GET'])
def another_endpoint():
    # Some logic here
    return jsonify({'message': 'Hello from another endpoint'})

def handler(request):
    return app(request) 