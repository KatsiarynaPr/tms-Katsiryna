from framework.types import RequestT
from framework.types import ResponseT
from framework.utils import build_status
from framework.utils import read_static


def handler_logo(_request: RequestT) -> ResponseT:
    payload = read_static("logo.jpg")
    status = build_status(200)
    headers = {
        "Content-type": payload.content_type,
    }
    payload = payload.encode()
    return ResponseT(status, headers, payload)
