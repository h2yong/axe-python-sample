"""Run the application using Gunicorn or Waitress based on the operating system."""

import os
import platform

from app.config import APP_CONFIG


def start_gunicorn_app() -> None:
    """Start the application with Gunicorn on non-Windows systems and Waitress on Windows."""
    if platform.system().lower() == "windows":
        os.system(f"waitress-serve --threads=4 --port={APP_CONFIG['DEFAULT']['REST_PORT']} app.server.http_server:app")
    else:
        # 服务主要处理io, 故使用gevent工作模式
        os.system(
            f"gunicorn --workers=4 --timeout=0 --worker-class=gevent --log-level=debug --bind=0.0.0.0:{APP_CONFIG['DEFAULT']['REST_PORT']} app.server.http_server:app "
        )


if __name__ == "__main__":
    start_gunicorn_app()
