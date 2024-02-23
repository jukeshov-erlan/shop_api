from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CategoryViewSet, ProductViewSet, ProductImageView


router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)
# print(router.urls)

urlpatterns = [
    path('products/add-product-image/', ProductImageView.as_view()),
    path('', include(router.urls)),

]


# urlpatterns = [
#     path('products/', ProductViewSet.as_view({'get': 'list', 'post': 'create'})),
#     path('products/<slug:pk>/', ProductViewSet.as_view({'get': 'retrieve', 'put': 'update'}))
# ]