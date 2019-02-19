from flask import Flask, render_template, request
app = Flask(__name__)

class chat():
  def __init__(self):
    self.chatContent = ""

  def addContent(self, content):
    self.chatContent += content

  def getContent(self):
    return self.chatContent

c = chat()

@app.route('/hello/<name>')
def hello_world(name):
  return 'Hello World! %s' % name

@app.route('/hello')
def hello_world_template():
  return render_template('hello.html')

@app.route('/hello/pull')
def hello_world_pull():
  return 'pull'

@app.route('/chat', methods=['POST'])
def chat():
  c.addContent(request.get_data().decode('UTF-8'))
  return c.getContent()

if __name__ == '__main__':
  # app.run(port='5000', debug='true')
  app.run(host='0.0.0.0', port='5000', debug='true')
