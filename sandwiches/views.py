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


class ToppingView(View):
    """
    토핑 추가하기
    """
    def post(self, request):
        try:
            data = json.loads(request.body)
            if Topping.objects.filter(name=data['name']).exists():
                return JsonResponse(
                    {'message': 'TOPPING_ALREADY_EXIST'},
                    status=400)
            Topping.objects.create(
                    name=data['name'],
                    quantity=data['quantity'],
                    price=data['price'])
            return JsonResponse({'message': 'TOPPING_CREATED'}, status=201)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)


class ToppingListView(View):
    """
    토핑 재고 목록 보여주기(이름, 재고 숫자, 가격)
    """
    def get(self, request):
        toppings = Topping.objects.all()
        if not toppings:
            return JsonResponse({'message': 'TOPPINGS_NOT_FOUND'}, status=404)
        toppings = {
            'toppings': [
                {
                    'name': topping.name,
                    'stocks': topping.quantity,
                    'per_price': topping.price
                }
                for topping in toppings
            ]
        }
        return JsonResponse(toppings, status=200)


class ToppingDetailView(View):
    """
    토핑 정보 수정하기
    토핑 정보 삭제하기
    """
    def put(self, request, name):
        try:
            data = json.loads(request.body)
            topping = Topping.objects.get(name=name)
            if topping:
                if data['quantity']:
                    topping.quantity = data['quantity']
                if data['price']:
                    topping.price = data['price']
                topping.save()
            return JsonResponse({'message': 'TOPPING_UPDATED'}, status=200)
        except Topping.DoesNotExist:
            return JsonResponse({'message': 'TOPPING_NOT_FOUND'}, status=404)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

    def delete(self, request, name):
        try:
            topping = Topping.objects.get(name=name)
            if topping:
                topping.delete()
                return JsonResponse({'message': 'TOPPING_DELETED'}, status=200)
        except Topping.DoesNotExist:
            return JsonResponse({'message': 'TOPPING_NOT_FOUND'}, status=404)


class CheeseView(View):
    """
    치즈 추가하기
    """
    def post(self, request):
        try:
            data = json.loads(request.body)
            if Cheese.objects.filter(name=data['name']).exists():
                return JsonResponse(
                    {'message': 'CHEESE_ALREADY_EXIST'},
                    status=400)
            Cheese.objects.create(
                    name=data['name'],
                    quantity=data['quantity'],
                    price=data['price'])
            return JsonResponse({'message': 'CHEESE_CREATED'}, status=201)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)


class CheeseListView(View):
    """
    치즈 재고 목록 보여주기(이름, 재고 숫자, 가격)
    """
    def get(self, request):
        cheeses = Cheese.objects.all()
        if not cheeses:
            return JsonResponse({'message': 'CHEESES_NOT_FOUND'}, status=404)
        cheeses = {
            'cheeses': [
                {
                    'name': cheese.name,
                    'stocks': cheese.quantity,
                    'per_price': cheese.price
                }
                for cheese in cheeses
            ]
        }
        return JsonResponse(cheeses, status=200)


class CheeseDetailView(View):
    """
    치즈 정보 수정하기
    치즈 정보 삭제하기
    """
    def put(self, request, name):
        try:
            data = json.loads(request.body)
            cheese = Cheese.objects.get(name=name)
            if cheese:
                if data['quantity']:
                    cheese.quantity = data['quantity']
                if data['price']:
                    cheese.price = data['price']
                cheese.save()
            return JsonResponse({'message': 'CHEESE_UPDATED'}, status=200)
        except Cheese.DoesNotExist:
            return JsonResponse({'message': 'CHEESE_NOT_FOUND'}, status=404)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

    def delete(self, request, name):
        try:
            cheese = Cheese.objects.get(name=name)
            if cheese:
                cheese.delete()
                return JsonResponse({'message': 'CHEESE_DELETED'}, status=200)
        except Cheese.DoesNotExist:
            return JsonResponse({'message': 'CHEESE_NOT_FOUND'}, status=404)
