from framework.types import RequestT
from handlers.index import handler_index
from handlers.logo import handler_logo
from handlers.not_found import handler_404
from handlers.styles import handler_styles

handlers = {
    "/": handler_index,
    "/logo.png/": handler_logo,
    "/xxx/": handler_styles,
}


def application(environ: dict, start_response):

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
    )

    response = handler(request)

    start_response(response.status, list(response.headers.items()))

    yield response.payload
