#!/usr/bin/env python

import cv2
from flask import Flask
from flask_socketio import SocketIO, emit
import config

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, config.FRAME_WIDTH)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, config.FRAME_HEIGHT)


def generate_frames():
    if not camera.isOpened():
        print("Error: Camera is not opened")
        exit()

    while True:
        success, frame = camera.read()

        if not success:
            print("Error: Can't retrieve frame from camera")
            break

        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            continue

        frame_bytes = buffer.tobytes()

        socketio.emit('frame', {'frame_data': frame_bytes}, namespace=config.NAMESPACE)


@app.route('/')
def index():
    return "Video stream..."


@socketio.on('connect', namespace=config.NAMESPACE)
def connect():
    print('Client connected')


@socketio.on('disconnect', namespace=config.NAMESPACE)
def disconnect():
    print('Client Disconnected')


if __name__ == "__main__":
    socketio.start_background_task(generate_frames)
    socketio.run(app, host='0.0.0.0', port=config.PORT)
