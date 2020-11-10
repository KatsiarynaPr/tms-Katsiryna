from pathlib import Path

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
