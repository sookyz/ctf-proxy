from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length).decode('utf-8', errors='replace')
        print("=" * 60, flush=True)
        print(f"收到请求: {self.path}", flush=True)
        print(f"Headers: {dict(self.headers)}", flush=True)
        print(f"Body:\n{body}", flush=True)
        print("=" * 60, flush=True)
        resp = {
            "id": "chatcmpl-test", "object": "chat.completion", "created": 1234567890,
            "model": "gpt-4o-mini",
            "choices": [{"index": 0, "message": {"role": "assistant", "content": "ok"}, "finish_reason": "stop"}],
            "usage": {"prompt_tokens": 1, "completion_tokens": 1, "total_tokens": 2}
        }
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(resp).encode())

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(b'{"status":"ok"}')

    def log_message(self, format, *args):
        pass

port = int(os.environ.get("PORT", 8000))
HTTPServer(('0.0.0.0', port), Handler).serve_forever()