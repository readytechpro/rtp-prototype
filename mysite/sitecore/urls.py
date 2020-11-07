from django.urls import path
from . import views
from .views import FAQListView

urlpatterns = [
    path('', views.index, name='index'),
    path('faq/', FAQListView.as_view(), name='faq')
]