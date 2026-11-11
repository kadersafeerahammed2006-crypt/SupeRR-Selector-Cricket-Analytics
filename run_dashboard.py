"""
Standalone Web Dashboard Launcher: SupeRR Selector Season 2 - PressurePlay Analytics
Serves the bespoke Dark Blue HTML/JS dashboard on http://localhost:8000
Zero Streamlit, instant loading, 100% responsive.
"""

import os
import sys
import webbrowser
import http.server
import socketserver
from pathlib import Path

PORT = 8000
WEB_DIR = os.path.join(os.path.dirname(__file__), "web")

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WEB_DIR, **kwargs)

    def log_message(self, format, *args):
        # Suppress verbose terminal log spam
        pass

def run():
    # Make sure dashboard HTML exists
    html_path = os.path.join(WEB_DIR, "index.html")
    if not os.path.exists(html_path):
        import subprocess
        subprocess.run([sys.executable, "src/build_web_dashboard.py"], check=True)

    url = f"http://localhost:{PORT}"
    print("=" * 70)
    print("   PRESSUREPLAY ANALYTICS - BESPOKE DARK BLUE WEB PLATFORM")
    print("=" * 70)
    print(f">> Web Dashboard URL: {url}")
    print(f">> Direct File Link:   file:///{html_path.replace(os.sep, '/')}")
    print("-" * 70)
    print(">> Press Ctrl+C to stop the server at any time.")
    print("=" * 70)

    # Open browser
    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"Note: Could not auto-launch browser ({e}). Please navigate to {url}")

    # Start HTTP server
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n>> Server stopped gracefully.")

if __name__ == "__main__":
    run()

