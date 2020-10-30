import mimetypes

from framework.types import RequestT
from framework.types import ResponseT
from framework.utils import read_static


def handler_logo(_request: RequestT) -> ResponseT:
    file_name = "logo.jpg"
    payload = read_static(file_name)
    status = "200 OK"
    headers = {
        "Content-type": mimetypes.guess_type(file_name)[0],
    }

    return ResponseT(status, headers, payload)
