from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_world(name):
  return 'Hello World! %s' % name

@app.route('/hello')
def hello_world_template():
  return render_template('hello.html')

@app.route('/hello/pull')
def hello_world_pull():
  return 'pull'

if __name__ == '__main__':
  app.run(port='5000', debug='true')
  # app.run(host='0.0.0.0', port='5000')
