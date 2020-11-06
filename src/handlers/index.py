from framework.types import RequestT
from framework.types import ResponseT
from framework.utils import read_static
from framework.utils import build_status

#def handler_index(_request: RequestT) -> ResponseT:
 #   base = read_static("_base.html")
  #  base_html = base.content.decode()
   # index_html = read_static("index.html").content.decode()

    #result = base_html.format(xxx=index_html)
    #result = result.encode()

    #status = build_status(200)
    #headers = {
     #   "Content-type": base.content_type,
    #}

    #return ResponseT(
     #   status=status,
      #  headers=headers,
       # payload=result,
    #)

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