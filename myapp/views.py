from django.shortcuts import render, HttpResponse

def test(response):
    return HttpResponse("This is a test response.")