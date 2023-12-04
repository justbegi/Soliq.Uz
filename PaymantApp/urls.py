from django.urls import path

from .views import AddMoneyView, Add_Card,CheckView

urlpatterns = [
    path("add_money/", AddMoneyView.as_view()),
    path("add_card/", Add_Card.as_view()),
    path("createcheck/",CheckView.as_view())
]
