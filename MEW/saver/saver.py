import json

from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/api', methods=['POST'])
def saver():
	jsonData = json.loads(request.data.encode('utf-8'))
	return jsonData['password']

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=1337, debug=True)