from flask import Flask, request, render_template
import socket
from common_ports import ports_and_services

app = Flask(__name__)

def get_open_ports(target, start_port, end_port):
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        return None, "Error: Invalid hostname"
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)
        if sock.connect_ex((ip, port)) == 0:
            open_ports.append(port)
        sock.close()
    return (open_ports, ip), None

@app.route("/scan", methods=["GET", "POST"])
def home():
    error = None
    results = None
    ip = None
    target = ""
    if request.method == "POST":
        target = request.form.get("target", "").strip()
        try:
            start = int(request.form.get("start_port", 20))
            end = int(request.form.get("end_port", 1024))
        except ValueError:
            error = "Please use valid port numbers."
        else:
            data, err = get_open_ports(target, start, end)
            if err:
                error = err
            else:
                open_ports, ip = data
                results = [(p, ports_and_services.get(p, "unknown")) for p in open_ports]

        print("Open ports found:", open_ports)
    return render_template("index.html", target=target, results=results, ip=ip, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
