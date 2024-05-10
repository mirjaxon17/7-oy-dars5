from django.urls import path
from .views import CategoryListView,ProductsListView,SearchResultsView

urlpatterns = [
    path('category/',CategoryListView.as_view(),name='category'),
    path('product/',ProductsListView.as_view(),name='product'),
    path('search/', SearchResultsView.as_view(), name='search'),

]



