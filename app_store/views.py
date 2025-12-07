from django.http import JsonResponse, HttpResponse
from .models import DATABASE


def product_view_json(request) -> JsonResponse:
    if request.method == 'GET':
        return JsonResponse(DATABASE, json_dumps_params={'ensure_ascii': False,
                                                         'indent': 4})


def shop_view(request) -> HttpResponse:
    if request.method == 'GET':
        with open('app_store/shop.html', 'r', encoding='utf8') as f:
            data = f.read()
        return HttpResponse(data)
