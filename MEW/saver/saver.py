from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/api', methods=['POST'])
def saver():
	return str(request.data)

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=1337, debug=True)