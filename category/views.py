from django.shortcuts import render, redirect
from django.views import View
from .models import Products,Category,Search
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class CategoryListView(View):
    def get(self,request):
        category = Category.objects.all()
        contex = {
            'category':category,
        }
        return render(request, 'main/shop.html',contex)

class ProductsListView(View):
    def get(self,request):
        products = Products.objects.all()
        contex = {
            'product':products
        }
        return render(request, 'main/shop-detail.html',contex)


class SearchResultsView(View):
    def get(self, request):
        query = request.GET.get('query')
        results = Products.objects.filter(title=query)
        return render(request, 'search_results.html', {'results': results, 'query': query})





