from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import CategoryListAPIViewSet,ProductlAPIViewSet,UsersListAPIViewSet
from rest_framework.authtoken import views
router = DefaultRouter()
router.register('category',CategoryListAPIViewSet)
router.register('product',ProductlAPIViewSet)
router.register('users',UsersListAPIViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('',include(router.urls)),
    path('',include(router.urls)),
    path('auth/',views.obtain_auth_token),

]
