from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect


def hello(request: HttpRequest) -> HttpResponse:
    name = request.session.get("name")
    address = request.session.get("address")
    context = {
        "name_header": name or "anonymous",
        "name_value": name or "",
        "address_header": address or "nowhere",
        "address_value": address or "",
    }
    result = render(request, "hello/hello.html", context=context)

    return HttpResponse(result)

def view_hello_greet(request: HttpRequest) -> HttpResponse:
    name = request.POST.get("name")
    address = request.POST.get("address")

    request.session["name"] = name
    request.session["address"] = address

    return redirect("/h/")


def view_hello_reset(request: HttpRequest) -> HttpResponse:
    request.session.clear()
    return redirect("/h/")