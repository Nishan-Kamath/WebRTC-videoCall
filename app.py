from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

# Handle joining the room
@socketio.on('join')
def handle_join(data):
    room = data['room']
    join_room(room)
    emit('user_joined', data, room=room)

# Handle WebRTC signaling data
@socketio.on('signal')
def handle_signal(data):
    room = data['room']
    emit('signal', data, room=room)

if __name__ == '__main__':
    # Ensure you're running in debug mode for development
    socketio.run(app, debug=True)
