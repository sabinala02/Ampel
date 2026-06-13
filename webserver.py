import socket
import network
from blink import cars_green, switch_to_pedestrians

ssid = '{insertSSID}'
password = '{insertSSID-PW}'
access_point = network.WLAN(network.AP_IF)
access_point.config(essid=ssid, password=password)
access_point.active(True)

while access_point.active() == False:
    pass

print('Connection successful')
print(access_point.ifconfig())

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Ampelsteuerung</title>
</head>
<body>
    <h1>Ampelsteuerung</h1>

    <form action="/pedestrian">
        <button type="submit">Fußgänger wartet</button>
    </form>

    <br>

    <form action="/car">
        <button type="submit">Auto wartet</button>
    </form>
</body>
</html>
"""

address = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
server_socket = socket.socket()
server_socket.bind(address)
server_socket.listen(1)

print('listening on', address)
cars_green()

while True:
    try:
        client_connection, address = server_socket.accept()
        request = client_connection.recv(1024).decode()
        print(request)

        if "/pedestrian" in request:
            switch_to_pedestrians()
        elif "/car" in request:
            cars_green()

        response = "HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n" + html
        client_connection.send(response)
        client_connection.close()

    except OSError:
        try:
            client_connection.close()
        except:
            pass