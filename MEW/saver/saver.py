import json

from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/api', methods=['POST'])
def saver():
	jsonData = request.data
	theJson = json.loads(jsonData.decode('utf-8'))
	return str(theJson['key'])

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=1337, debug=True)