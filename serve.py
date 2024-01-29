from flask import Flask
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_ip():
    hostname = socket.gethostname()
    private_ip = socket.gethostbyname(hostname)
    return private_ip

@app.route('/', methods=['POST'])
def stress_cpu():
    subprocess.Popen(["python3", "stress_cpu.py"])
    return "CPU stress initiated.", 202

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

