import json

from django.views import View
from django.http.response import JsonResponse
from django.db import transaction
from django.db.models import Q

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
                    {'message': 'BREAD_ALREADY_EXIST'}, status=400)
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
                    {'message': 'TOPPING_ALREADY_EXIST'}, status=400)
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
                    {'message': 'CHEESE_ALREADY_EXIST'}, status=400)
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


class SauceView(View):
    """
    소스 추가하기
    """
    def post(self, request):
        try:
            data = json.loads(request.body)
            if Sauce.objects.filter(name=data['name']).exists():
                return JsonResponse(
                    {'message': 'SAUCE_ALREADY_EXIST'}, status=400)
            Sauce.objects.create(
                    name=data['name'],
                    quantity=data['quantity'],
                    price=data['price'])
            return JsonResponse({'message': 'SAUCE_CREATED'}, status=201)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)


class SauceListView(View):
    """
    소스 재고 목록 보여주기(이름, 재고 숫자, 가격)
    """
    def get(self, request):
        sauces = Sauce.objects.all()
        if not sauces:
            return JsonResponse({'message': 'SAUCES_NOT_FOUND'}, status=404)
        sauces = {
            'sauces': [
                {
                    'name': sauce.name,
                    'stocks': sauce.quantity,
                    'per_price': sauce.price
                }
                for sauce in sauces
            ]
        }
        return JsonResponse(sauces, status=200)


class SauceDetailView(View):
    """
    소스 정보 수정하기
    소스 정보 삭제하기
    """
    def put(self, request, name):
        try:
            data = json.loads(request.body)
            sauce = Sauce.objects.get(name=name)
            if sauce:
                if data['quantity']:
                    sauce.quantity = data['quantity']
                if data['price']:
                    sauce.price = data['price']
                sauce.save()
            return JsonResponse({'message': 'SAUCE_UPDATED'}, status=200)
        except Sauce.DoesNotExist:
            return JsonResponse({'message': 'SAUCE_NOT_FOUND'}, status=404)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

    def delete(self, request, name):
        try:
            sauce = Sauce.objects.get(name=name)
            if sauce:
                sauce.delete()
                return JsonResponse({'message': 'SAUCE_DELETED'}, status=200)
        except Sauce.DoesNotExist:
            return JsonResponse({'message': 'SAUCE_NOT_FOUND'}, status=404)


class SandwichView(View):
    """
    샌드위치 만들기
    """
    def post(self, request):
        try:
            data = json.loads(request.body)
            bread = data.get('bread')
            toppings = data.get('toppings')
            cheese = data.get('cheese')
            sauces = data.get('sauces')
            bread_obj = Bread.objects.get(name=bread[0])
            toppings_obj = [Topping.objects.get(name=topping) for topping in toppings]
            toppings_price = [topping.price for topping in toppings_obj]
            cheese_obj = Cheese.objects.get(name=cheese[0])
            sauces_obj = [Sauce.objects.get(name=sauce) for sauce in sauces]
            sacues_price = [sauce.price for sauce in sauces_obj]
            if not (bread and toppings and cheese and sauces):
                return JsonResponse(
                    {'message': 'REQUIRED_MORE_INGREDIENT'}, status=400)
            if bread_obj.quantity == 0 or len(bread) >= 2:
                return JsonResponse(
                    {'message': 'INSUFFICIENT_BREAD'}, status=400)
            if any(topping_obj.quantity == 0 for topping_obj in toppings_obj) \
                or len(toppings) >= 3:
                return JsonResponse(
                    {'message': 'INSUFFICIENT_TOPPINGS'}, status=400)
            if cheese_obj.quantity == 0 or len(cheese) >= 2:
                return JsonResponse(
                    {'message': 'INSUFFICIENT_CHEESE'}, status=400)
            if any(sauce_obj.quantity == 0 for sauce_obj in sauces_obj) or \
                len(sauces) >= 3:
                return JsonResponse(
                    {'message': 'INSUFFICIENT_SAUCE'}, status=400)
            with transaction.atomic():
                sandwich = Sandwich.objects.create(
                    bread=bread_obj,
                    cheese=cheese_obj,
                    price=bread_obj.price+cheese_obj.price+sum(toppings_price)+sum(sacues_price)
                )
                sandwich = Sandwich.objects.select_related('bread', 'cheese').get(pk=sandwich.pk)
                sandwich.toppings.add(*toppings_obj)
                sandwich.sauces.add(*sauces_obj)
                sandwich.bread.quantity -= 1
                sandwich.bread.save()
                sandwich.cheese.quantity -= 1
                sandwich.cheese.save()
                for topping_obj in sandwich.toppings.all():
                    topping_obj.quantity -= 1
                    topping_obj.save()
                for sauce_obj in sandwich.sauces.all():
                    sauce_obj.quantity -= 1
                    sauce_obj.save()
            return JsonResponse({'message': 'SANDWICH_CREATED'}, status=201)
        except Bread.DoesNotExist:
            return JsonResponse({'message': 'BREAD_NOT_FOUND'}, status=404)
        except Topping.DoesNotExist:
            return JsonResponse({'message': 'TOPPING_NOT_FOUND'}, status=404)
        except Cheese.DoesNotExist:
            return JsonResponse({'message': 'CHEESE_NOT_FOUND'}, status=404)
        except Sauce.DoesNotExist:
            return JsonResponse({'message': 'SAUCE_NOT_FOUND'}, status=404)


class SandwichListView(View):
    """
    샌드위치 목록 보여주기(1페이지당 10개씩, 재료/가격별 필터링)
    """
    def get(self, request):
        page = int(request.GET.get('page', 1))
        limit = 10
        offset = (page - 1) * limit
        bread = request.GET.get('bread')
        topping = request.GET.get('topping')
        cheese = request.GET.get('cheese')
        sauce = request.GET.get('sauce')
        start_price = int(request.GET.get('start_price'))
        end_price = int(request.GET.get('end_price'))
        if bread:
            sandwiches = Sandwich.objects.filter(bread__name__icontains=bread)\
                [offset:offset+limit]
        if topping:
            sandwiches = Sandwich.objects.filter(toppings__name__icontains=topping)\
                [offset:offset+limit]
        if cheese:
            sandwiches = Sandwich.objects.filter(cheese__name__icontains=cheese)\
                [offset:offset+limit]
        if sauce:
            sandwiches = Sandwich.objects.filter(sauces__name__icontains=sauce)\
                [offset:offset+limit]
        if start_price < 0 or end_price < 0:
            return JsonResponse({'message': 'INVALID_VALUE'}, status=400)
        if start_price > end_price:
            return JsonResponse({'message': 'INVALID_RANGE'}, status=400)
        if start_price and end_price:
            sandwiches = Sandwich.objects.filter(price__range=(start_price, end_price))\
                [offset:offset+limit]
        if not sandwiches:
            return JsonResponse({'message': 'NOT_FOUND_SANDWICH'}, status=404)
        return JsonResponse({'sandwich': [
            {'id': sandwich.pk} for sandwich in sandwiches]}, status=200)


class SandwichDetailView(View):
    """
    샌드위치 상세보기
    샌드위치 삭제하기
    """
    def get(self, request, pk):
        try:
            sandwich = Sandwich.objects.get(pk=pk)
            result = {
                'sandwich': {
                    'bread': {
                        'name': sandwich.bread.name,
                        'price': sandwich.bread.price,
                    },
                    'toppings': [
                        {
                            'name': topping.name,
                            'price': topping.price,
                        } for topping in sandwich.toppings.all()
                    ],
                    'cheese': {
                        'name': sandwich.cheese.name,
                        'price': sandwich.cheese.price,
                    },
                    'sauces': [
                        {
                            'name': sauce.name,
                            'price': sauce.price,
                        } for sauce in sandwich.sauces.all()
                    ],
                    'price': sandwich.price
                }
            }
            return JsonResponse(result, status=404)
        except Sandwich.DoesNotExist:
            return JsonResponse({'message': 'SANDWICH_NOT_FOUND'}, status=404)

    def delete(self, request, pk):
        pass
