from flask import Flask, request
from datetime import datetime
import socket
import os
import platform

app = Flask(__name__)

request_count = 0

@app.route("/")
def home():
    return {
        "message": "Flask Infrastructure Demo API",
        "status": "running",
        "environment": os.getenv("APP_ENV", "development"),
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "hostname": socket.gethostname()
    }

@app.route("/health")
def health():
    return {
        "status": "healthy"
    }

@app.route("/info")
def info():
    return {
        "hostname": socket.gethostname(),
        "python_version": platform.python_version(),
        "platform": platform.system(),
        "environment": os.getenv("APP_ENV", "development"),
        "version": os.getenv("APP_VERSION", "1.0.0")
    }

@app.route("/time")
def time():
    return {
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

@app.route("/metrics")
def metrics():
    global request_count
    request_count += 1

    return {
        "request_count": request_count,
        "client_ip": request.remote_addr
    }

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
