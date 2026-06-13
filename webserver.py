import socket
import network
import machine

ssid = '{insertSSID}'
password = '{insertSSID-PW}'
led = machine.Pin("LED",machine.Pin.OUT)
ap = network.WLAN(network.AP_IF)
ap.config(essid=ssid, password=password)
ap.active(True)
while ap.active() == False:
    pass
print('Connection successful')
print(ap.ifconfig())
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
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print('listening on', addr)
led.off()

# Listen for connections
while True:
    try:
        cl, addr = s.accept()
        print('client connected from', addr)
        request = cl.recv(1024)
        led.on()
        print(request)
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(html)
        cl.close()
        led.off()
    except OSError as e:
        try:
            cl.close()
        except:
            pass
        print('connection closed')