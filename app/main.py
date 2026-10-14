"""Minimal HTTP service so the container has something to run."""

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

from app.refunds import refund_amount


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = parse_qs(urlparse(self.path).query)
        amount = query.get("amount", ["0"])[0]
        try:
            body = str(refund_amount(amount))
            status = 200
        except (ValueError, ArithmeticError) as exc:
            body, status = f"error: {exc}", 400
        self.send_response(status)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(body.encode())

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
