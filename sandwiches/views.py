import json

from django.views import View
from django.http.response import JsonResponse

from .models import Sandwich, Bread, Topping, Cheese, Sauce


class BreadView(View):
    """
    빵 추가하기
    """
    def post(self, request):
        try:
            data = json.loads(request.body)
            if Bread.objects.filter(name=data['name']).exists():
                return JsonResponse(
                    {'message': 'BREAD_ALREADY_EXIST'},
                    status=400)
            Bread.objects.create(
                    name=data['name'],
                    quantity=data['quantity'],
                    price=data['price'])
            return JsonResponse({'message': 'BREAD_CREATED'}, status=201)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)


class BreadListView(View):
    """
    빵 재고 목록 보여주기(이름, 재고 숫자, 가격)
    """
    def get(self, request):
        breads = Bread.objects.all()
        if not breads:
            return JsonResponse({'message': 'BREADS_NOT_FOUND'}, status=404)
        breads = {
            'breads': [
                {
                    'name': bread.name,
                    'stocks': bread.quantity,
                    'per_price': bread.price
                }
                for bread in breads
            ]
        }
        return JsonResponse(breads, status=200)


class BreadDetailView(View):
    """
    빵 정보 수정하기
    빵 정보 삭제하기
    """
    def put(self, request, name):
        try:
            data = json.loads(request.body)
            bread = Bread.objects.get(name=name)
            if bread:
                if data['quantity']:
                    bread.quantity = data['quantity']
                if data['price']:
                    bread.price = data['price']
                bread.save()
            return JsonResponse({'message': 'BREAD_UPDATED'}, status=200)
        except Bread.DoesNotExist:
            return JsonResponse({'message': 'BREAD_NOT_FOUND'}, status=404)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

    def delete(self, request, name):
        try:
            bread = Bread.objects.get(name=name)
            if bread:
                bread.delete()
                return JsonResponse({'message': 'BREAD_DELETED'}, status=200)
        except Bread.DoesNotExist:
            return JsonResponse({'message': 'BREAD_NOT_FOUND'}, status=404)
