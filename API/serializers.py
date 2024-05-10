from rest_framework import serializers
from category.models import  Category,Products
from users.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("title","image","last_updated")


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ("title","image","price","category")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name","last_name","ade")

