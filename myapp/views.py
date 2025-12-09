from django.shortcuts import render, HttpResponse

# Auser
# Buser

def test(response):
    return HttpResponse("This is a test response.")

def aweb(response):
    return HttpResponse("This is a aweb response.")
# Buser
def test(response):
    return HttpResponse("This is a test response.")

def bweb(response):
    print("hello world")
    return HttpResponse("Hello, this is bweb view response.完成!!")
