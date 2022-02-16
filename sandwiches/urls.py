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
    path("cheese/", views.CheeseView.as_view()),
    path("cheese/list/", views.CheeseListView.as_view()),
    path("cheese/<str:name>/", views.CheeseDetailView.as_view()),
    path("sauce/", views.SauceView.as_view()),
    path("sauce/list/", views.SauceListView.as_view()),
    path("sauce/<str:name>/", views.SauceDetailView.as_view()),
    path("", views.SandwichView.as_view()),
    path("list/", views.SandwichListView.as_view()),
    path("<int:pk>/", views.SandwichDetailView.as_view()),
]
