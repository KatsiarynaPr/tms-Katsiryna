from urllib.parse import parse_qs

from framework.types import RequestT
from handlers.error import make_error
from handlers.hello import handler_hello
from handlers.index import handler_index
from handlers.logo import handler_logo
from handlers.not_found import handler_404
from handlers.server_error import handler_500
from handlers.styles import handler_styles

handlers = {
    "/": handler_index,
    "/logo.png/": handler_logo,
    "/xxx/": handler_styles,
    "/e/": make_error,
    "/h/": handler_hello,
}


def application(environ: dict, start_response):

    try:
        path = environ["PATH_INFO"]

        handler = handlers.get(path, handler_404)

        request_headers = {
            key[5:]: environ[key]
            for key in filter(lambda i: i.startswith("HTTP_"), environ)
        }

        request = RequestT(
            method=environ["PATH_INFO"],
            path=path,
            headers=request_headers,
            query=parse_qs(environ.get("QUERY_STRING") or ""),
        )

        response = handler(request)
    except Exception:
        response = handler_500()

    start_response(response.status, list(response.headers.items()))

    yield response.payload
