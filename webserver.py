import socket
import network
from utime import sleep_ms
from blink import request_pedestrian, request_car, update_traffic_light

ssid = 'ampel-WS'
password = '12345678'

ap = network.WLAN(network.AP_IF)
ap.config(essid=ssid, password=password)
ap.active(True)

while ap.active() == False:
    pass

print("Connection successful")
print(ap.ifconfig())

html_page = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Ampelsteuerung</title>
</head>
<body>
    <h1>Ampelsteuerung</h1>

    <button onclick="sendRequest('/pedestrian')">Fußgänger wartet</button>
    <button onclick="sendRequest('/car')">Auto wartet</button>

    <p id="status">Bereit</p>

    <script>
        async function sendRequest(path) {
            try {
                await fetch(path);
            } catch (error) {
                document.getElementById("status").textContent = "Fehler beim Senden";
            }
        }
    </script>
</body>
</html>
"""

addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)

print("listening on", addr)

while True:
    try:
        cl, addr = s.accept()
        print("client connected from", addr)
        request_message = cl.recv(1024)
        print(request_message)

        if "/pedestrian" in request_message:
            request_pedestrian()
        elif "/car" in request_message:
            request_car()

        response_message = (
            "HTTP/1.0 200 OK\r\n"
            "Content-type: text/html\r\n"
            "Connection: close\r\n\r\n"
            + html_page
        )
        cl.send(response_message)
        cl.close()

    except OSError as e:
        cl.close()
        print('connection closed')
        
    update_traffic_light()
    sleep_ms(100)
