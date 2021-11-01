from django.http import HttpResponse


def index(request):
    return HttpResponse(""
                        "<title>Greetings</title>"
                        "<h1 style='text-align: center; margin: 2%'>Hello World !</h1>"
                        "<hr>"
                        "")
