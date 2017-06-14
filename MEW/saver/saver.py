from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/save', methods=['OPTIONS'])
def saver():
	return request.get_json(force=True)

if __name__ == '__main__':
  app.run( 
        host="0.0.0.0",
        port=1337,
  )