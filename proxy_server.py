from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

from replacer import modify_content


url = "https://dou.ua"


class DouProxyHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
        }
        dou = requests.get(url + self.path, headers=headers)

        self.send_response(dou.status_code)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        new_content = modify_content(dou.content.decode())
        self.wfile.write(new_content.encode())
        return


if __name__ == "__main__":
    server = HTTPServer(('127.0.0.1', 8888,), DouProxyHandler)
    server.serve_forever()
