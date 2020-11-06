from framework.types import RequestT
from framework.types import ResponseT
from framework.utils import build_status
from framework.utils import read_static


def handler_styles(_request: RequestT) -> ResponseT:
    styles = read_static("styles.css")

    status = build_status(200)
    headers = {
        "Content-type": "text/css",
    }

    return ResponseT(status, headers, styles)
