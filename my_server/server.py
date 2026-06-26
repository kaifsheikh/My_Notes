import http.server
import json
import os
from urllib.parse import unquote, urlparse, parse_qs

# Yeh aapke notes wale folder ka path automatically le lega
NOTES_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Handler(http.server.SimpleHTTPRequestHandler):
    # Get Request
    def do_GET(self):
        parsed = urlparse(self.path)

        # API: Saari .md files ki list bhejo
        if parsed.path == "/api/files":
            md_files = []
            # Poore folder ko scan karo, har .md file ki relative path lo
            for root, dirs, files in os.walk(NOTES_DIR):
                for file in files:
                    if file.endswith(".md"):
                        full_path = os.path.join(root, file)
                        rel_path = os.path.relpath(full_path, NOTES_DIR)
                        # server.py aur viewer.html ko list mein mat daalo
                        if rel_path in ("server.py", "viewer.html"):
                            continue
                        # Windows backslash ko forward slash mein badlo
                        md_files.append(rel_path.replace("\\", "/"))
            md_files.sort()
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(md_files, indent=2).encode("utf-8"))

        # API: Ek specific file ka content bhejo
        elif parsed.path == "/api/file":
            qs = parse_qs(parsed.query)
            rel_path = qs.get("path", [None])[0]
            if not rel_path:
                self.send_error(400, "Missing path parameter")
                return
            # Safety check – sirf NOTES_DIR ke andar ki .md file hi khole
            safe_path = os.path.normpath(os.path.join(NOTES_DIR, rel_path))
            if not safe_path.startswith(NOTES_DIR) or not safe_path.endswith(".md"):
                self.send_error(403, "Forbidden")
                return
            try:
                with open(safe_path, "r", encoding="utf-8") as f:
                    content = f.read()
                self.send_response(200)
                self.send_header("Content-type", "text/plain; charset=utf-8")
                self.end_headers()
                self.wfile.write(content.encode("utf-8"))
            except FileNotFoundError:
                self.send_error(404, "File not found")

        # Baaki requests (jaise viewer.html, images) ko default serve karo
        else:
            super().do_GET()

if __name__ == "__main__":
    PORT = 8000
    print(
        f"🌟 Server shuru! Browser mein yeh kholen: http://localhost:{PORT}/viewer.html"
    )
    http.server.HTTPServer(("localhost", PORT), Handler).serve_forever()
