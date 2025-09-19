from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        <title>
            Device Specification - 25013503
        </title>
    </head>
    <body>
        <h1>Device Specification - 25013503</h1>
        <table border="3" cellspacing="2" cellpadding="4">
            <tr bgcolor="grey">
                <th>S.no</th>
                <th>Device Specification</th>
                <th>Descryption</th>
            </tr>
            <tr bgcolor="lightgreen">
                <td>1.</td>
                <td>Storage</td>
                <td>477GB</td>
            </tr>
            <tr bgcolor="lightgreen">
                <td>2.</td>
                <td>Processor</td>
                <td>AMD Ryzen 7 7435HS</td>
            </tr>
            <tr bgcolor="lightgreen">
                <td>3.</td>
                <td>Graphics card</td>
                <td>4GB</td>
            </tr>
            <tr bgcolor="lightgreen">
                <td>4.</td>
                <td>Version</td>
                <td>24HS</td>
            </tr>
            <tr bgcolor="lightgreen">
                <td>5.</td>
                <td>Windows</td>
                <td>11</td>
            </tr>
        </table>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()