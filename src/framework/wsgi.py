from framework import errors
from framework.db import find_user
from framework.types import RequestT
from framework.utils import authenticate
from framework.utils import build_cookies
from framework.utils import build_form_data
from framework.utils import get_request_body
from framework.utils import get_request_headers
from framework.utils import get_request_method
from framework.utils import get_request_path
from framework.utils import get_request_query
from handlers import get_handler_and_kwargs
from handlers import special


def application(environ: dict, start_response):
    path = get_request_path(environ)
    method = get_request_method(environ)
    handler, kwargs = get_handler_and_kwargs(path)
    request_headers = get_request_headers(environ)
    query = get_request_query(environ)
    body = get_request_body(environ)
    form_data = build_form_data(body)
    cookies = build_cookies(request_headers)

    request = RequestT(
        body=body,
        cookies=cookies,
        form_data=form_data,
        headers=request_headers,
        kwargs=kwargs,
        method=method,
        path=path,
        query=query,
    )
    authenticate(request)
    try:
        response = handler(request)
    except errors.NotFound:
        response = special.handler_404(request)
    except Exception:
        response = special.handler_500(request)

    start_response(
        response.status, list((response.headers or {}).items())
    )  # DON'T ANDESTEND

    yield response.payload or b""
