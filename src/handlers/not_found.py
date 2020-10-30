import random

from framework.types import RequestT
from framework.types import ResponseT


def handler_404(request: RequestT) -> ResponseT:
    url = request.path
    pin = random.randint(1, 10000)
    advice = "https://fucking-great-advice.ru/advice/" + str(pin)
    msg = f'Your path: {url} not found. Read the advice ---> <a href="{advice}">ADVICE</a> !!!'
    payload = msg.encode()
    status = "404 Not Found"
    headers = {
        "Content-type": "text/html",
    }

    return ResponseT(status, headers, payload)
