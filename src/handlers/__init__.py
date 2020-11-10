import re
from typing import Dict
from typing import Tuple

from framework.types import HandlerT
from handlers import special
from handlers.error import make_error
from handlers.hello import handler_hello
from handlers.index import handler_index

urlpatterns: Dict[re.compile, HandlerT] = {
    re.compile(_path_pattern): _handler
    for _path_pattern, _handler in {
        "^/$": handler_index,
        "^/e/$": make_error,
        "^/h/$": handler_hello,
        "^/s/(?P<file_name>.+)$": special.handler_static,
    }.items()
}


def get_handler_and_kwargs(path: str) -> Tuple[HandlerT, dict]:
    handler = special.handler_404
    kwargs = {}

    for current_path_regex, current_handler in urlpatterns.items():
        if match := current_path_regex.match(path):
            handler = current_handler
            kwargs = match.groupdict()
            break

    return handler, kwargs
