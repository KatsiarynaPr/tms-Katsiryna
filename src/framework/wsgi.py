import random
from mimetypes import guess_type

from framework.consts import DIR_STATIC


def application(environ, start_response):
    url = environ["PATH_INFO"]

    handlers = {"/": handler_index}

    handler = handlers.get(url, handler_404)

    status = "200 OK"
    headers = {
        "Content-type": "text/html",
    }
    payload = handler(environ)

    start_response(status, list(headers.items()))

    yield payload


def read_static(file_name: str) -> bytes:
    path = DIR_STATIC / file_name

    with path.open("rb") as fp:
        payload = fp.read()

    return payload


def handler_index(_environ) -> bytes:
    basde_html = read_static("_base.html").decode()
    index_html = read_static("index.html").decode()
    text = basde_html.format(xxx=index_html)
    return text.encode()


def handler_404(environ) -> bytes:
    url = environ["PATH_INFO"]
    pin = random.randint(1, 10000)
    advice = "https://fucking-great-advice.ru/advice/" + str(pin)
    msg = f'Your path: {url} not found. Read the advice ---> <a href="{advice}">ADVICE</a> !!!'

    return msg.encode()
