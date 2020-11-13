import random

from framework.types import RequestT
from framework.types import ResponseT
from framework.utils import build_status


def handler_404(request: RequestT) -> ResponseT:
    url = request.path
    pin = random.randint(1, 10000)
    advice = "https://fucking-great-advice.ru/advice/" + str(pin)
    headers_string = [f"{h} -> {v}" for h, v in request.headers.items()]
    headers_text = ""
    for item in headers_string:
        headers_text = headers_text + item + "<br>"
    msg = f"""Your path: {url} not found. Read the advice ---> <a href="{advice}">ADVICE</a> !!!
   {headers_text}
    """
    payload = msg.encode()
    status = build_status(404)
    headers = {
        "Content-type": "text/html",
    }

    return ResponseT(status, headers, payload)


def handler_405(request: RequestT) -> ResponseT:
    status = build_status(405)
    payload = f"Resource {request.path} does not support {request.method} requests."
    headers = {"Content-type": "text/plain"}

    return ResponseT(
        status=status,
        headers=headers,
        payload=payload.encode(),
    )
