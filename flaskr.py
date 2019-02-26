from flask import Flask, render_template, request
from flask.json import jsonify

app = Flask(__name__)

class Chat():
  def __init__(self):
    self.chatContents = list()

  def addContent(self, content):
    self.chatContents.append(content)

  def getContents(self):
    return self.chatContents

  def initContents(self):
    self.chatContents.clear()

  def serialize(self):
    return {
      'chatContents': [
        content.serialize() for content in self.chatContents
      ]
    }

class Content():
  def __init__(self, message, author):
    self.message = message
    self.author = author
    self.readerIds = list()

  def serialize(self):
    return {
      'message': self.message,
      'author': self.author,
      'readerIds': [
        readerId for readerId in self.readerIds
      ]
    }

c = Chat()

@app.route('/hello')
def hello_template():
  return render_template('hello.html')

@app.route('/chat')
def chat_template():
  return render_template('chat.html')

@app.route('/calc')
def calc_template():
  return render_template('calc.html')




@app.route('/chat/message', methods=['GET'])
def getChat():
  userId = request.cookies.get("userId")
  for content in c.getContents():
    if userId not in content.readerIds:
      content.readerIds.append(userId)
  return jsonify(c.serialize())

@app.route('/chat/message', methods=['POST'])
def addChat():

  uesrId = request.cookies.get("userId")
  message = request.get_data().decode('UTF-8')
  content = Content(message, uesrId)
  c.addContent(content)
  return 'ok'

@app.route('/chat/message/init', methods=['POST'])
def initChat():
  c.initContents()
  return 'ok'

if __name__ == '__main__':
  app.run(port='5000', debug='true')
  # app.run(host='0.0.0.0', port='5000', debug='true')
