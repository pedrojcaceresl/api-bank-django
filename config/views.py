from django.http import JsonResponse, HttpResponse

def health_check(request):
    return JsonResponse({"status": "Online", "health": "ok"})

def mensaje(request):
    return JsonResponse({"name": "Romy", "lastName": "Cardozo"})

def saludar(request):
    return HttpResponse("Holi")
