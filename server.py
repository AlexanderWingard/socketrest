import flask
from flask.ext.socketio import SocketIO, join_room, leave_room, send
app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.debug = True
socketio = SocketIO(app)
client = app.test_client()
data = 0
data2 = 0

@app.route('/')
def index():
    global count
    return flask.render_template("index.html")


@app.route('/api/set')
def set():
    global data
    data += 1
    push_api('/api/get')
    return "ok"

@app.route('/api/set2')
def set2():
    global data2
    data2 -= 1
    push_api('/api/get2')
    return "ok"


@app.route('/api/get')
def get():
    return str(data)

@app.route('/api/get2')
def get2():
    return str(data2)

def call_api(api):
    return {'room': api, 'data': client.get(api).data }


def push_api(api):
    socketio.emit("data", call_api(api), room=api)

app.jinja_env.globals.update(call_api=call_api)


@socketio.on('join_rooms')
def handle_message(message):
    for room in message['data']:
        join_room(room)


@socketio.on('connect')
def on_connect():
    print "connect"


if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=5001)
