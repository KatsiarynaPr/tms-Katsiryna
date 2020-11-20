from datetime import timedelta
from pathlib import Path

from scripts.consts import DIR_REPO

SERVER_RUNNING_BANNER = """
+----------------------------------------+
|             SERVER WORKS!              |
+----------------------------------------+

Visit http://{host}:{port}

..........................................
"""

DIR_STATIC = (Path(__file__).parent.parent / "static").resolve()

METHODS_WITH_REQUEST_BODY = {
    "POST",
}

DIR_STORAGE = (DIR_REPO / "db").resolve()

USERS_STORAGE = (DIR_STORAGE / "users.json").resolve()

USER_COOKIE = "z37user"

USER_TTL = timedelta(minutes=5)

DATE_TIME_FMT = "%Y-%m-%d %H:%M:%S"


map = {
    "ttf": "font/ttf",
}
