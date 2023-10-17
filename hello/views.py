from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("--------------Hi HPE Team good afternoon, My Name is Mario Ortega, I am learning AZURE Cloud Computing[AZ900]-------------- ")
