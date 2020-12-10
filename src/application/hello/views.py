from django import forms
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import FormView


class HelloForm(forms.Form):
    name = forms.CharField()
    address = forms.CharField()


class HelloView(FormView):
    template_name = "hello/hello.html"
    success_url = "/h/"
    form_class = HelloForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        name = self.request.session.get("name")
        address = self.request.session.get("address")
        context.update(
            {
                "name": name or "anonymous",
                "address": address or "nowhere",
            }
        )
        return context

    def form_valid(self, form):
        name = form.cleaned_data["name"]
        address = form.cleaned_data["address"]
        self.request.session["name"] = name
        self.request.session["address"] = address

        return super().form_valid(form)


# def hello(request: HttpRequest) -> HttpResponse:
#    name = request.session.get("name")
#   address = request.session.get("address")
#  context = {
#     "name_header": name or "anonymous",
#    "name_value": name or "",
#   "address_header": address or "nowhere",
#  "address_value": address or "",
# }
# result = render(request, "hello/hello.html", context=context)

# return HttpResponse(result)


# def view_hello_greet(request: HttpRequest) -> HttpResponse:
# name = request.POST.get("name")
# address = request.POST.get("address")

# request.session["name"] = name
# request.session["address"] = address

# return redirect("/h/")


def view_hello_reset(request: HttpRequest) -> HttpResponse:
    request.session.clear()
    return redirect("/h/")
