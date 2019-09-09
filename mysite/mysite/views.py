from django.http import HttpResponse

def homePage(request):
    return HttpResponse('Home Page')


def about(request):
    return HttpResponse('about')
