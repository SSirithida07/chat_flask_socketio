from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/index2')
def index2():
    return render_template('index2.html')

@socketio.on('message')
def handle_message(message):
    if request.path == '/index2':
        if message.startswith('Chat2:'):
            emit('message', message, broadcast=True)
        else:
            emit('message', message, broadcast=True)
    else:
        if message.startswith('Chat1:'):
            emit('message', message, broadcast=True)
        else:
            emit('message', message, broadcast=True)
            
       

if __name__ == '__main__':
    socketio.run(app)
