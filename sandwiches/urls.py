from django.urls import path

from . import views

app_name = "sandwiches"

urlpatterns = [
    path("bread/", views.BreadView.as_view()),
    path("bread/list/", views.BreadListView.as_view()),
    path("bread/<str:name>/", views.BreadDetailView.as_view()),
    path("topping/", views.ToppingView.as_view()),
    path("topping/list/", views.ToppingListView.as_view()),
    path("topping/<str:name>/", views.ToppingDetailView.as_view()),
]
