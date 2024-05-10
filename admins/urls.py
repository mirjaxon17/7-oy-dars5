from django.urls import path
from .views import AdminViews,AdresViews

urlpatterns = [
    path('admins/',AdminViews.as_view(),name='admins'),
    path('adress/',AdresViews.as_view(),name='adress'),

]