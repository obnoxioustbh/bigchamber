from flask import Flask
app = Flask(__name__)

@app.route('/save', methods=['OPTIONS'])
def saver():
	return request.form

if __name__ == '__main__':
  app.run( 
        host="0.0.0.0",
        port=1337,
  )