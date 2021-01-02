from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class IndexViex(View):
    def get(self, request):
        result = render(request, "landing/index.html")

        return result
