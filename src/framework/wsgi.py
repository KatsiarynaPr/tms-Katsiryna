from mimetypes import guess_type

from framework.consts import DIR_STATIC


def application(environ, start_response):
    url = environ["PATH_INFO"]
    if url == "/xxx/":
        status = "200 OK"
        headers = {
            "Content-type": guess_type("style.css")[0],
        }
        payload = read_from_style_css()
        start_response(status, list(headers.items()))

        yield payload

    elif url == "/logo.png/":
        status = "200 OK"
        headers = {
            "Content-type": guess_type("logo.jpg")[0],
        }
        payload = read_from_logo_png()
        start_response(status, list(headers.items()))

        yield payload

    else:
        status = "200 OK"
        headers = {
            "Content-type": guess_type("index.html")[0],
        }
        payload = read_from_index_html()

        start_response(status, list(headers.items()))

        yield payload


def read_from_index_html():
    path = DIR_STATIC / "index.html"

    with path.open("r") as fp:
        payload = fp.read()

    payload = payload.encode()
    return payload


def read_from_style_css():
    path = DIR_STATIC / "styles.css"

    with path.open("r") as fp:
        payload = fp.read()

    payload = payload.encode()
    return payload


def read_from_logo_png():
    path = DIR_STATIC / "logo.jpg"

    with path.open("rb") as fp:
        payload = fp.read()

    return payload
