from django.http import HttpResponse,JsonResponse
def hello_test (request):
    return HttpResponse('hello world')
def hello_test_ (request):
    return JsonResponse({'key':'value'}) 