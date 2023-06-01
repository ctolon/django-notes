from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# http://<host>:<port>/myapp/
def index(request) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the polls index.")


