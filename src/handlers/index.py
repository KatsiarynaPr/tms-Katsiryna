from framework.types import RequestT
from framework.types import ResponseT
from framework.utils import read_static


def handler_index(_request: RequestT) -> ResponseT:
    basde_html = read_static("_base.html").decode()
    index_html = read_static("index.html").decode()
    text = basde_html.format(xxx=index_html).encode()

    status = "200 OK"
    headers = {
        "Content-type": "text/html",
    }

    return ResponseT(
        status=status,
        headers=headers,
        payload=text,
    )
