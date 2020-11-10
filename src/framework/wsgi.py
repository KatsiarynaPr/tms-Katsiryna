from framework.types import RequestT
from framework.errors import NotFound
from handlers import get_handler_and_kwargs
from framework.utils import get_request_headers
from handlers import special
from framework.utils import get_query
from framework.utils import get_body
from framework.utils import get_form_data

def application(environ: dict, start_response):
    path = environ["PATH_INFO"]
    method = environ["REQUEST_METHOD"]
    handler, kwargs = get_handler_and_kwargs(path)
    request_headers = get_request_headers(environ)
    query = get_query(environ)
    body = get_body(environ)
    form_data = get_form_data(body)

    request = RequestT(
        body=body,
        form_data=form_data,
        headers=request_headers,
        kwargs=kwargs,
        method=method,
        path=path,
        query=query,
    )
    try:
        response = handler(request)
    except NotFound:
        response = special.handler_404(request)
    except Exception:
        response = special.handler_500(request)

    start_response(response.status, list(response.headers.items()))

    yield response.payload